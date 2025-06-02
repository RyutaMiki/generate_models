
from datetime import datetime
from sqlalchemy import (
    Column, String, Text, Integer, Float, Boolean, Date, TIMESTAMP, DECIMAL,
    Index, UniqueConstraint, ForeignKey, ForeignKeyConstraint,
    PrimaryKeyConstraint, CheckConstraint, text, func, SmallInteger
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import uuid
from enumType import EnumType

Base = declarative_base()


class LineLinkCode(Base):
    """
    　LINE連携用ワンタイムコード
    """
    __tablename__ = 't_line_link_code'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    code = Column('code', String(8, collation='ja_JP.utf8'), nullable=False, unique=True, comment='ワンタイムコード')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), nullable=False, index=True, comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    expires_at = Column('expires_at', TIMESTAMP, nullable=False, comment='LINE連携用ワンタイムコードが使える期限')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default=datetime.now, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者従業員コード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者従業員コード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __mapper_args__ = {
        'version_id_col': update_count    }
    __table_args__ = (Index('ix_t_line_link_code', "code"), UniqueConstraint("code"),)
