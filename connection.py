"""
db_connection.py
~~~~~~~~~~~~~~~~
DSN を ``DATABASE_URL`` から読んで QueuePool 付き Engine を作る薄ラッパー。
"""

from __future__ import annotations

import os
from typing import Optional

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import scoped_session, sessionmaker


class Connection:
    """
    SQLAlchemy Engine／Session ファクトリ（接続プーリング設定込み）

    Parameters
    ----------
    utility :
        ``send_error_logs(...)`` メソッドを持つロガー的オブジェクト。
        Engine 作成失敗時に呼ばれる。無ければ黙って無視。
    """

    # ---- デフォルト値（⇦ 好みに合わせてここだけ触れば全体に反映） ---------------- #
    DEFAULT_POOL_SIZE: int = 30       # 常時プールする上限
    DEFAULT_MAX_OVERFLOW: int = 60    # 足りなくなったとき臨時にいくつまで増殖するか
    DEFAULT_POOL_TIMEOUT: int = 30    # get() が待つ秒数（デフォ 30）
    DEFAULT_POOL_RECYCLE: int = 1800  # 秒経過でコネクションをリサイクル（MySQL wait_timeout 対策）
    DEFAULT_POOL_PRE_PING: bool = True  # 取得前に "SELECT 1" で死活確認（切断検知）

    def __init__(self, utility: Optional[object] = None) -> None:
        self.utility = utility
        self._engine: Optional[Engine] = None

    # ------------------------------------------------------------------ #
    # Engine                                                             #
    # ------------------------------------------------------------------ #
    def get_engine(
        self,
        *,
        dsn: Optional[str] = None,
        pool_size: int = DEFAULT_POOL_SIZE,
        max_overflow: int = DEFAULT_MAX_OVERFLOW,
        pool_timeout: int = DEFAULT_POOL_TIMEOUT,
        pool_recycle: int = DEFAULT_POOL_RECYCLE,
        pool_pre_ping: bool = DEFAULT_POOL_PRE_PING,
        **kwargs,
    ) -> Engine:
        """
        Engine を “遅延生成 & キャッシュ返却” する。

        引数でプーリング参数を上書き可（指定しなければクラス定数が効く）。
        他の SQLAlchemy Engine オプションは **kwargs にそのまま渡る。
        """
        # 既に作成済みならキャッシュを返す
        if self._engine is not None:
            return self._engine

        # .env 読み込み（毎回でも誤差レベル）
        load_dotenv(verbose=False)

        # DSN 解決
        dsn = dsn or os.getenv("DATABASE_URL")
        if not dsn:
            raise RuntimeError("DATABASE_URL が設定されていません（dsn 引数でも可）")

        # Engine 作成
        try:
            self._engine = create_engine(
                dsn,
                pool_size=pool_size,
                max_overflow=max_overflow,
                pool_timeout=pool_timeout,
                pool_recycle=pool_recycle,
                pool_pre_ping=pool_pre_ping,
                **kwargs,
            )
            return self._engine

        except Exception as exc:  # noqa: BLE001
            self._log_error("DB 接続で例外が発生", exc)
            raise

    # ------------------------------------------------------------------ #
    # Session factory convenience                                        #
    # ------------------------------------------------------------------ #
    def get_session_factory(self) -> scoped_session:
        """
        スレッドセーフな scoped_session を返す（初回呼び出しで Engine も初期化）。
        """
        engine = self.get_engine()
        return scoped_session(sessionmaker(bind=engine))

    # ------------------------------------------------------------------ #
    # Private helpers                                                    #
    # ------------------------------------------------------------------ #
    def _log_error(self, msg: str, exc: Exception) -> None:
        """ロガーがあれば送信。失敗しても握りつぶす。"""
        if self.utility is None or not hasattr(self.utility, "send_error_logs"):
            return
        try:
            self.utility.send_error_logs(
                None, "", 0, msg, "", str(exc), "", None,
            )
        except Exception:  # noqa: BLE001
            pass
