from enum import IntEnum


"""
Enum:HTTPステータス
SUCCESS　正常
CLIENT_ERROR クライアントエラー
UNAUTHORIZED 認証エラー
SERVER_ERROR サーバーエラー
SUCCESS_ROLEBACK 正常(DB更新なし)
"""


class HttpStatus(IntEnum):
    SUCCESS = 200
    CLIENT_ERROR = 400
    UNAUTHORIZED = 401
    NOT_FOUND = 404
    SERVER_ERROR = 500
    SUCCESS_ROLEBACK = 999

    @property
    def label(self) -> str:
        return {
            HttpStatus.SUCCESS: "正常",
            HttpStatus.CLIENT_ERROR: "クライアントエラー",
            HttpStatus.UNAUTHORIZED: "認証エラー",
            HttpStatus.NOT_FOUND: "未検出",
            HttpStatus.SERVER_ERROR: "サーバーエラー",
            HttpStatus.SUCCESS_ROLEBACK: "正常(DB更新なし)",
        }[self]


"""
Enum:リスクの可能性
HIGH_POSSIBILITY 高[確実又は可能性が極めて高い(よほど注意しないと発生する)]
MODERETE_POSIBILITY 中[可能性がある(注意していないと発生する)]
LOW_POSSIBILITY 低[ほとんどない(注意していなくてもほぼ発生しない)]
NONE 不明
"""


class PossibilityRisk(IntEnum):
    HIGH_POSSIBILITY = 1
    MODERETE_POSIBILITY = 2
    LOW_POSSIBILITY = 3
    NONE = 0

    @property
    def label(self) -> str:
        return {
            PossibilityRisk.HIGH_POSSIBILITY: "高[確実又は可能性が極めて高い(よほど注意しないと発生する)]",
            PossibilityRisk.MODERETE_POSIBILITY: "中[可能性がある(注意していないと発生する)]",
            PossibilityRisk.LOW_POSSIBILITY: "低[ほとんどない(注意していなくてもほぼ発生しない)]",
            PossibilityRisk.NONE: "不明",
        }[self]


"""
Enum:取引区分
A 顧客
B 協力会社
C 顧客&協力会社
D 見込み客
E その他
"""


class TransactionType(IntEnum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5

    @property
    def label(self) -> str:
        return {
            TransactionType.A: "顧客",
            TransactionType.B: "協力会社",
            TransactionType.C: "顧客&協力会社",
            TransactionType.D: "見込み客",
            TransactionType.E: "その他",
        }[self]


"""
Enum:請求単位
A 伝票単位
B 請求書単位
"""


class BillingUnit(IntEnum):
    A = 1
    B = 2

    @property
    def label(self) -> str:
        return {
            BillingUnit.A: "伝票単位",
            BillingUnit.B: "請求書単位",
        }[self]


"""
Enum:税転嫁区分
A 外税/伝票単位...伝票の各明細の金額は税抜として扱われます。消費税は伝票単位で一括して計算され、伝票の［消費税額］に表示されます。
B 外税/請求単位...伝票の各明細の金額は税抜として扱われます。消費税は請求締切の際に計算されます。伝票には消費税額が表示されません。
C 内税...伝票の各明細の金額は税込として扱われます。売上金額なども税込で計算されます。適格請求書等保存方式、区分記載請求書等保存方式の対象外です。
D 輸出（免税）...伝票の各明細の金額は、消費税の対象になりません。輸出（免税）取引の場合に選択します。
E 外税/手入力...伝票の各明細の金額は、［内訳］で「消費税」が選択された明細に消費税が自動計算されます。税額を直接入力する場合に選択します。
"""


class TaxPassThroughClassification(IntEnum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5

    @property
    def label(self) -> str:
        return {
            TaxPassThroughClassification.A: "外税/伝票単位",
            TaxPassThroughClassification.B: "外税/請求単位",
            TaxPassThroughClassification.C: "内税",
            TaxPassThroughClassification.D: "輸出（免税）",
            TaxPassThroughClassification.E: "外税/手入力",
        }[self]


"""
Enum:信用度の格付け
A 非常に優良
B 優良
C 通常
D やや注意
E 注意
F 要警戒
G 格付け対象外
"""


class CreditEvaluationMethod(IntEnum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7

    @property
    def label(self) -> str:
        return {
            CreditEvaluationMethod.A: "非常に優良",
            CreditEvaluationMethod.B: "優良",
            CreditEvaluationMethod.C: "通常",
            CreditEvaluationMethod.D: "やや注意",
            CreditEvaluationMethod.E: "注意",
            CreditEvaluationMethod.F: "要警戒",
            CreditEvaluationMethod.G: "格付け対象外",
        }[self]


"""
Enum:問題の原因
PROGRAM_BUG プログラムバグ
SPECIFICATION_BUG 仕様バグ
INSUFFICIENT_CONSIDERATION 検討不足
SPECIFICATION_CHANGE 仕様変更
NONE 不明
"""


class CauseOfTheProblem(IntEnum):
    PROGRAM_BUG = 1
    SPECIFICATION_BUG = 2
    INSUFFICIENT_CONSIDERATION = 3
    SPECIFICATION_CHANGE = 4
    NONE = 9

    @property
    def label(self) -> str:
        return {
            CauseOfTheProblem.PROGRAM_BUG: "プログラムバグ",
            CauseOfTheProblem.SPECIFICATION_BUG: "仕様バグ",
            CauseOfTheProblem.INSUFFICIENT_CONSIDERATION: "検討不足",
            CauseOfTheProblem.SPECIFICATION_CHANGE: "仕様変更",
            CauseOfTheProblem.NONE: "不明",
        }[self]


"""
Enum:リスクの強度
HIGH_INTEMSITY 高[極めて重大]
MODERETE_INTEMSITY 中[重大]
LOW_INTEMSITY 低[軽微]
NONE 不明
"""


class IntensityRisk(IntEnum):
    HIGH_INTEMSITY = 1
    MODERETE_INTEMSITY = 2
    LOW_INTEMSITY = 3
    NONE = 9

    @property
    def label(self) -> str:
        return {
            IntensityRisk.HIGH_INTEMSITY: "高[極めて重大]",
            IntensityRisk.MODERETE_INTEMSITY: "中[重大]",
            IntensityRisk.LOW_INTEMSITY: "低[軽微]",
            IntensityRisk.NONE: "不明",
        }[self]


"""
Enum:リスクの種類
CUSTOMER_RELATED_RISK 顧客関連のリスク
CONTRACTUAL_RISK 契約のリスク
REQUIREMENTS_RISK 要求事項のリスク
TEAMS_WORK_EXPERIENCE_RISK チームの業務経験リスク
MANAGEMENT_RISK マネジメントのリスク
ESTIMATION_RISK 見積りのリスク
RISK_DUE_CONSTRAINTS 制約条件によるリスク
RISK_DUE_TO_THE_COMPLEXITY_RISK 成果物の複雑性や規模によるリスク
CONTRACTOR_RISK 請負業者のリスク
NONE 不明
"""


class TypeOfRisk(IntEnum):
    CUSTOMER_RELATED_RISK = 1
    CONTRACTUAL_RISK = 2
    REQUIREMENTS_RISK = 3
    TEAMS_WORK_EXPERIENCE_RISK = 4
    MANAGEMENT_RISK = 5
    ESTIMATION_RISK = 6
    RISK_DUE_CONSTRAINTS = 7
    RISK_DUE_TO_THE_COMPLEXITY_RISK = 8
    CONTRACTOR_RISK = 9
    NONE = 0

    @property
    def label(self) -> str:
        return {
            TypeOfRisk.CUSTOMER_RELATED_RISK: "顧客関連のリスク",
            TypeOfRisk.CONTRACTUAL_RISK: "契約のリスク",
            TypeOfRisk.REQUIREMENTS_RISK: "要求事項のリスク",
            TypeOfRisk.TEAMS_WORK_EXPERIENCE_RISK: "チームの業務経験リスク",
            TypeOfRisk.MANAGEMENT_RISK: "マネジメントのリスク",
            TypeOfRisk.ESTIMATION_RISK: "見積りのリスク",
            TypeOfRisk.RISK_DUE_CONSTRAINTS: "制約条件によるリスク",
            TypeOfRisk.RISK_DUE_TO_THE_COMPLEXITY_RISK: "成果物の複雑性や規模によるリスク",
            TypeOfRisk.CONTRACTOR_RISK: "請負業者のリスク",
            TypeOfRisk.NONE: "不明",
        }[self]


"""
Enum:エンジン名
Artemis 総合エンジン
Kronos 勤怠エンジン
Laube ワークフローエンジン
Abundantia 給与エンジン
Panakeia 有給管理エンジン
Pan 36協定監視エンジン
Lucifer [個人用]勤怠エンジン
Score ランキングエンジン
Aqua AIエンジン
"""


class EngineName(IntEnum):
    Artemis = 1
    Kronos = 2
    Laube = 3
    Abundantia = 4
    Panakeia = 5
    Pan = 6
    Lucifer = 7
    Score = 8
    Aqua = 9

    @property
    def label(self) -> str:
        return {
            EngineName.Artemis: "総合エンジン",
            EngineName.Kronos: "勤怠エンジン",
            EngineName.Laube: "ワークフローエンジン",
            EngineName.Abundantia: "給与エンジン",
            EngineName.Panakeia: "有給管理エンジン",
            EngineName.Pan: "36協定監視エンジン",
            EngineName.Lucifer: "[個人用]勤怠エンジン",
            EngineName.Score: "ランキングエンジン",
            EngineName.Aqua: "AIエンジン",
        }[self]


"""
Enum:性別
MAN 男性
WOMAN 女性
NOT_SET 未設定
"""


class Sex(IntEnum):
    MAN = 1
    WOMAN = 2
    NOT_SET = 9

    @property
    def label(self) -> str:
        return {
            Sex.MAN: "男性",
            Sex.WOMAN: "女性",
            Sex.NOT_SET: "未設定",
        }[self]


"""
Enum:売上高
FEW 少ない
MEDIUM 普通
MANY 多い
"""


class SalesScale(IntEnum):
    FEW = 1
    MEDIUM = 2
    MANY = 3

    @property
    def label(self) -> str:
        return {
            SalesScale.FEW: "少ない",
            SalesScale.MEDIUM: "普通",
            SalesScale.MANY: "多い",
        }[self]


"""
Enum:利益高
FEW 少ない
MEDIUM 普通
MANY 多い
"""


class ProfitScale(IntEnum):
    FEW = 1
    MEDIUM = 2
    MANY = 3

    @property
    def label(self) -> str:
        return {
            ProfitScale.FEW: "少ない",
            ProfitScale.MEDIUM: "普通",
            ProfitScale.MANY: "多い",
        }[self]


"""
Enum:資本金
FEW 少ない
MEDIUM 普通
MANY 多い
"""


class CapitalScale(IntEnum):
    FEW = 1
    MEDIUM = 2
    MANY = 3

    @property
    def label(self) -> str:
        return {
            CapitalScale.FEW: "少ない",
            CapitalScale.MEDIUM: "普通",
            CapitalScale.MANY: "多い",
        }[self]


"""
Enum:成長率
SLOW 遅い
USUALLY 普通
FIRST 早い
"""


class GrowthScale(IntEnum):
    SLOW = 1
    USUALLY = 2
    FIRST = 3

    @property
    def label(self) -> str:
        return {
            GrowthScale.SLOW: "遅い",
            GrowthScale.USUALLY: "普通",
            GrowthScale.FIRST: "早い",
        }[self]


"""
Enum:従業員
FEW 少ない
MEDIUM 普通
MANY 多い
"""


class NumberEmployeeScale(IntEnum):
    FEW = 1
    MEDIUM = 2
    MANY = 3

    @property
    def label(self) -> str:
        return {
            NumberEmployeeScale.FEW: "少ない",
            NumberEmployeeScale.MEDIUM: "普通",
            NumberEmployeeScale.MANY: "多い",
        }[self]


"""
Enum:システム画面フラグ
ON システム画面
OFF システム画面以外
"""


class SystemScreenFlg(IntEnum):
    ON = 1
    OFF = 2

    @property
    def label(self) -> str:
        return {
            SystemScreenFlg.ON: "システム画面",
            SystemScreenFlg.OFF: "システム画面以外",
        }[self]


"""
Enum:画面種別
MAIN メイン画面
POPUP ポップアップ画面
DASH_BOARD ダッシュボード
"""


class ScreenType(IntEnum):
    MAIN = 1
    POPUP = 2
    DASH_BOARD = 3

    @property
    def label(self) -> str:
        return {
            ScreenType.MAIN: "メイン画面",
            ScreenType.POPUP: "ポップアップ画面",
            ScreenType.DASH_BOARD: "ダッシュボード",
        }[self]


"""
Enum:システム管理会社フラグ
ON システム管理会社
OFF 一般会社
"""


class SystemCompanyFlg(IntEnum):
    ON = 1
    OFF = 2

    @property
    def label(self) -> str:
        return {
            SystemCompanyFlg.ON: "システム管理会社",
            SystemCompanyFlg.OFF: "一般会社",
        }[self]


"""
Enum:課金免除フラグ
EXEMPTION 課金免除
NON_SUBSCRIPTION 課金
"""


class ChargeExemptionFlg(IntEnum):
    EXEMPTION = 1
    NON_EXEMPTION = 2

    @property
    def label(self) -> str:
        return {
            ChargeExemptionFlg.EXEMPTION: "課金免除",
            ChargeExemptionFlg.NON_EXEMPTION: "課金",
        }[self]


"""
Enum:社会保険
SUBSCRIPTION 加入
NON_SUBSCRIPTION 未加入
"""


class SocialInsurance(IntEnum):
    SUBSCRIPTION = 1
    NON_SUBSCRIPTION = 2

    @property
    def label(self) -> str:
        return {
            SocialInsurance.SUBSCRIPTION: "加入",
            SocialInsurance.NON_SUBSCRIPTION: "未加入",
        }[self]


"""
Enum:反映フラグ
WAIT 作成中
REFLECTED 反映済
NON_REFLECTED 未反映
ERROR_DUPLICATE 出勤中に出勤打刻エラー
"""


class ReflectionFlg(IntEnum):
    WAIT = 1
    REFLECTED = 2
    NON_REFLECTED = 3
    ERROR_DUPLICATE = 4

    @property
    def label(self) -> str:
        return {
            ReflectionFlg.WAIT: "作成中",
            ReflectionFlg.REFLECTED: "反映済",
            ReflectionFlg.NON_REFLECTED: "未反映",
            ReflectionFlg.ERROR_DUPLICATE: "出勤中に出勤打刻エラー",
        }[self]


"""
Enum:シフト確定フラグ
UNADJUSTED 未調整
UNDER_ADJUSTMENT 調整中
REFLECTED 確定
"""


class ShiftReflectionFlg(IntEnum):
    UNADJUSTED = 1
    UNDER_ADJUSTMENT = 3
    REFLECTED = 4

    @property
    def label(self) -> str:
        return {
            ShiftReflectionFlg.UNADJUSTED: "未調整",
            ShiftReflectionFlg.UNDER_ADJUSTMENT: "調整中",
            ShiftReflectionFlg.REFLECTED: "確定",
        }[self]


"""
Enum:エラー項目(Pan)
REAL_TOTAL_MINUTES 労働時間
JOB_TOTAL_MINUTES 所定労働時間
JOB_OVERWORK_MINUTES 所定外労働時間
JOB_HOLIDAY_DAYS 所定休日労働日数
JOB_HOLIDAY_HOURS 所定休日労働時間
LEGAL_JOB_MINUTES 法定労働時間
LEGAL_OVERWORK_MINUTES 法定外労働時間
LEGAL_HOLIDAY_OVERWORK_DAYS 法定休日労働日数
LEGAL_HOLIDAY_OVERWORK_MINUTES 法定休日労働時間
LATE_NIGHT_OVERWORK_MINUTES 深夜労働時間
BREAK_MINUTES 休憩時間
PAID_HOLIDAY_DAYS 有給日数
PAID_HOLIDAY_HOURS 有給時間数
CHILD_TIME_LEAVE_DAYS 育児休暇日数
CHILD_TIME_LEAVE_HOURS 育児時間休暇数
COMPENSATORY_HOLIDAY_DAYS 代休日数
LEAVE_DAYS 休職日数
CLOSED_DAYS 休業日数
SPECIAL_PROVISIONS_YEAR_COUNT 特別条項の摘要回数
UNIT_PRICE 時給
"""


class ErrorItem(IntEnum):
    REAL_TOTAL_MINUTES = 1
    JOB_TOTAL_MINUTES = 2
    JOB_OVERWORK_MINUTES = 3
    JOB_HOLIDAY_DAYS = 4
    JOB_HOLIDAY_HOURS = 5
    LEGAL_JOB_MINUTES = 6
    LEGAL_OVERWORK_MINUTES = 7
    LEGAL_HOLIDAY_OVERWORK_DAYS = 8
    LEGAL_HOLIDAY_OVERWORK_MINUTES = 9
    LATE_NIGHT_OVERWORK_MINUTES = 10
    BREAK_MINUTES = 11
    PAID_HOLIDAY_DAYS = 12
    PAID_HOLIDAY_HOURS = 13
    CHILD_TIME_LEAVE_DAYS = 14
    CHILD_TIME_LEAVE_HOURS = 15
    COMPENSATORY_HOLIDAY_DAYS = 16
    LEAVE_DAYS = 17
    CLOSED_DAYS = 18
    SPECIAL_PROVISIONS_YEAR_COUNT = 19
    UNIT_PRICE = 20

    @property
    def label(self) -> str:
        return {
            ErrorItem.REAL_TOTAL_MINUTES: "労働時間",
            ErrorItem.JOB_TOTAL_MINUTES: "所定労働時間",
            ErrorItem.JOB_OVERWORK_MINUTES: "所定外労働時間",
            ErrorItem.JOB_HOLIDAY_DAYS: "所定休日労働日数",
            ErrorItem.JOB_HOLIDAY_HOURS: "所定休日労働時間",
            ErrorItem.LEGAL_JOB_MINUTES: "法定労働時間",
            ErrorItem.LEGAL_OVERWORK_MINUTES: "法定外労働時間",
            ErrorItem.LEGAL_HOLIDAY_OVERWORK_DAYS: "法定休日労働日数",
            ErrorItem.LEGAL_HOLIDAY_OVERWORK_MINUTES: "法定休日労働時間",
            ErrorItem.LATE_NIGHT_OVERWORK_MINUTES: "深夜労働時間",
            ErrorItem.BREAK_MINUTES: "休憩時間",
            ErrorItem.PAID_HOLIDAY_DAYS: "有給日数",
            ErrorItem.PAID_HOLIDAY_HOURS: "有給時間数",
            ErrorItem.CHILD_TIME_LEAVE_DAYS: "育児休暇日数",
            ErrorItem.CHILD_TIME_LEAVE_HOURS: "育児時間休暇数",
            ErrorItem.COMPENSATORY_HOLIDAY_DAYS: "代休日数",
            ErrorItem.LEAVE_DAYS: "休職日数",
            ErrorItem.CLOSED_DAYS: "休業日数",
            ErrorItem.SPECIAL_PROVISIONS_YEAR_COUNT: "特別条項の摘要回数",
            ErrorItem.UNIT_PRICE: "時給",
        }[self]


"""
Enum:打刻区分
JOB_START            出勤打刻
JOB_FINISH            退勤打刻
BREAKTIME_START        休憩開始打刻
BREAKTIME_FINISH    休憩終了打刻
"""


class StampingType(IntEnum):
    JOB_START = 1
    JOB_FINISH = 2
    BREAKTIME_START = 3
    BREAKTIME_FINISH = 4

    @property
    def label(self) -> str:
        return {
            StampingType.JOB_START: "出勤打刻",
            StampingType.JOB_FINISH: "退勤打刻",
            StampingType.BREAKTIME_START: "休憩開始打刻",
            StampingType.BREAKTIME_FINISH: "休憩終了打刻",
        }[self]


"""
Enum:打刻方法
CORPUS コーパスからの移行
SMART_PHONE スマホ打刻
PC パソコン打刻
FELICA フェリカ打刻
QRCODE QRバーコード打刻
TABLET タブレット打刻
VEIN_AUTHENTICATION 静脈認証打刻
FINGERPRINT_AUTHENTICATION 指紋認証打刻
FACE_AUTHENTICATION 顔認証打刻
IMPRINT_CORRECTION 打刻補正
KRONOS 自動登録
ALEXA Alexa打刻
INPUT_ATTENDANCE_RECORD 出勤簿手入力
"""


class EntryFlg(IntEnum):
    CORPUS = 1
    SMART_PHONE = 2
    PC = 3
    FELICA = 4
    QRCODE = 5
    TABLET = 6
    VEIN_AUTHENTICATION = 7
    FINGERPRINT_AUTHENTICATION = 8
    FACE_AUTHENTICATION = 9
    IMPRINT_CORRECTION = 10
    KRONOS = 11
    ALEXA = 12
    INPUT_ATTENDANCE_RECORD = 13

    @property
    def label(self) -> str:
        return {
            EntryFlg.CORPUS: "コーパスからの移行",
            EntryFlg.SMART_PHONE: "スマホ打刻",
            EntryFlg.PC: "パソコン打刻",
            EntryFlg.FELICA: "フェリカ打刻",
            EntryFlg.QRCODE: "QRバーコード打刻",
            EntryFlg.TABLET: "タブレット打刻",
            EntryFlg.VEIN_AUTHENTICATION: "静脈認証打刻",
            EntryFlg.FINGERPRINT_AUTHENTICATION: "指紋認証打刻",
            EntryFlg.FACE_AUTHENTICATION: "顔認証打刻",
            EntryFlg.IMPRINT_CORRECTION: "打刻補正",
            EntryFlg.KRONOS: "自動登録",
            EntryFlg.ALEXA: "Alexa打刻",
            EntryFlg.INPUT_ATTENDANCE_RECORD: "出勤簿手入力",
        }[self]


"""
Enum:敬称
TYPE1 様
TYPE2 御中
"""


class Honorific(IntEnum):
    TYPE1 = 1
    TYPE2 = 2

    @property
    def label(self) -> str:
        return {
            Honorific.TYPE1: "様",
            Honorific.TYPE2: "御中",
        }[self]


"""
Enum:品名単位
TYPE1 個
TYPE2 リットル
TYPE3 人月
TYPE9 任意
"""


class ProductItemUnit(IntEnum):
    TYPE1 = 1
    TYPE2 = 2
    TYPE3 = 3
    TYPE9 = 9

    @property
    def label(self) -> str:
        return {
            ProductItemUnit.TYPE1: "個",
            ProductItemUnit.TYPE2: "リットル",
            ProductItemUnit.TYPE3: "人月",
            ProductItemUnit.TYPE9: "任意",
        }[self]


"""
Enum:入金日単位
TYPE1 当月
TYPE2 翌月
TYPE3 翌々月
TYPE4 6カ月後
TYPE9 都度
"""


class PaymentDateUnit(IntEnum):
    TYPE1 = 1
    TYPE2 = 2
    TYPE3 = 3
    TYPE4 = 4
    TYPE9 = 9

    @property
    def label(self) -> str:
        return {
            PaymentDateUnit.TYPE1: "当月",
            PaymentDateUnit.TYPE2: "翌月",
            PaymentDateUnit.TYPE3: "翌々月",
            PaymentDateUnit.TYPE4: "6カ月後",
            PaymentDateUnit.TYPE9: "都度",
        }[self]


"""
Enum:明細毎の端数処理
TRUNCATION 切り捨て
ROUND_UP 切り上げ
ROUNDING 四捨五入
"""


class RoundingOffForEachLineItem(IntEnum):
    TRUNCATION = 1
    ROUND_UP = 2
    ROUNDING = 3

    @property
    def label(self) -> str:
        return {
            RoundingOffForEachLineItem.TRUNCATION: "切り捨て",
            RoundingOffForEachLineItem.ROUND_UP: "切り上げ",
            RoundingOffForEachLineItem.ROUNDING: "四捨五入",
        }[self]


"""
Enum:消費税の端数処理
TRUNCATION 切り捨て
ROUND_UP 切り上げ
ROUNDING 四捨五入
"""


class RoundingOfConsumptionTax(IntEnum):
    TRUNCATION = 1
    ROUND_UP = 2
    ROUNDING = 3

    @property
    def label(self) -> str:
        return {
            RoundingOfConsumptionTax.TRUNCATION: "切り捨て",
            RoundingOfConsumptionTax.ROUND_UP: "切り上げ",
            RoundingOfConsumptionTax.ROUNDING: "四捨五入",
        }[self]


"""
Enum:消費税[内税/外税]
INCLUSIVE 内税
EXCLUSIVE 外税
"""


class TaxInclusiveExclusive(IntEnum):
    INCLUSIVE = 1
    EXCLUSIVE = 2

    @property
    def label(self) -> str:
        return {
            TaxInclusiveExclusive.INCLUSIVE: "内税",
            TaxInclusiveExclusive.EXCLUSIVE: "外税",
        }[self]


"""
Enum:帳票ステータス
MAKING 作成中
MAKED 作成完了
ERR 作成エラー
"""


class ReportStatus(IntEnum):
    MAKING = 1
    MAKED = 2
    ERR = 9

    @property
    def label(self) -> str:
        return {
            ReportStatus.MAKING: "作成中",
            ReportStatus.MAKED: "作成完了",
            ReportStatus.ERR: "作成エラー",
        }[self]


"""
Enum:メール送信ステータス
NONE 未送信
SEND 送信済
ERR 送信エラー
"""


class SendMailStatus(IntEnum):
    NONE = 1
    SEND = 2
    ERR = 9

    @property
    def label(self) -> str:
        return {
            SendMailStatus.NONE: "未送信",
            SendMailStatus.SEND: "送信済",
            SendMailStatus.ERR: "送信エラー",
        }[self]


"""
Enum:従業員申請管理区分
MANAGED 管理する
NON_MANAGED 管理しない
COMPANY_FOLLOW 会社申請管理区分に従う
GROUP_FOLLOW 部署申請管理区分に従う
OFFICE_FOLLOW 事業所申請管理区分に従う
"""


class EmployeeApplicationControl(IntEnum):
    MANAGED = 1
    NON_MANAGED = 2
    COMPANY_FOLLOW = 3
    GROUP_FOLLOW = 4
    OFFICE_FOLLOW = 5

    @property
    def label(self) -> str:
        return {
            EmployeeApplicationControl.MANAGED: "管理する",
            EmployeeApplicationControl.NON_MANAGED: "管理しない",
            EmployeeApplicationControl.COMPANY_FOLLOW: "会社申請管理区分に従う",
            EmployeeApplicationControl.GROUP_FOLLOW: "部署申請管理区分に従う",
            EmployeeApplicationControl.OFFICE_FOLLOW: "事業所申請管理区分に従う",
        }[self]


"""
Enum:部署申請管理区分
MANAGED 管理する
NON_MANAGED 管理しない
COMPANY_FOLLOW 会社申請管理区分に従う
GROUP_FOLLOW 上位部署の部署申請管理区分に従う
"""


class GroupApplicationControl(IntEnum):
    MANAGED = 1
    NON_MANAGED = 2
    COMPANY_FOLLOW = 3
    GROUP_FOLLOW = 4

    @property
    def label(self) -> str:
        return {
            GroupApplicationControl.MANAGED: "管理する",
            GroupApplicationControl.NON_MANAGED: "管理しない",
            GroupApplicationControl.COMPANY_FOLLOW: "会社申請管理区分に従う",
            GroupApplicationControl.GROUP_FOLLOW: "上位部署の部署申請管理区分に従う",
        }[self]


"""
Enum:事業所申請管理区分
MANAGED 管理する
NON_MANAGED 管理しない
COMPANY_FOLLOW 会社申請管理区分に従う
"""


class OfficeApplicationControl(IntEnum):
    MANAGED = 1
    NON_MANAGED = 2
    COMPANY_FOLLOW = 3

    @property
    def label(self) -> str:
        return {
            OfficeApplicationControl.MANAGED: "管理する",
            OfficeApplicationControl.NON_MANAGED: "管理しない",
            OfficeApplicationControl.COMPANY_FOLLOW: "会社申請管理区分に従う",
        }[self]


"""
Enum:会社申請管理区分
MANAGED 管理する
NON_MANAGED 管理しない
"""


class CompanyApplicationControl(IntEnum):
    MANAGED = 1
    NON_MANAGED = 2

    @property
    def label(self) -> str:
        return {
            CompanyApplicationControl.MANAGED: "管理する",
            CompanyApplicationControl.NON_MANAGED: "管理しない",
        }[self]


"""
Enum:申請書ステータス
CANCEL 取り下げ
DRAFT 下書き
PULL_BACK 引き戻し
WITH_DRAWAL 差し戻し
UNDER_EXAMINATION 審査中
DENIAL 否認
APPROVED 承認
"""


class ApplicationStatus(IntEnum):
    CANCEL = 1
    DRAFT = 2
    PULL_BACK = 3
    WITH_DRAWAL = 4
    UNDER_EXAMINATION = 5
    DENIAL = 6
    APPROVED = 7

    @property
    def label(self) -> str:
        return {
            ApplicationStatus.CANCEL: "取り下げ",
            ApplicationStatus.DRAFT: "下書き",
            ApplicationStatus.PULL_BACK: "引き戻し",
            ApplicationStatus.WITH_DRAWAL: "差し戻し",
            ApplicationStatus.UNDER_EXAMINATION: "審査中",
            ApplicationStatus.DENIAL: "否認",
            ApplicationStatus.APPROVED: "承認",
        }[self]


"""
Enum:税額区分
A 甲
B 乙
C 丙
"""


class TaxAmountClassification(IntEnum):
    A = 1
    B = 2
    C = 3

    @property
    def label(self) -> str:
        return {
            TaxAmountClassification.A: "甲",
            TaxAmountClassification.B: "乙",
            TaxAmountClassification.C: "丙",
        }[self]


"""
Enum:育児休業中の保険料免除
ON 免除中
OFF 対象外
"""


class PremiumExemptionDuringChildcareLeave(IntEnum):
    ON = 1
    OFF = 2

    @property
    def label(self) -> str:
        return {
            PremiumExemptionDuringChildcareLeave.ON: "免除中",
            PremiumExemptionDuringChildcareLeave.OFF: "対象外",
        }[self]


"""
Enum:昇給降給区分
UP 昇給
DOWN 降給
"""


class SalaryChange(IntEnum):
    UP = 1
    DOWN = 2

    @property
    def label(self) -> str:
        return {
            SalaryChange.UP: "昇給",
            SalaryChange.DOWN: "降給",
        }[self]


"""
Enum:給料変更理由
    A 70歳以上被用者月額変更
    B 二以上勤務
    C 短時間労働者(特定適用事業所等)
    D 昇給・降給の理由
    E 健康保険のみ月額変更(70歳到達時の契約変更等)
    F その他
"""


class ChangeReason(IntEnum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6

    @property
    def label(self) -> str:
        return {
            ChangeReason.A: "70歳以上被用者月額変更",
            ChangeReason.B: "二以上勤務",
            ChangeReason.C: "短時間労働者(特定適用事業所等)",
            ChangeReason.D: "昇給・降給の理由",
            ChangeReason.E: "健康保険のみ月額変更(70歳到達時の契約変更等)",
            ChangeReason.F: "その他",
        }[self]


"""
Enum:給料決定理由
    A 70歳以上被用者算定
    B 二以上勤務
    C 月額変更予定
    D 途中入社
    E 病休・育休・休職等
    F 短時間労働者（特定適用事業所等）
    G パート
    H 年間平均
    I その他
"""


class DecisionReason(IntEnum):
    TYPE_A = 1
    TYPE_B = 2
    TYPE_C = 3
    TYPE_D = 4
    TYPE_E = 5
    TYPE_F = 6
    TYPE_G = 7
    TYPE_H = 8
    TYPE_I = 9

    @property
    def label(self) -> str:
        return {
            DecisionReason.TYPE_A: "70歳以上被用者算定",
            DecisionReason.TYPE_B: "二以上勤務",
            DecisionReason.TYPE_C: "月額変更予定",
            DecisionReason.TYPE_D: "途中入社",
            DecisionReason.TYPE_E: "病休・育休・休職等",
            DecisionReason.TYPE_F: "短時間労働者（特定適用事業所等）",
            DecisionReason.TYPE_G: "パート",
            DecisionReason.TYPE_H: "年間平均",
            DecisionReason.TYPE_I: "その他",
        }[self]


"""
Enum:従業員区分タイプ
    A 一般
    B 短時間労働者
    C パート
"""


class EmployeeClassificationType(IntEnum):
    TYPE_A = 1
    TYPE_B = 2
    TYPE_C = 3


"""
Enum:アラート通知区分
NOTICE 通知
WARNING 警告
VIOLATION 違反
"""


class AlertJunlManagementControl(IntEnum):
    NOTICE = 1
    WARNING = 2
    VIOLATION = 3


"""
Enum:アラート通知方法
MAIL メール
ARTEMIS アルテミスのトップページ
ALL 全て
"""


class AlertNotificationMethod(IntEnum):
    MAIL = 1
    ARTEMIS = 2
    ALL = 9


"""
Enum:アラート管理区分
MANAGED 管理する
NON_MANAGED 管理しない
"""


class AlertManagementControl(IntEnum):
    MANAGED = 1
    NON_MANAGED = 2


"""
Enum:申請書グループ
AUTHORIZER_UNTREATED 未処理
UNDER_EXAMINATION 審査中
APPROVED 承認済
CONFIRM 確定
"""


class ApplicationGroup(IntEnum):
    AUTHORIZER_UNTREATED = 1
    UNDER_EXAMINATION = 2
    APPROVED = 3
    CONFIRM = 4


"""
Enum:申請者ステータス
CANCEL 取り下げ
PULL_BACK 引き戻し
APPLY 申請
"""


class ApplicantStatus(IntEnum):
    CANCEL = 1
    PULL_BACK = 3
    APPLY = 4


"""
Enum:承認者ステータス
AUTHORIZER_UNTREATED 未処理
ARRIVAL 到着
HOLD 保留
AUTHORIZER_CONFIRMATION 確認
AUTHORIZER_DENIAL 否認
AUTHORIZER_APPROVAL 承認
AUTHORIZER_ANTICIPATING_APPROVAL 先取り承認
AUTHORIZER_HIKE_APPROVAL 引上げ承認
AUTHORIZER_AUTOMATIC_APPROVAL 自動承認
AUTHORIZER_FORCED_APPROVAL 強制承認
SKIP 審査不要
WITH_DRAWAL 差し戻し
PULL_BACK 引き戻し
"""


class ActivityStatus(IntEnum):
    AUTHORIZER_UNTREATED = 1
    ARRIVAL = 2
    HOLD = 3
    AUTHORIZER_CONFIRMATION = 4
    AUTHORIZER_DENIAL = 5
    AUTHORIZER_APPROVAL = 6
    AUTHORIZER_ANTICIPATING_APPROVAL = 7
    AUTHORIZER_HIKE_APPROVAL = 8
    AUTHORIZER_AUTOMATIC_APPROVAL = 9
    AUTHORIZER_FORCED_APPROVAL = 10
    SKIP = 11
    WITH_DRAWAL = 12
    PULL_BACK = 13


"""
Enum:表示用承認者ステータス
NO_ARRIVED 未着
APPROVAL_PENDING 承認待ち
PENDING_VERIFICATION 確認待ち
AUTHORIZER_DENIAL 否認済
AUTHORIZER_APPROVAL 承認済
CONFIRMED 確認済
"""


class ActivityStatus4display(IntEnum):
    NO_ARRIVED = 1
    APPROVAL_PENDING = 2
    PENDING_VERIFICATION = 3
    AUTHORIZER_DENIAL = 4
    AUTHORIZER_APPROVAL = 5
    CONFIRMED = 6


"""
Enum:取り下げ区分
POSSIBLE_BEFORE_APPROVAL 承認前なら可能
POSSIBLE_AFTER_APPROVAL 承認後も可能
"""


class WithdrawalFlag(IntEnum):
    POSSIBLE_BEFORE_APPROVAL = 1
    POSSIBLE_AFTER_APPROVAL = 2


"""
Enum:引き戻し区分
NO_PULLING 引き戻し禁止
POSSIBLE_BEFORE_APPROVAL 承認前なら可能
POSSIBLE_AFTER_APPROVAL 承認後も可能
"""


class PullingFlag(IntEnum):
    NO_PULLING = 1
    POSSIBLE_BEFORE_APPROVAL = 2
    POSSIBLE_AFTER_APPROVAL = 3


"""
Enum:コネクター
UNSPECIFIED 未定義
LOGICAL_SUM 論理和
LOGICAL_PRODUCT 論理積
EXCLUSIVE_OR 排他的論理和
MAJORITY 多数
REPEAT 繰り返し
"""


class Connector(IntEnum):
    UNSPECIFIED = 1
    LOGICAL_SUM = 2
    LOGICAL_PRODUCT = 3
    EXCLUSIVE_OR = 4
    MAJORITY = 5
    REPEAT = 6


"""
Enum:比較演算子
UNSPECIFIED 未定義
THE_FOLLOWING 以下
SMALLER より小さい
SAME 等しい
OR_MORE 以上
LARGER_THAN より大きい
UNEQUAL 等しくない
"""


class ComparisonOperator(IntEnum):
    UNSPECIFIED = 1
    THE_FOLLOWING = 2
    SMALLER = 3
    SAME = 4
    OR_MORE = 5
    LARGER_THAN = 6
    UNEQUAL = 7


"""
Enum:承認画面の機能
EXAMINATION 審査
AUTHORIZER_AUTOMATIC_APPROVAL 自動承認
FUNCTION_CONFIRMATION 確認
AUTHORIZER_FORCED_APPROVAL 強制承認
"""


class ApprovalFunction(IntEnum):
    EXAMINATION = 1
    AUTHORIZER_AUTOMATIC_APPROVAL = 2
    FUNCTION_CONFIRMATION = 3
    AUTHORIZER_FORCED_APPROVAL = 4


"""
Enum:自動承認フラグ
AUTOMATIC_APPROVAL 自動承認
MANUAL_APPROVAL 手動承認
"""


class AutoApproverlFlag(IntEnum):
    AUTOMATIC_APPROVAL = 1
    MANUAL_APPROVAL = 2


"""
Enum:個別ルートフラグ
NO_INDIVIDUAL_ROUTE 直接部門なし
INDIVIDUAL_ROUTE 直接部門有り
BOSS_ROUTE 上司ルート
"""


class RouteFlag(IntEnum):
    NO_INDIVIDUAL_ROUTE = 1
    INDIVIDUAL_ROUTE = 2
    BOSS_ROUTE = 3


"""
Enum:ルートタイプ
INDIVIDUAL_ROUTE 個別ルート
COMMON_ROUTE 共通ルート
"""


class RouteType(IntEnum):
    INDIVIDUAL_ROUTE = 1
    COMMON_ROUTE = 2


"""
Enum:画面モード
画面を開く際、どのモードで開くのかをVueに伝えるための区分です。
APPLY_MODE_1 申請モード1　[下書き/申請]
APPLY_MODE_2 申請モード2　[取り下げ/下書き/申請]
APPLY_MODE_3 申請モード3　[取り下げ/申請]
APPROVAL_MODE_1 承認モード1　[差し戻し/保留/否認/承認]
APPROVAL_MODE_3 承認モード3　[先取り承認/引き上げ承認]
APPROVAL_MODE_4 承認モード4　[強制承認]
CONFIRMATION_MODE 確認モード [確認]
SEE_MODE_1参照モード1　[ボタンなし]
SEE_MODE_2 参照モード2　[再申請]
SEE_MODE_3 参照モード3　[引き戻し][再申請]
SEE_MODE_4 参照モード4　[取り下げ][再申請]
SEE_MODE_5 参照モード5　[引き戻し][取り下げ]
SEE_MODE_6 参照モード6　[引き戻し][取り下げ][再申請]
SEE_MODE_7 参照モード7　[取り下げ]
SEE_MODE_8 参照モード8　[引き戻し]
"""


class ScreenMode(IntEnum):
    APPLY_MODE_1 = 1
    APPLY_MODE_2 = 2
    APPLY_MODE_3 = 3
    APPROVAL_MODE_1 = 4
    APPROVAL_MODE_3 = 5
    APPROVAL_MODE_4 = 15
    CONFIRMATION_MODE = 6
    SEE_MODE_1 = 7
    SEE_MODE_2 = 8
    SEE_MODE_3 = 9
    SEE_MODE_4 = 10
    SEE_MODE_5 = 11
    SEE_MODE_6 = 12
    SEE_MODE_7 = 13
    SEE_MODE_8 = 14


"""
Enum:次のパーティコードの代替値
START 開始
END 終了
"""


class SpecifiedValue(IntEnum):
    START = 1
    END = 2


"""
Enum:雇用保険
SUBSCRIPTION　加入
NON_SUBSCRIPTION　未加入
"""


class EmploymentInsurance(IntEnum):
    SUBSCRIPTION = 1
    NON_SUBSCRIPTION = 2


"""
Enum:アップロードステータス
UPLOADING アップロード中
UPLOADED アップロード完了
ERR 作成エラー
"""


class UploadStatus(IntEnum):
    UPLOADING = 1
    UPLOADED = 2
    ERR = 9


"""
Enum:厚生年金基金
SUBSCRIPTION　加入
NON_SUBSCRIPTION　未加入
"""


class PensionFundContributions(IntEnum):
    SUBSCRIPTION = 1
    NON_SUBSCRIPTION = 2


"""
Enum:労働管理
MANAGE　管理する
NON_MANAGE　管理しない
"""


class AttendanceManagement(IntEnum):
    MANAGE = 1
    NON_MANAGE = 2


"""
Enum:賃金管理
MANAGE　管理する
NON_MANAGE　管理しない
"""


class PayrollManagement(IntEnum):
    MANAGE = 1
    NON_MANAGE = 2


"""
Enum:会社名の公開
RELEASE　公開
PRIVATE　非公開
"""


class DisclosureOfCompany(IntEnum):
    RELEASE = 1
    PRIVATE = 2


"""
Enum:労働秒の丸め
TRUNCATION 労働秒を切り捨て
ROUND_UP 労働秒を切り上げ
"""


class RoundingSecond(IntEnum):
    TRUNCATION = 1
    ROUND_UP = 2


"""
Enum:労働時間の丸め
NON_ROUNDING 丸め処理をしない
MONTHLY 月単位
DAILY 日単位
"""


class RoundingType(IntEnum):
    NON_ROUNDING = 1
    MONTHLY = 2
    DAILY = 3


"""
Enum:勤務時間を月単位で丸め
TRUNCATION 30分未満は切り捨て
ROUND_UP 30分未満は切り上げ
"""


class RoundingMonth(IntEnum):
    TRUNCATION = 1
    ROUND_UP = 2


"""
Enum:丸め処理(日単位)　出勤時間の丸め
TRUNCATION 労働時間を切り捨て
ROUND_UP 労働時間を切り上げ
"""


class RoundingJobStart(IntEnum):
    TRUNCATION = 1
    ROUND_UP = 2


"""
Enum:丸め処理(日単位)　退勤時間の丸め
TRUNCATION 労働時間を切り捨て
ROUND_UP 労働時間を切り上げ
"""


class RoundingJobEnd(IntEnum):
    TRUNCATION = 1
    ROUND_UP = 2


"""
Enum:始業時間前の労働時間を含む
TARGET 対象
NON_TARGET 非対象
"""


class JobBeforeStartTime(IntEnum):
    TARGET = 1
    NON_TARGET = 2


"""
Enum:完全週休二日制におけるフレックスタイムの適用有無
TARGET 対象
OUT_OF_SCOPE 対象外
"""


class FlextimeFullTwoDayWeekendSystem(IntEnum):
    TARGET = 1
    OUT_OF_SCOPE = 2


class Availability(IntEnum):
    AVAILABLE = 1
    UNUSABLE = 2


"""
Enum:仮登録フラグ
1仮登録中
9 本登録済
"""


class PendingFlg(IntEnum):
    PENDING = 1
    REGISTRATION = 9


"""
Enum:利用権限範囲
PERSONAL 個人
ALL 全員
"""


class Range(IntEnum):
    PERSONAL = 1
    ALL = 2


"""
Enum:権限の譲渡フラグ
AVAILABLE 可能です
UNUSABLE 出来ません
"""


class Permission(IntEnum):
    AVAILABLE = 1
    UNUSABLE = 2


"""
Enum:処理フラグ
PROCESSED 処理済
UNTREATED 未処理
"""


class IsProcessed(IntEnum):
    PROCESSED = 1
    UNTREATED = 2


"""
Enum:契約期間のルール
UN_LIMITED 期間の定め無し
LIMITED 期間の定めあり
"""


class ContractPeriodRule(IntEnum):
    UN_LIMITED = 1
    LIMITED = 2


"""
Enum:本人の安否
NO_PROBLEM 無事
MINOR_INJURY 軽傷
SERIOUS_INJURY 重傷
NO_CONTACT 連絡とれず
"""


class SafetyOfThePerson(IntEnum):
    NO_PROBLEM = 1
    MINOR_INJURY = 2
    SERIOUS_INJURY = 3
    NO_CONTACT = 9


"""
Enum:出勤可否
AVAILABLE_FOR_WORK 出勤可能
UNABLE_TO_GO_TO_WORK 出勤不可能
UNABLE_TO_GO_TO_WORK_FAMILY_INJURED 出勤不可能[家族が怪我]
BEFIND_TIME_ONE_HOUR 遅刻[一時間以内]
BEFIND_TIME_ONE_HOUR_IN_THE_MORNING 遅刻[午前]
BEFIND_TIME_ONE_HOUR_IN_THEAFTERNOON 遅刻[午後]
"""


class ComingToWork(IntEnum):
    AVAILABLE_FOR_WORK = 1
    UNABLE_TO_GO_TO_WORK = 2
    UNABLE_TO_GO_TO_WORK_FAMILY_INJURED = 3
    BEFIND_TIME_ONE_HOUR = 4
    BEFIND_TIME_ONE_HOUR_IN_THE_MORNING = 5
    BEFIND_TIME_ONE_HOUR_IN_THEAFTERNOON = 6


"""
Enum:有給休暇の繰り越し可否
UNUSABLE 不可
AVAILABLE 可能
"""


class RollOver(IntEnum):
    UNUSABLE = 1
    AVAILABLE = 2


"""
Enum:有給休暇の消化順序
OLD 古い方から利用
NEW 新しい方から利用
"""


class DigestionOrder(IntEnum):
    OLD = 1
    NEW = 2


"""
Enum:出勤率の端数処理方法
TRUNCATION 切り捨て
ROUND_UP 切り上げ
ROUNDING 四捨五入
"""


class FractionOfAttendanceRate(IntEnum):
    TRUNCATION = 1
    ROUND_UP = 2
    ROUNDING = 3


"""
Enum:計画的付与の扱い
NONE 行わない
SPECIAL_PAID 特別休暇
LEAVE_ALLOWANCE 休業手当
"""


class HandlingPlannedGrants(IntEnum):
    NONE = 1
    SPECIAL_PAID = 2
    LEAVE_ALLOWANCE = 3


"""
Enum:有給休暇
ON 　有給休暇あり
OFF　有給休暇なし
"""


class PaidLeavePayment(IntEnum):
    ON = 1
    OFF = 2


"""
Enum:色パターン
ORIGINAL オリジナル
A 基本A
B 基本B
ARTEMIS-CODIE Artemisカラー
"""


class ColorPattern(IntEnum):
    ORIGINAL = 1
    A = 2
    B = 3
    ARTEMIS = 9


"""
Enum:種類
REGULAR_HOLIDAY 通常年休
HOURLY_ANNUAL_HOLIDAY 時間単位年休
PLANNED_HOLIDAY 計画年休
HALF_REGULAR_HOLIDAY 半休
CHILD_TIME_LEAVE 育児休暇
ALTERNATIVE_HOLIDAY 代替休暇
"""


class PaidHolidayType(IntEnum):
    REGULAR_HOLIDAY = 1
    HOURLY_ANNUAL_HOLIDAY = 2
    PLANNED_HOLIDAY = 3
    HALF_REGULAR_HOLIDAY = 4
    CHILD_TIME_LEAVE = 5
    ALTERNATIVE_HOLIDAY = 6


"""
Enum:変形時間労働制のタイプ
WEEKLY 週単位
MONTHLY 月単位
YEAR 年単位
HALF_REGULAR_HOLIDAY 半休
"""


class FlexibleLaborType(IntEnum):
    WEEKLY = 1
    MONTHLY = 2
    YEAR = 3


"""
Enum:種類
CHILD_TIME_LEAVE 育児休暇
HOURLY_CHILD_TIME_LEAVE 育児時間休暇
"""


class ParentalLeaveType(IntEnum):
    CHILD_TIME_LEAVE = 1
    HOURLY_CHILD_TIME_LEAVE = 2


"""
Enum:有給休暇　理由コード
ANNUAL_GRANT  年次付与
PRESCRIPTION  時効
INSUFFICIENT_ATTENDANCE_RATE 出勤率不足
EXPIRATION_DUE_TO_PRESCRIPTION 時効による失効
SCREEN_ADD 有給管理画面より付与
SCREEN_DEL 有給管理画面より失効
RESIGN 退職による失効
"""


class PaidLeaveReason(IntEnum):
    ANNUAL_GRANT = 1
    PRESCRIPTION = 2
    INSUFFICIENT_ATTENDANCE_RATE = 3
    EXPIRATION_DUE_TO_PRESCRIPTION = 4
    SCREEN_ADD = 5
    SCREEN_DEL = 6
    RESIGN = 7


"""
Enum:有給休暇付与ルール
INDIVIDUAL 入社日毎に支給する
ALL_AT_ONCE 統一支給日に支給する
"""


class PaidLeaveGranted(IntEnum):
    INDIVIDUAL = 1
    ALL_AT_ONCE = 2


"""
Enum:統一支給方式
ONCE_PROVIDED 入社日に支給
MOST_RECENTLY_PAID 入社日から最初に訪れる統一支給日に支給
MIX 入社日毎に支給し、その後は統一支給日に支給
"""


class PaidLeavePaymentMethod(IntEnum):
    ONCE_PROVIDED = 1
    MOST_RECENTLY_PAID = 2
    MIX = 3


"""
Enum:代替休暇利用フラグ
AVAILABLE 使用
UNAVAILABLE 未使用
"""


class AlternativeLeaveFlag(IntEnum):
    AVAILABLE = 1
    UNAVAILABLE = 2


"""
Enum:所定労働日区分
ON 　所定労働日扱い
OFF　所定労働日扱いしない
"""


class LaborDayClassification(IntEnum):
    ON = 1
    OFF = 2


"""
Enum:出勤日扱い区分
ON 　出勤日扱いする
OFF　出勤日扱いしない
"""


class AttendanceDateClassification(IntEnum):
    ON = 1
    OFF = 2


"""
Enum:賃金支給区分
ON 　賃金支給する
OFF　賃金支給しない
"""


class WageClassification(IntEnum):
    ON = 1
    OFF = 2


"""
Enum:通知間隔単位
MINUTES 分
HOUR 時間
DAY 日
"""


class AlertTermUnit(IntEnum):
    MINUTES = 1
    HOUR = 2
    DAY = 3


"""
Enum:CSV出力項目単位
MINUTES 分
HOUR 時間
DAY 日
COUNT 回
PRICE 円
RATE %
DATE 月日
"""


class WorkItemUnit(IntEnum):
    MINUTES = 1
    HOUR = 2
    DAY = 3
    COUNT = 4
    PRICE = 5
    RATE = 6
    DATE = 7
    MINUTES_1 = 8
    MINUTES_2 = 9
    MINUTES_3 = 10
    MINUTES_4 = 11
    HOUR_1 = 12
    HOUR_2 = 13
    HOUR_3 = 14
    HOUR_4 = 15
    DAY_1 = 16
    COUNT_1 = 17
    PRICE_1 = 18
    RATE_1 = 19
    RATE_2 = 20
    RATE_3 = 21
    DATE_1 = 22
    DATE_2 = 23


"""
Enum:承認済
NON_APPROVAL  未承認
WAIT  審査中
NOT_APPLICABLE_TO_LAUBE  ワークフロー対象外
APPROVED  承認済
INVALID  無効
"""


class ApprovalFlg(IntEnum):
    NON_APPROVAL = 1
    WAIT = 2
    APPROVED = 3
    NOT_APPLICABLE_TO_LAUBE = 8
    INVALID = 9


"""
Enum:反映済
REFLECTED  反映済
NON_REFLECTED  未反映
"""


class ReflectedFlg(IntEnum):
    REFLECTED = 1
    NON_REFLECTED = 2


"""
Enum:希望シフトステータス
WANT  勤務を希望
NOT_WANT  勤務を希望しない
CANNOT 勤務不可
"""


class ShiftPreferenceStatus(IntEnum):
    WANT = 1
    NOT_WANT = 2
    CANNOT = 9

    @property
    def priority_level(self) -> int:
        return {
            ShiftPreferenceStatus.WANT: 3,
            ShiftPreferenceStatus.NOT_WANT: -1,
            ShiftPreferenceStatus.CANNOT: -100,
        }[self]


"""
Enum:シフト公開フラグ
PUBLIC 公開
PRIVATE 非公開
"""


class ShiftPublishFlg(IntEnum):
    PUBLIC = 1
    PRIVATE = 2


"""
Enum:色
BLACK 黒色
BLUE 青色
RED 赤色
GREEN 緑色
"""


class Color(IntEnum):
    BLACK = 1
    BLUE = 2
    RED = 3
    GREEN = 4


"""
Enum:事由マスタ　出勤簿利用可否
AVAILABLE 利用可能
UNAVAILABLE 利用不可
OUT 利用不可[変更不可]
"""


class TimecardAvailableFlg(IntEnum):
    AVAILABLE = 1
    UNAVAILABLE = 2
    OUT = 9


"""
Enum:打刻時間未使用フラグ
AVAILABLE 使用
UNAVAILABLE 未使用
"""


class NonStampFlg(IntEnum):
    AVAILABLE = 1
    UNAVAILABLE = 2

    @property
    def label(self) -> str:
        return {
            NonStampFlg.AVAILABLE: "使用",
            NonStampFlg.UNAVAILABLE: "未使用",
        }[self]


"""
Enum:受付可能区分
OPEN 受付中
CLOSE 受付終了
"""


class Acceptable(IntEnum):
    OPEN = 1
    CLOSED = 2

    @property
    def label(self) -> str:
        return {
            Acceptable.OPEN: "受付中",
            Acceptable.CLOSED: "受付終了",
        }[self]


"""
Enum:締め処理
OPEN 締め未
CLOSED 締め済
"""


class IsClose(IntEnum):
    OPEN = 1
    CLOSED = 2

    @property
    def label(self) -> str:
        return {
            IsClose.OPEN: "締め未",
            IsClose.CLOSED: "締め済",
        }[self]


"""
Enum:障害者区分
GENERAL_DISABLED_PERSON_EN 一般障害者
SPECIAL_DISABLED_PERSON_EN 特別障害者
"""


class DisabilityClassification(IntEnum):
    GENERAL_DISABLED_PERSON_EN = 1
    SPECIAL_DISABLED_PERSON_EN = 2

    @property
    def label(self) -> str:
        return {
            DisabilityClassification.GENERAL_DISABLED_PERSON_EN: "一般障害者",
            DisabilityClassification.SPECIAL_DISABLED_PERSON_EN: "特別障害者",
        }[self]


"""
Enum:同居区分
LIVING_TOGETHER 同居あり
WITHOUT_COHABITATION 同居なし
"""


class LivingTogether(IntEnum):
    LIVING_TOGETHER = 1
    WITHOUT_COHABITATION = 2

    @property
    def label(self) -> str:
        return {
            LivingTogether.LIVING_TOGETHER: "同居あり",
            LivingTogether.WITHOUT_COHABITATION: "同居なし",
        }[self]


"""
Enum:扶養親族区分
GENERAL 一般
YOUNG 年少
SPECIFIC 特定
OLD_MAN 老人
OLD_PARENTS 老親等
"""


class DependentRelativeClassification(IntEnum):
    GENERAL = 1
    YOUNG = 2
    SPECIFIC = 3
    OLD_MAN = 4
    OLD_PARENTS = 5

    @property
    def label(self) -> str:
        return {
            DependentRelativeClassification.GENERAL: "一般",
            DependentRelativeClassification.YOUNG: "年少",
            DependentRelativeClassification.SPECIFIC: "特定",
            DependentRelativeClassification.OLD_MAN: "老人",
            DependentRelativeClassification.OLD_PARENTS: "老親等",
        }[self]


"""
Enum:続柄
HUSBAND 夫
WIFE 妻
FATHER 父
MOTHER 母
CHILDREN 子供
SPOUSES_PARENTS 配偶者の父母
BROTHER 兄弟/姉妹
GRAND_CHILD 孫
GRAND_PARENTS 祖父母
SPOUSES_BROTHER 配偶者の兄弟
SPOUSES_PARENTS_PARENTS 配偶者の父母の親
"""


class Relationship(IntEnum):
    HUSBAND = 1
    WIFE = 2
    FATHER = 3
    MOTHER = 4
    CHILDREN = 5
    SPOUSES_PARENTS = 6
    BROTHER = 7
    GRAND_CHILD = 8
    GRAND_PARENTS = 9
    SPOUSES_BROTHER = 10
    SPOUSES_PARENTS_PARENTS = 11

    @property
    def label(self) -> str:
        return {
            Relationship.HUSBAND: "夫",
            Relationship.WIFE: "妻",
            Relationship.FATHER: "父",
            Relationship.MOTHER: "母",
            Relationship.CHILDREN: "子供",
            Relationship.SPOUSES_PARENTS: "配偶者の父母",
            Relationship.BROTHER: "兄弟/姉妹",
            Relationship.GRAND_CHILD: "孫",
            Relationship.GRAND_PARENTS: "祖父母",
            Relationship.SPOUSES_BROTHER: "配偶者の兄弟",
            Relationship.SPOUSES_PARENTS_PARENTS: "配偶者の父母の親",
        }[self]


"""
Enum:曜日
MONDAY 月曜日
TUESDAY 火曜日
WEDNESDAY 水曜日
THURSDAY 木曜日
FRIDAY 金曜日
SATURDAY 土曜日
SUNDAY 日曜日
"""


class DayOfTheWeek(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    @property
    def label(self) -> str:
        return {
            DayOfTheWeek.MONDAY: "月曜日",
            DayOfTheWeek.TUESDAY: "火曜日",
            DayOfTheWeek.WEDNESDAY: "水曜日",
            DayOfTheWeek.THURSDAY: "木曜日",
            DayOfTheWeek.FRIDAY: "金曜日",
            DayOfTheWeek.SATURDAY: "土曜日",
            DayOfTheWeek.SUNDAY: "日曜日",
        }[self]


"""
Enum:除算/乗算区分
DIVISION 除算
MULTIPLICATION 乗算
"""


class DivisionMultiplicationClassification(IntEnum):
    DIVISION = 1
    MULTIPLICATION = 2


"""
Enum:メーカー
PFDIZER ファイザー
MODERNA モデルナ
"""


class Maker(IntEnum):
    PFDIZER = 1
    MODERNA = 2


"""
Enum:ワクチン種類
COVID_19 COVID19
"""


class Vaccination(IntEnum):
    COVID_19 = 1


"""
Enum:基本給区分
BASIC_SALARY 基本給
ALLOWANCE 手当
OUT_OF_SCOPE 対象外
"""


class BasicSalary(IntEnum):
    BASIC_SALARY = 1
    ALLOWANCE = 2
    OUT_OF_SCOPE = 3


"""
Enum:日割り対象
ON 対象
OFF 対象外
"""


class DailyDivision(IntEnum):
    ON = 1
    OFF = 2


"""
Enum:在留資格
DIPLOMACY 外交
PUBLIC_USE 公用
PROFESSOR 教授
ART 芸術
RELIGION 宗教
REPORT 報道
HIGHLY_SKILLED 高度専門職
BUSINESS_ADMINISTRATION 経営・管理
LEGAL_ACCOUNTING_SERVICES 法律・会計業務
MEDICAL_CARE 医療
RESEARCH 研究
EDUCATION 教育
SPECIALIST 技術・人文知識・国際業務
INTRA_COMPANY_TRANSFER 企業内転勤
NURSING_CARE 介護
PERFORMANCE 興行
SKILL 技能
SPECIFIED_SKILL 特定技能
TECHNICAL_TRAINING 技術実習
PERMANENT_RESIDENT 永住者
JAPANESE_SPOUSE 日本人の配偶者等
PERMANENT_RESIDENT_SPOUSE 永住者の配偶者等
LONG_TERM_RESIDENT 定住者
SPECIFIC_ACTIVITY 特定活動
"""


class ResidentialStatus(IntEnum):
    DIPLOMACY = 1
    PUBLIC_USE = 2
    PROFESSOR = 3
    ART = 4
    RELIGION = 5
    REPORT = 6
    HIGHLY_SKILLED = 7
    BUSINESS_ADMINISTRATION = 8
    LEGAL_ACCOUNTING_SERVICES = 9
    MEDICAL_CARE = 10
    RESEARCH = 11
    EDUCATION = 12
    SPECIALIST = 13
    INTRA_COMPANY_TRANSFER = 14
    NURSING_CARE = 15
    PERFORMANCE = 16
    SKILL = 17
    SPECIFIED_SKILL = 18
    TECHNICAL_TRAINING = 19
    PERMANENT_RESIDENT = 20
    JAPANESE_SPOUSE = 21
    PERMANENT_RESIDENT_SPOUSE = 22
    LONG_TERM_RESIDENT = 23
    SPECIFIC_ACTIVITY = 24


"""
Enum:文字コード
SHIFT_JIS 1
UTF_8 2
CP932 3
UTF_16 4
UTF_32 5
"""


class Encode(IntEnum):
    SHIFT_JIS = 1
    UTF_8 = 2
    CP932 = 3
    UTF_16 = 4
    UTF_32 = 5
    UTF_8_SIG = 6

    @property
    def label(self) -> str:
        return {
            Encode.SHIFT_JIS: "SHIFT_JIS",
            Encode.UTF_8: "UTF-8",
            Encode.CP932: "CP932",
            Encode.UTF_16: "UTF-16",
            Encode.UTF_32: "UTF-32",
            Encode.UTF_8_SIG: "UTF-8 (BOM付き)",
        }[self]


"""
Enum:集計区分
労働月トランに項目が増えた場合、必ずここにも追加してください。
REAL_TOTAL_MINUTES 労働時間
JOB_TOTAL_DAYS 所定労働出勤日数
ABSENT_TOTAL_DAYS 欠勤日数+休業日数
JOB_TOTAL_MINUTES 所定労働時間
JOB_OVERWORK_MINUTES 所定外労働時間
JOB_HOLIDAY_DAYS 所定休日労働日数
JOB_HOLIDAY_HOURS 所定休日労働時間
LEGAL_JOB_MINUTES 法定労働時間
LEGAL_OVERWORK_MINUTES 法定外労働時間
LEGAL_HOLIDAY_OVERWORK_DAYS 法定休日労働日数
LEGAL_HOLIDAY_OVERWORK_MINUTES 法定休日労働時間
LATE_NIGHT_OVERWORK_MINUTES 深夜労働時間
BREAK_MINUTES 休憩時間
LATE_DAYS 遅刻回数
LATE_MINUTES 遅刻時間
EARLY_DEPARTURE_DAYS 早退回数
EARLY_DEPARTURE_MINUTES 早退時間
PAID_HOLIDAY_DAYS 有給日数
PAID_HOLIDAY_HOURS 有給時間数
COMPENSATORY_HOLIODAY_DAYS 代休日数
LEAVE_DAYS 休職日数
LEGAL_WITHIN_45_OVERWORK_MINUTES 45時間以内の法定外労働時間
LEGAL_45_OVERWORK_MINUTES 45時間を超過した法定外労働時間
LEGAL_60_OVERWORK_MINUTES 60時間を超過した法定外労働時間
LACK_MINUTES 集計期間の不足時間(給与控除が必要な時間)
ESTIMATED_OEVRTIME_HOURS 見込み残業時間
JOB_LEGAL_OVERWORK_MINUTES 所定外労働時間+法定外労働時間
LATE_EARLY_DEPARTURE_MINUTES 遅刻時間+早退時間
LATE_EARLY_DEPARTURE_DAYS 遅刻回数+早退回数
TELEWORK_COUNT テレワーク回数
CLOSED_DAYS 休業日数
STANDRAD_LEGAL_MINUTES 標準法定労働時間
STANDRAD_JOB_MINUTES 標準所定労働時間
STANDRAD_LEGAL_DAYS 標準法定労働日数
JOB_TOTAL_DAYS_WITH_OUT_TELEWORK 所定労働出勤日数(テレワーク日数を除く)
CHILD_TIME_LEAVE_DAYS 育児休暇日数
CHILD_TIME_LEAVE_HOURS 育児時間休暇数
LEGAL_60_OVERWORK_RATE 60時間を超える割増賃金率
ALTERNATIVE_LEAVE_RATE 代替休暇を取得した場合に支払う割増賃金率
BLACKOUT_DAYS 除外日数
#    WORKING_INTERVAL インターバル時間
#    FLEX_REAL_TOTAL_MINUTES フレックス集計労働時間
#    FLEX_LEGAL_HOLIDAY_OVERWORK_MINUTES フレックス集計法定休日労働時間
#    FLEX_STANDARD_LEGAL_MINUTES フレックス集計標準法定労働時間
#    FLEX_ESTIMATED_OVERWORK_MINUTES 集計期間の見込み残業時間
#   (システム計算枠)
AVERAGE_WORKING_HOURS_PER_MONTH 月の平均労働時間
AVERAGE_WORKING_DAYS_PER_MONTH 月の平均労働日数
UNIT_PRICE 単価
STANDARD_JOB_MINUTES_4_DAY 一日の所定労働時間
"""


class AggregationCategory(IntEnum):
    REAL_TOTAL_MINUTES = 1
    JOB_TOTAL_DAYS = 2
    ABSENT_TOTAL_DAYS = 3
    JOB_TOTAL_MINUTES = 4
    JOB_OVERWORK_MINUTES = 5
    JOB_HOLIDAY_DAYS = 6
    JOB_HOLIDAY_HOURS = 7
    LEGAL_JOB_MINUTES = 8
    LEGAL_OVERWORK_MINUTES = 9
    LEGAL_HOLIDAY_OVERWORK_DAYS = 10
    LEGAL_HOLIDAY_OVERWORK_MINUTES = 11
    LATE_NIGHT_OVERWORK_MINUTES = 12
    BREAK_MINUTES = 13
    LATE_DAYS = 14
    LATE_MINUTES = 15
    EARLY_DEPARTURE_DAYS = 16
    EARLY_DEPARTURE_MINUTES = 17
    PAID_HOLIDAY_DAYS = 18
    PAID_HOLIDAY_HOURS = 19
    COMPENSATORY_HOLIODAY_DAYS = 20
    LEAVE_DAYS = 21
    LEGAL_WITHIN_45_OVERWORK_MINUTES = 22
    LEGAL_45_OVERWORK_MINUTES = 23
    LEGAL_60_OVERWORK_MINUTES = 24
    LACK_MINUTES = 25
    ESTIMATED_OEVRTIME_HOURS = 26
    JOB_LEGAL_OVERWORK_MINUTES = 27
    LATE_EARLY_DEPARTURE_MINUTES = 28
    LATE_EARLY_DEPARTURE_DAYS = 29
    TELEWORK_COUNT = 30
    CLOSED_DAYS = 31
    STANDRAD_LEGAL_MINUTES = 32
    STANDRAD_LEGAL_DAYS = 33
    JOB_TOTAL_DAYS_WITH_OUT_TELEWORK = 34
    CHILD_TIME_LEAVE_DAYS = 38
    CHILD_TIME_LEAVE_HOURS = 35
    LEGAL_60_OVERWORK_RATE = 36
    ALTERNATIVE_LEAVE_RATE = 37
    STANDRAD_JOB_MINUTES = 38
    BLACKOUT_DAYS = 39
    AVERAGE_WORKING_HOURS_PER_MONTH = 90
    AVERAGE_WORKING_DAYS_PER_MONTH = 91
    UNIT_PRICE = 92
    STANDARD_JOB_MINUTES_4_DAY = 93

    @property
    def label(self) -> str:
        return {
            AggregationCategory.REAL_TOTAL_MINUTES: "労働時間",
            AggregationCategory.JOB_TOTAL_DAYS: "所定労働出勤日数",
            AggregationCategory.ABSENT_TOTAL_DAYS: "欠勤日数+休業日数",
            AggregationCategory.JOB_TOTAL_MINUTES: "所定労働時間",
            AggregationCategory.JOB_OVERWORK_MINUTES: "所定外労働時間",
            AggregationCategory.JOB_HOLIDAY_DAYS: "所定休日労働日数",
            AggregationCategory.JOB_HOLIDAY_HOURS: "所定休日労働時間",
            AggregationCategory.LEGAL_JOB_MINUTES: "法定労働時間",
            AggregationCategory.LEGAL_OVERWORK_MINUTES: "法定外労働時間",
            AggregationCategory.LEGAL_HOLIDAY_OVERWORK_DAYS: "法定休日労働日数",
            AggregationCategory.LEGAL_HOLIDAY_OVERWORK_MINUTES: "法定休日労働時間",
            AggregationCategory.LATE_NIGHT_OVERWORK_MINUTES: "深夜労働時間",
            AggregationCategory.BREAK_MINUTES: "休憩時間",
            AggregationCategory.LATE_DAYS: "遅刻回数",
            AggregationCategory.LATE_MINUTES: "遅刻時間",
            AggregationCategory.EARLY_DEPARTURE_DAYS: "早退回数",
            AggregationCategory.EARLY_DEPARTURE_MINUTES: "早退時間",
            AggregationCategory.PAID_HOLIDAY_DAYS: "有給日数",
            AggregationCategory.PAID_HOLIDAY_HOURS: "有給時間数",
            AggregationCategory.COMPENSATORY_HOLIODAY_DAYS: "代休日数",
            AggregationCategory.LEAVE_DAYS: "休職日数",
            AggregationCategory.LEGAL_WITHIN_45_OVERWORK_MINUTES: "45時間以内の法定外労働時間",
            AggregationCategory.LEGAL_45_OVERWORK_MINUTES: "45時間を超過した法定外労働時間",
            AggregationCategory.LEGAL_60_OVERWORK_MINUTES: "60時間を超過した法定外労働時間",
            AggregationCategory.LACK_MINUTES: "集計期間の不足時間(給与控除が必要な時間)",
            AggregationCategory.ESTIMATED_OEVRTIME_HOURS: "見込み残業時間",
            AggregationCategory.JOB_LEGAL_OVERWORK_MINUTES: "所定外労働時間+法定外労働時間",
            AggregationCategory.LATE_EARLY_DEPARTURE_MINUTES: "遅刻時間+早退時間",
            AggregationCategory.LATE_EARLY_DEPARTURE_DAYS: "遅刻回数+早退回数",
            AggregationCategory.TELEWORK_COUNT: "テレワーク回数",
            AggregationCategory.CLOSED_DAYS: "休業日数",
            AggregationCategory.STANDRAD_LEGAL_MINUTES: "標準法定労働時間",
            AggregationCategory.STANDRAD_LEGAL_DAYS: "標準法定労働日数",
            AggregationCategory.JOB_TOTAL_DAYS_WITH_OUT_TELEWORK: "所定労働出勤日数(テレワーク日数を除く)",
            AggregationCategory.CHILD_TIME_LEAVE_DAYS: "育児休暇日数",
            AggregationCategory.CHILD_TIME_LEAVE_HOURS: "育児時間休暇数",
            AggregationCategory.LEGAL_60_OVERWORK_RATE: "60時間を超える割増賃金率",
            AggregationCategory.ALTERNATIVE_LEAVE_RATE: "代替休暇を取得した場合に支払う割増賃金率",
            AggregationCategory.STANDRAD_JOB_MINUTES: "標準所定労働時間",
            AggregationCategory.BLACKOUT_DAYS: "除外日数",
            AggregationCategory.AVERAGE_WORKING_HOURS_PER_MONTH: "月の平均労働時間",
            AggregationCategory.AVERAGE_WORKING_DAYS_PER_MONTH: "月の平均労働日数",
            AggregationCategory.UNIT_PRICE: "単価",
            AggregationCategory.STANDARD_JOB_MINUTES_4_DAY: "一日の所定労働時間",
        }[self]


"""
Enum:システム項目

TRANSPORTATION_EXPENSES 交通費
TAX_EXEMPT_TRANSPORTATION_COSTS 非課税対象交通費
TAXABLE_TRANSPORTATION_EXPENSES 課税対象交通費
TAXABLE_AMOUNT 課税対象額
HEALTH_INSURANCE_INCLUDE 健康保険
HEALTH_INSURANCE 健康保険[介護保険を除く]
WELFARE_PENSION 厚生年金
EMPLOYEES_PENSION_FUND 厚生年金基金
EMPLOYMENT_INSURANCE 雇用保険
EMPLOYMENT_INSURANCE_AMOUNT 雇用保険対象額
SOCIAL_INSURANCE_AMOUNT 社会保険対象額
SOCIAL_INSURANCE_TOTAL 社会保険計
TAXABLE_AMOUNT_2 課税対象額 [課税給与－健康保険－厚生年金－雇用保険]
INCOME_TAX 源泉所得税
RESIDENT_TAX 住民税
GENERAL_HEALTH_INSURANCE 健康保険　一般　※介護保険料は含みません
HEALTH_INSURANCE_ADJUSTMENT 健康保険　調整　※介護保険料は含みません
CARE_INSURANCE 介護保険
LUNCH_BOX_ACCOUNTS_PAYABLE 弁当未払金
TAXABLE_AMOUNT_BONUS [賞与]課税対象額
HEALTH_INSURANCE_INCLUDE_BONUS [賞与]健康保険
HEALTH_INSURANCE_BONUS [賞与]健康保険[介護保険を除く]
WELFARE_PENSION_BONUS [賞与]厚生年金
EMPLOYMENT_INSURANCE_BONUS [賞与]雇用保険
EMPLOYMENT_INSURANCE_AMOUNT_BONUS [賞与]雇用保険対象額
SOCIAL_INSURANCE_AMOUNT_BONUS [賞与]社会保険対象額
SOCIAL_INSURANCE_TOTAL_BONUS [賞与]社会保険計
TAXABLE_AMOUNT_2_BONUS [賞与]課税対象額 [課税給与－健康保険－厚生年金－雇用保険]
INCOME_TAX_BONUS [賞与]源泉所得税
GENERAL_HEALTH_INSURANCE_BONUS [賞与]健康保険　一般　※介護保険料は含みません
HEALTH_INSURANCE_ADJUSTMENT_BONUS [賞与]健康保険　調整　※介護保険料は含みません
CARE_INSURANCE_BONUS [賞与]介護保険

"""


class SystemItem(IntEnum):
    TRANSPORTATION_EXPENSES = 400
    TAX_EXEMPT_TRANSPORTATION_COSTS = 401
    TAXABLE_TRANSPORTATION_EXPENSES = 402
    TAXABLE_AMOUNT = 491
    HEALTH_INSURANCE_INCLUDE = 501
    HEALTH_INSURANCE = 502
    WELFARE_PENSION = 503
    EMPLOYEES_PENSION_FUND = 504
    EMPLOYMENT_INSURANCE = 505
    EMPLOYMENT_INSURANCE_AMOUNT = 506
    SOCIAL_INSURANCE_AMOUNT = 507
    SOCIAL_INSURANCE_TOTAL = 510
    TAXABLE_AMOUNT_2 = 520
    INCOME_TAX = 521
    RESIDENT_TAX = 525
    GENERAL_HEALTH_INSURANCE = 581
    HEALTH_INSURANCE_ADJUSTMENT = 582
    CARE_INSURANCE = 583
    LUNCH_BOX_ACCOUNTS_PAYABLE = 584
    TAXABLE_AMOUNT_BONUS = 586
    HEALTH_INSURANCE_INCLUDE_BONUS = 587
    HEALTH_INSURANCE_BONUS = 588
    WELFARE_PENSION_BONUS = 589
    EMPLOYMENT_INSURANCE_BONUS = 590
    EMPLOYMENT_INSURANCE_AMOUNT_BONUS = 591
    SOCIAL_INSURANCE_AMOUNT_BONUS = 592
    SOCIAL_INSURANCE_TOTAL_BONUS = 593
    TAXABLE_AMOUNT_2_BONUS = 594
    INCOME_TAX_BONUS = 595
    GENERAL_HEALTH_INSURANCE_BONUS = 596
    HEALTH_INSURANCE_ADJUSTMENT_BONUS = 597
    CARE_INSURANCE_BONUS = 598

    @property
    def label(self) -> str:
        return {
            SystemItem.TRANSPORTATION_EXPENSES: "交通費",
            SystemItem.TAX_EXEMPT_TRANSPORTATION_COSTS: "非課税対象交通費",
            SystemItem.TAXABLE_TRANSPORTATION_EXPENSES: "課税対象交通費",
            SystemItem.TAXABLE_AMOUNT: "課税対象額",
            SystemItem.HEALTH_INSURANCE_INCLUDE: "健康保険",
            SystemItem.HEALTH_INSURANCE: "健康保険[介護保険を除く]",
            SystemItem.WELFARE_PENSION: "厚生年金",
            SystemItem.EMPLOYEES_PENSION_FUND: "厚生年金基金",
            SystemItem.EMPLOYMENT_INSURANCE: "雇用保険",
            SystemItem.EMPLOYMENT_INSURANCE_AMOUNT: "雇用保険対象額",
            SystemItem.SOCIAL_INSURANCE_AMOUNT: "社会保険対象額",
            SystemItem.SOCIAL_INSURANCE_TOTAL: "社会保険計",
            SystemItem.TAXABLE_AMOUNT_2: "課税対象額 [課税給与－健康保険－厚生年金－雇用保険]",
            SystemItem.INCOME_TAX: "源泉所得税",
            SystemItem.RESIDENT_TAX: "住民税",
            SystemItem.GENERAL_HEALTH_INSURANCE: "健康保険　一般　※介護保険料は含みません",
            SystemItem.HEALTH_INSURANCE_ADJUSTMENT: "健康保険　調整　※介護保険料は含みません",
            SystemItem.CARE_INSURANCE: "介護保険",
            SystemItem.LUNCH_BOX_ACCOUNTS_PAYABLE: "弁当未払金",
            SystemItem.TAXABLE_AMOUNT_BONUS: "[賞与]課税対象額",
            SystemItem.HEALTH_INSURANCE_INCLUDE_BONUS: "[賞与]健康保険",
            SystemItem.HEALTH_INSURANCE_BONUS: "[賞与]健康保険[介護保険を除く]",
            SystemItem.WELFARE_PENSION_BONUS: "[賞与]厚生年金",
            SystemItem.EMPLOYMENT_INSURANCE_BONUS: "[賞与]雇用保険",
            SystemItem.EMPLOYMENT_INSURANCE_AMOUNT_BONUS: "[賞与]雇用保険対象額",
            SystemItem.SOCIAL_INSURANCE_AMOUNT_BONUS: "[賞与]社会保険対象額",
            SystemItem.SOCIAL_INSURANCE_TOTAL_BONUS: "[賞与]社会保険計",
            SystemItem.TAXABLE_AMOUNT_2_BONUS: "[賞与]課税対象額 [課税給与－健康保険－厚生年金－雇用保険]",
            SystemItem.INCOME_TAX_BONUS: "[賞与]源泉所得税",
            SystemItem.GENERAL_HEALTH_INSURANCE_BONUS: "[賞与]健康保険　一般　※介護保険料は含みません",
            SystemItem.HEALTH_INSURANCE_ADJUSTMENT_BONUS: "[賞与]健康保険　調整　※介護保険料は含みません",
            SystemItem.CARE_INSURANCE_BONUS: "[賞与]介護保険",
        }[self]


"""
Enum:雇用保険加入有無
YES 有り
NONE 無し
"""


class EmploymentInsuranceExistence(IntEnum):
    YES = 1
    NONE = 2


"""
Enum:健康保険加入有無
YES 有り
NONE 無し
"""


class HealthInsuranceExistence(IntEnum):
    YES = 1
    NONE = 2


"""
Enum:厚生年金加入有無
YES 有り
NONE 無し
"""


class WelfarePensionExistence(IntEnum):
    YES = 1
    NONE = 2


"""
Enum:厚生年金基金加入有無
YES 有り
NONE 無し
"""


class EmployeesPensionFundExistence(IntEnum):
    YES = 1
    NONE = 2


"""
Enum:事業の種類
A 一般事業所
B 農林水産業・清酒製造業
C 建設業
"""


class TypeOfBusiness(IntEnum):
    A = 1
    B = 2
    C = 3


"""
Enum:社会保険料の徴収タイミング
A 当月分の社会保険料を当月支給の給与から控除
B 前月分の社会保険料を当月支給の給与から控除
"""


class CollectionOfSocialInsurancePremiums(IntEnum):
    A = 1
    B = 2


"""
Enum:住民税の徴収タイミング
A 当月分の住民税を当月支給の給与から控除
B 前月分の住民税を当月支給の給与から控除
"""


class CollectionOfResidentTax(IntEnum):
    A = 1
    B = 2


"""
Enum:健康保険/介護保険端数区分
ROUNDED_DOWN 切り捨て（端数は事業主負担）
ROUNDING 50銭以下切捨・50銭超切上（政府管掌に従・給与控除）
"""


class HealthInsuranceNursingCareFraction(IntEnum):
    ROUNDED_DOWN = 1
    ROUNDING = 2


"""
Enum:厚生年金端数区分
ROUNDED_DOWN 切り捨て（端数は事業主負担）
ROUNDING 50銭以下切捨・50銭超切上（政府管掌に従・給与控除）
"""


class WelfarePensionFractionClassification(IntEnum):
    ROUNDED_DOWN = 1
    ROUNDING = 2


"""
Enum:雇用保険端数区分
ROUNDED_DOWN 切り捨て（端数は事業主負担）
ROUNDING 50銭以下切捨・50銭超切上（政府管掌に従・給与控除）
"""


class EmploymentInsuranceFractionClassification(IntEnum):
    ROUNDED_DOWN = 1
    ROUNDING = 2


"""
Enum:口座種別
ORDINARY_DEPOSIT 普通預金
CURRENT_ACCOUNT 当座預金
"""


class AccountClassification(IntEnum):
    ORDINARY_DEPOSIT = 1
    CURRENT_ACCOUNT = 2


"""
Enum:振込方法
TRANSFER 振込
CASH 現金
ELECTORIC_MONEY 電子マネー
"""


class TransferMethod(IntEnum):
    TRANSFER = 1
    CASH = 2
    ELECTORIC_MONEY = 3


"""
Enum:支給/控除区分
PAYMENT 支給項目
DEDUCTION 控除項目
SUMMARY 集計項目
"""


class PaymentDeductionCategory(IntEnum):
    PAYMENT = 1
    DEDUCTION = 2
    SUMMARY = 3


"""
Enum:雇用保険対象区分
TARGET 対象
OUT_OF_SCOPE 対象外
"""


class EmploymentInsuranceTargetCategory(IntEnum):
    TARGET = 1
    OUT_OF_SCOPE = 2


"""
Enum:介護保険対象区分
TARGET 対象
OUT_OF_SCOPE 対象外
"""


class IsLongTermCareInsuranceTargetCategory(IntEnum):
    TARGET = 1
    OUT_OF_SCOPE = 2


"""
Enum:出勤状況
AWAY_FROM_KEYBOARD   離席中
IN_A_MEETING         会議中
IS_OUT               外出中
AT_WORK              勤務中（客先）
"""


class AttendanceStatus(IntEnum):
    AWAY_FROM_KEYBOARD = 1
    IN_A_MEETING = 2
    IS_OUT = 3
    AT_WORK = 4


"""
Enum:所得税対象区分
TARGET 対象
OUT_OF_SCOPE 対象外
"""


class TaxTargetCategory(IntEnum):
    TARGET = 1
    OUT_OF_SCOPE = 2


"""
Enum:シフト利用有無
TARGET 対象
OUT_OF_SCOPE 対象外
"""


class IsShiftWork(IntEnum):
    TARGET = 1
    OUT_OF_SCOPE = 2


"""
Enum:社会保険対象区分
TARGET 計算対象
OUT_OF_SCOPE 計算対象外
"""


class SocialInsuranceTargetCategory(IntEnum):
    TARGET = 1
    OUT_OF_SCOPE = 2


"""
Enum:算定区分
NoCalculationRequired 算定不要
DeterminedAtTheTimeOfQualificationAcquisition 資格取得時の決定
RegularCalculation 定時決定
CalculatedFromTimeToTime 随時改定
RevisedAtTheEndOfChildcareLeave 育児休業等終了時の改定
InsurerDecision 保険者決定
"""


class CalculationCategory(IntEnum):
    NoCalculationRequired = 1
    DeterminedAtTheTimeOfQualificationAcquisition = 2
    RegularCalculation = 3
    CalculatedFromTimeToTime = 4
    RevisedAtTheEndOfChildcareLeave = 5
    InsurerDecision = 6


"""
Enum:AI計算区分
TurnoverRate 転職率
"""


class AiCalculationCategory(IntEnum):
    TurnoverRate = 1


"""
Enum:固定/変動区分
FIXED 固定項目
FLUCTUATION 変動項目
SYSTEM システム項目
"""


class FixedFluctuation(IntEnum):
    FIXED = 1
    FLUCTUATION = 2
    SYSTEM = 3


"""
Enum:加算/減算区分
ADDITION 加算
SUBTRACTION 減算
"""


class AdditionSubtractionClassification(IntEnum):
    ADDITION = 1
    SUBTRACTION = 2


"""
Enum:給与区分
YEAR 年俸制
MONTH 月給制
MONTH_DAY 月給日給制
DAY_MONTH 日給月給制
DAY 日給制[廃止]
DAY_TIME 日給時給制[廃止]
TIME 時給制
BONUS 賞与
#   DAY = 5  # 間違って番号を再利用しないようにコメント化して残す
#   DAY_TIME = 6  # 間違って番号を再利用しないようにコメント化して残す
"""


class SalaryCategory(IntEnum):
    YEAR = 1
    MONTH = 2
    MONTH_DAY = 3
    DAY_MONTH = 4
    TIME = 7
    BONUS = 8


"""
Enum:演算方法
DIVISION 除算
MULTI_PLICATION 乗算
"""


class DivisionMultiplicationDivision(IntEnum):
    DIVISION = 1
    MULTI_PLICATION = 2


"""
Enum:支給単位
MONTHLY 毎月
EVERY_THREE_MONTHS 三か月単位
SEMI_ANNUAL_UNIT 半年単位
NON 支給しない
"""


class PaymentUnit(IntEnum):
    MONTHLY = 1
    EVERY_THREE_MONTHS = 2
    SEMI_ANNUAL_UNIT = 3
    NON = 9


"""
Enum:支給月度
JAN_APL_JUL_OCT 1,4,7,10月
FEB_MAY_AUG_NOV 2,5,8,11月
MAR_JUN_SEP_DEC 3,6,9,12月
JAN_JLY 1,7月
FEB_AUG 2,8月
MAR_SEP 3,9月
APL_OCT 4,10月
MAY_NOV 5,11月
JUN_DEC 6,12月
"""


class TargetMonth(IntEnum):
    JAN_APL_JUL_OCT = 1
    FEB_MAY_AUG_NOV = 2
    MAR_JUN_SEP_DEC = 3
    JAN_JLY = 4
    FEB_AUG = 5
    MAR_SEP = 6
    APL_OCT = 7
    MAY_NOV = 8
    JUN_DEC = 9


"""
Enum:支給方法
CASH 現金
PAYMENT_IN_KIND 現物支給
ACCOUNT_TRANSFER 口座振替
OUT_OF_SCOPE 対象外
"""


class PaymentMethod(IntEnum):
    CASH = 1
    PAYMENT_IN_KIND = 2
    ACCOUNT_TRANSFER = 3
    OUT_OF_SCOPE = 4


"""
Enum:交通区分
TRANSPORTATION_FACILITIES 交通機関
TOLL_ROAD 有料道路
TRANSPOTATION_EQUIPMENT 交通用具
"""


class TrafficDivision(IntEnum):
    TRANSPORTATION_FACILITIES = 1
    TOLL_ROAD = 2
    TRANSPOTATION_EQUIPMENT = 3


"""
Enum:交通用具(自動車や自転車などの交通用具を使用している人に支給する通勤手当の非課税枠)を使用する距離
A 片道 2キロメートル未満
B 片道 2キロメートル以上10キロメートル未満
C 片道10キロメートル以上15キロメートル未満
D 片道15キロメートル以上25キロメートル未満
E 片道25キロメートル以上35キロメートル未満
F 片道35キロメートル以上45キロメートル未満
G 片道45キロメートル以上55キロメートル未満
H 片道55キロメートル以上
"""


class DistanceToUseTransportationEquipment(IntEnum):
    TYPE_A = 1
    TYPE_B = 2
    TYPE_C = 3
    TYPE_D = 4
    TYPE_E = 5
    TYPE_F = 6
    TYPE_G = 7
    TYPE_H = 8


"""
Enum:支給区分
SALARY 給与
BONUS 賞与
"""


class SalaryBonusClassification(IntEnum):
    SALARY = 1
    BONUS = 2


"""
Enum:受取済フラグ
ON 受取済
OFF 受取未
"""


class CatchFlg(IntEnum):
    ON = 1
    OFF = 2


"""
Enum:支払フラグ
ON 支払済
OFF 未払い
"""


"""
Enum:デフォルト勤務体系フラグ
ON デフォルト勤務体系
OFF その他
"""


class DefaultWorkScheduleFlg(IntEnum):
    ON = 1
    OFF = 2


"""
Enum:デフォルト部署フラグ
ON デフォルト部署
OFF その他
"""


class DefaultGroupFlg(IntEnum):
    ON = 1
    OFF = 2


"""
Enum:符号
PLUS プラス
MINUS マイナス
"""


class Sign(IntEnum):
    PLUS = 1
    MINUS = 2


"""
Enum:会計帳票区分
BALANCE_SHEET 貸借対照表
PROFIT_AND_LOSS_STATMENT 損益計算書
MANUFACTURING_COST_REPORT 製造原価報告書
"""


class AccountingFromClassification(IntEnum):
    BALANCE_SHEET = 1
    PROFIT_AND_LOSS_STATMENT = 2
    MANUFACTURING_COST_REPORT = 3


"""
Enum:税種別
A01課売 10%
A02 課売-返還 10%
A03 課売-貸倒 10%
A04 課売-回収 10%
A05 輸売 0%
A06 輸売-返還 0%
A07 輸売-貸倒 0%
A08 非売
A09 非売-返還
A10 非売-貸倒
A11非輸
A12 非輸-返還
A13 非輸-貸倒
A14 対象外売
A15 非売-有証
A16 対象外
A17 課仕 10%
A18 課仕-返還 10%
A19 輸仕-本体 10%
A20 非仕
A21対象外仕
"""


class TaxType(IntEnum):
    A01 = 1
    A02 = 2
    A03 = 3
    A04 = 4
    A05 = 5
    A06 = 6
    A07 = 7
    A08 = 8
    A09 = 9
    A10 = 10
    A11 = 11
    A12 = 12
    A13 = 13
    A14 = 14
    A15 = 15
    A16 = 16
    A17 = 17
    A18 = 18
    A19 = 19
    A20 = 20
    A21 = 21


"""
Enum:スマイルマーク
WELL 調子がいい
GLAD 嬉しい
SAD 悲しい
MAD  怒っている
SICK 具合が悪い
SLEEPY 眠い
LONELY 寂しい
NERVOUS 緊張している
NORMAL とくになし
"""


class SmileMark(IntEnum):
    WELL = 1
    GLAD = 2
    SAD = 3
    MAD = 4
    SICK = 5
    SLEEPY = 6
    LONELY = 7
    NERVOUS = 8
    NORMAL = 9


"""
Enum:法人フラグ
CORPORATE 法人
PRIVATE 個人
"""


class Corporate(IntEnum):
    CORPORATE = 1
    PRIVATE = 2


"""
Enum:等級変更確認フラグ
ON 更新済
OFF 更新未
"""


class GradeUpdateFlg(IntEnum):
    ON = 1
    OFF = 2


"""
Enum:メッセージタイプ
PRIVATE 個人向け
CORPORATION 法人向け
COMMON 共通
"""


class MessageType(IntEnum):
    PRIVATE = 1
    CORPORATION = 2
    COMMON = 3


"""
Enum:分類
NORMAL 正常
WARNING 警告
ERR 異常
"""


class MessageClassification(IntEnum):
    NORMAL = 1
    WARNING = 2
    ERR = 3


"""
Enum:原因
NOMAL 問題なし
PROGRAM_PROBLEM コード問題
ENVIRONMENT_ISSUES 環境問題
OPERATION_MISTAKE 操作ミス
UNKNOWN 不明
"""


class Cause(IntEnum):
    NOMAL = 0
    PROGRAM_PROBLEM = 1
    ENVIRONMENT_ISSUES = 2
    OPERATION_MISTAKE = 3
    UNKNOWN = 4


"""
Enum:対応
NOMAL 問題なし
CODE_PATCH コード修正
INFRASTRYCTURE_SUPPORT 環境対応
INQUIRY 問い合わせ
RETRY 再実行
RESEARCH 調査
"""


class Correspondence(IntEnum):
    NOMAL = 0
    CODE_PATCH = 1
    INFRASTRYCTURE_SUPPORT = 2
    INQUIRY = 3
    RETRY = 4
    RESEARCH = 5


"""
Enum:国別コード
https://ja.wikipedia.org/wiki/ISO_3166-1
JPN 日本
"""


class CountryCode(IntEnum):
    USA = 840
    JPN = 392


"""
Enum:選出方法
ELECTION_BY_VOTING 投票による選挙
RECOMMENDATION 推薦
RAISED_HANDS 挙手
WORKER_DISCUSSION 労働者の話し合い
RESOLUTION 持ち回り決議
VOTING_BY_EMAIL 電子メールによる投票
"""


class ElectionMethod(IntEnum):
    ELECTION_BY_VOTING = 1
    RECOMMENDATION = 2
    RAISED_HANDS = 3
    WORKER_DISCUSSION = 4
    RESOLUTION = 5
    VOTING_BY_EMAIL = 6


"""
Enum:特例措置対象事業場
ON 対象
OFF 対象外
"""


class SpecialMeasures(IntEnum):
    ON = 1
    OFF = 2


"""
Enum:単位
YEAR 年
MONTH 月
WEEK 週
DAY 日
"""


class Unit(IntEnum):
    YEAR = 1
    MONTH = 2
    WEEK = 3
    DAY = 4


"""
Enum:見積単位
MAN_MONTH 人月
"""


class EstimateUnit(IntEnum):
    MAN_MONTH = 1


"""
Enum:変更区分
INTERNAL 内的
EXTERNAL 外的
"""


class ChangeCategory(IntEnum):
    INTERNAL = 1
    EXTERNAL = 2


"""
Enum:変更状態
NOT_STARTED 未着手
IN_PROCESS 修正中
UNDER_TESTING テスト中
COMPLETED 完了
"""


class ChangeStatus(IntEnum):
    NOT_STARTED = 1
    IN_PROCESS = 2
    UNDER_TESTING = 3
    COMPLETED = 9


"""
Enum:データ単位
TIME_HH 単位[時]
TIME_HHMM 単位[時分]
TIME_MM 単位[分]
DATE_YYYY 単位[年]
DATE_YYYYMM 単位[年月]
DATE_DAY 単位[日]
COUNT 単位[回数]
CURRENCY_YEN 単位[円]
"""


class DataUnit(IntEnum):
    TIME_HH = 1
    TIME_HHMM = 2
    TIME_MM = 3
    DATE_YYYY = 4
    DATE_YYYYMM = 5
    DATE_DAY = 6
    COUNT = 7
    CURRENCY_YEN = 8


"""
Enum:警告タイプ
WARN 警告
ERR 違反
"""


class AlertType(IntEnum):
    WARN = 1
    ERR = 2


"""
Enum:申請対象フラグ
ON 対象
OFF 対象外
OUT 対象外[利用不可]
"""


class WorkflowFlg(IntEnum):
    ON = 1
    OFF = 2
    OUT = 9


"""
Enum:パートナー参照可否
AVAILABLE 参照可能
UNAVAILABLE 参照不可
"""


class IsVisible(IntEnum):
    AVAILABLE = 1
    UNAVAILABLE = 2


"""
Enum:寡婦/ひとり親
WIDOW 寡婦/寡夫
SINGLE_PARENT ひとり親
OFF 対象外
"""


class IsWidow(IntEnum):
    WIDOW = 1
    SINGLE_PARENT = 2
    OFF = 9


"""
Enum:勤労学生
ON 対象
OFF 対象外
"""


class IsWorkingStudent(IntEnum):
    ON = 1
    OFF = 2


"""
Enum:指定区分
A 本人指定
B 計画的付与
C 使用者指定
"""


class DesignatedCategory(IntEnum):
    A = 1
    B = 2
    C = 3


"""
Enum:スマイルマーク利用有無
ON 有り
OFF 無し
"""


class IsSmileMark(IntEnum):
    ON = 1
    OFF = 2


"""
Enum:緊急停止フラグ
ON 緊急停止中
OFF 運営中
"""


class EmergencyStopFlag(IntEnum):
    ON = 1
    OFF = 2


"""
Enum:勤務の種類
NORMAL 通常勤務
FLEX フレックス制
SHIFT シフト勤務
"""


class WorkingSystemType(IntEnum):
    NORMAL = 1
    FLEX = 2
    SHIFT = 3


"""
Enum:カレンダーフラグ
NOT_SET 未設定
WORKING_DAY 出勤日
JOB_HOLIDAY 所定休日
LEGAL_HOLIDAY 法定休日
PLAN_PAID_HOLIDAY 有給奨励日
SUMMER_HOLIDAY 夏季休日
NEW_YEAR_HOLIDAY_SEASON 年末年始
NATIONAL_HOLIDAY 国民の祝日
PLAN_GRANT_OF_PAID_LEAVE 有給休暇の計画的付与
HOLIDAYS_ATTRIBUTABLE_TO_THE_USER 使用者の責に帰す休業日
"""


class Calender(IntEnum):
    NOT_SET = 0
    WORKING_DAY = 1
    JOB_HOLIDAY = 2
    LEGAL_HOLIDAY = 3
    PLAN_PAID_HOLIDAY = 4
    SUMMER_HOLIDAY = 5
    NEW_YEAR_HOLIDAY_SEASON = 6
    NATIONAL_HOLIDAY = 7
    PLAN_GRANT_OF_PAID_LEAVE = 8
    HOLIDAYS_ATTRIBUTABLE_TO_THE_USER = 9


"""
Enum:お知らせの種類
NOTICE お知らせ
WARNING 警告
EMERGENCY 緊急
"""


class NoticeType(IntEnum):
    NOTICE = 1
    WARNING = 2
    EMERGENCY = 3


"""
Enum:既読フラグ
READ 既読
UNREAD 未読
"""


class ReadFlg(IntEnum):
    READ = 1
    UNREAD = 2


"""
Enum:源泉徴収税額の計算方法
USE_TAX_TABLE 税額表（月額表）を利用
USE_SPECIAL_CASE_COMPUTER_CALUCLATION 電算機計算の特例を利用
"""


class CalculateWithholdingTax(IntEnum):
    USE_TAX_TABLE = 1
    USE_SPECIAL_CASE_COMPUTER_CALUCLATION = 2


"""
Enum:理由タイプ
LEGAL_OVERWORK 法定外労働
LEGAL_HOLIDAY_OVERWORK 休日労働
TRANSFORMATION_TIME_LABOR 変形時間労働
LIMIT_OVERWORK 限度時間超過
"""


class ReasonsType(IntEnum):
    LEGAL_OVERWORK = 1
    LEGAL_HOLIDAY_OVERWORK = 2
    TRANSFORMATION_TIME_LABOR = 3
    LIMIT_OVERWORK = 4


"""
Enum:限度時間を超えて労働させる場合における手続き
CODE_1  労働時間が一定時間を超えた労働者に医師による面接指導を実施すること
CODE_2  労働基準法第37条第4項に既定する時刻の間において労働させる回数を1箇月について一定回数以内とすること
CODE_3  就業から始業までに一定時間以上の継続した休息時間を確保すること
CODE_4  労働者の勤務状況及びその健康状態に応じて、代償休日又は特別な休暇を付与すること
CODE_5  労働者の勤務状況及びその健康状態に応じて、健康診断を実施すること
CODE_6  年次有給休暇についてまとまった日数連続して取得することを含めてその取得を促進すること
CODE_7  心とからだの健康問題についての相談窓口を設置すること
CODE_8  労働者の勤務状況及びその健康状態に配慮し、必要な場合には適切な部署に配置転換をすること
CODE_9  必要に応じて、産業医等による助言・指導を受け、又は労働者に産業医等による保険指導を受けさせること
CODE_10 その他
"""


class ProcedureHealth(IntEnum):
    CODE_1 = 1
    CODE_2 = 2
    CODE_3 = 3
    CODE_4 = 4
    CODE_5 = 5
    CODE_6 = 6
    CODE_7 = 7
    CODE_8 = 8
    CODE_9 = 9
    CODE_10 = 10


"""
Enum:様式タイプ
STYLE_1様式1
STYLE_2 様式2
STYLE_3 様式3
STYLE_4 様式4
STYLE_5 様式5
STYLE_6 様式6
STYLE_7 様式7
"""


class DocumentStyle(IntEnum):
    STYLE_1 = 1
    STYLE_2 = 2
    STYLE_3 = 3
    STYLE_4 = 4
    STYLE_5 = 5
    STYLE_6 = 6
    STYLE_7 = 7


"""
Enum:勤務間インターバル制度の取扱方法
ADVANCE_START_TIME 始業時刻を繰り下げる
CONSIDER_OVERLAPPING_TIME_AS_LABOR 重複する時間を働いたものとみなす
"""


class HandlingMethodWorkingInterval(IntEnum):
    ADVANCE_START_TIME = 1
    CONSIDER_OVERLAPPING_TIME_AS_LABOR = 2


"""
Enum:勤務間インターバル適用除外
SERIOUS_CLAIMS 重大なクレーム
SUDDEN_TROUBLE 突発的なトラブル
CORRESPONDS_LOCAL_TIME_OF_OVERSEAS_CASE 海外事案の現地時間に対応
LABOR_STANDARDS_LAW_ARTICLE_33 労働基準法第33条の規定に基づき、災害その他避けることのできない事由によって臨時の必要がある場合
ETC その他
"""


class ExemptionWorkingInterval(IntEnum):
    SERIOUS_CLAIMS = 1
    SUDDEN_TROUBLE = 2
    CORRESPONDS_LOCAL_TIME_OF_OVERSEAS_CASE = 3
    LABOR_STANDARDS_LAW_ARTICLE_33 = 4
    ETC = 5


"""
Enum:締め区分
ATTENDANCE RECORD 勤怠
SALARY 給与
"""


class ClosingClassification(IntEnum):
    ATTENDANCE = 1
    SALARY = 2


"""
Enum:バッチ処理ステータス
MAKING 実行中
MAKED 実行完了
ERR 実行エラー
"""


class BatchStatus(IntEnum):
    MAKING = 1
    MAKED = 2
    ERR = 9


"""
Enum:締め処理タイプ
FORCED_CLOSING 締め処理
LEGAL_RULE_VIOLATOR 36協定監視
"""


class BatchType(IntEnum):
    FORCED_CLOSING = 1
    LEGAL_RULE_VIOLATOR = 2


"""
Enum:締め処理状態
WAITING リクエスト受付中
READY 実行待機中
PROCESSING 実行中
"""


class BatchAction(IntEnum):
    WAITING = 1
    READY = 2
    PROCESSING = 3


"""
Enum:名称変更許可フラグ
OK 変更可能
NG 変更不可
"""


class ChangeOkFlg(IntEnum):
    OK = 1
    NG = 2


"""
Enum:ラベル出力の有無
ON 出力します
OFF 出力しません
"""


class IsLabelOutput(IntEnum):
    ON = 1
    OFF = 2


"""
Enum:クォーテーションマーク
NONE なし
DOUBLE_QUOTATION ダブルクォート
SINGLE_QUOTATION シングルクォート
"""


class QuotationMark(IntEnum):
    NONE = 1
    DOUBLE_QUOTATION = 2
    SINGLE_QUOTATION = 3


"""
Enum:フィールド区切り
COMMA カンマ区切り
SPACE スペース区切り
TAB タブ区切り
"""


class FieldSeparator(IntEnum):
    COMMA = 1
    SPACE = 2
    TAB = 3


"""
Enum:時間形式
SEXAGESIMAL 60進法
DECIMAL 10進法
"""


class TimeStyle(IntEnum):
    SEXAGESIMAL = 1
    DECIMAL = 2


"""
Enum:登録単位
COMPANY 会社単位
EMPLOYEE 従業員単位
"""


class RegistrationUnit(IntEnum):
    COMPANY = 1
    EMPLOYEE = 2


"""
Enum:労務費区分
DIRECT_LABOR_COST 直接労務費
INDIRECT_LABOR_COST 間接労務費
"""


class LaborCostCategory(IntEnum):
    DIRECT_LABOR_COST = 1
    INDIRECT_LABOR_COST = 2


"""
Enum:労務費区分
WORK 労働希望日
NEVER_WORK 所定休日
LEGAL_HOLIDAY 法定休日
"""


class WorkStatus(IntEnum):
    WORK = 1
    NEVER_WORK = 2
    LEGAL_HOLIDAY = 3


"""
Enum:出勤簿レイアウト区分
HORIZONTAL ヨコ型
VERTICAL タテ型
"""


class AttendanceRecordLayout(IntEnum):
    HORIZONTAL = 1
    VERTICAL = 2


"""
Enum:上場
LISTING 上場
UNLISTED 非上場
"""


class Listing(IntEnum):
    LISTING = 1
    UNLISTED = 2


"""
Enum:上場市場
RANK_1 プライム
RANK_2 スタンダード
RANK_3 グロース
RANK_4 名証一部
RANK_5 名証二部
RANK_6 セントレックス
RANK_7 札幌証券取引所
RANK_8 アンビシャス
RANK_9 福岡証券取引所
RANK_10 Q-Board
"""


class ListingMarket(IntEnum):
    RANK_1 = 1
    RANK_2 = 2
    RANK_3 = 2
    RANK_4 = 2
    RANK_5 = 2
    RANK_6 = 2
    RANK_7 = 2
    RANK_8 = 2
    RANK_9 = 2
    RANK_10 = 2


"""
Enum:上場予定
ON 有り
OFF 無し
"""


class ScheduledToBeListed(IntEnum):
    ON = 1
    OFF = 2


"""
Enum:Vue側のラベル管理
"""


class VueLabel(IntEnum):
    number_of_employees_in_use = 1
    about_artemis = 1
    account_classification = 1
    account_number = 1
    achievement = 1
    active_employee_count = 1
    actual = 1
    add_national_holiday = 1
    add_pin = 1
    administrator = 1
    admin_login = 1
    age = 1
    aggregation_category = 1
    agreement_parties_employee_name = 1
    agreement_parties_job_title_name = 1
    allocation = 1
    all_employee_application_control = 1
    already = 1
    amount_from = 1
    amount_of_money = 1
    amount_to = 1
    annual_holidays = 1
    annual_result = 1
    apl = 1
    application_type = 1
    apply_employee = 1
    apply_person = 1
    applicant_employee = 1
    application = 1
    application_classification = 1
    application_inf = 1
    approval_attendance = 1
    approval_route = 1
    approval_salary = 1
    approved = 1
    approver = 1
    approverl_company = 1
    approverl_employee = 1
    approverl_employee_name = 1
    approverl_group = 1
    approverl_role_code = 1
    app_store_logo_path = 1
    apr = 1
    artemis_login = 1
    artemis_system_admin = 1
    assign_to_employee = 1
    attached_employee = 1
    attached_file = 1
    attendance = 1
    attendance_record = 1
    aug = 1
    auto_approverl_flag = 1
    available = 1
    average = 1
    average_age = 1
    average_wage = 1
    average_overtime_hours = 1
    average_paid_holidays = 1
    average_enrolled_months = 1
    balance = 1
    bank = 1
    bank_code = 1
    bank_search_description = 1
    bank_search_description2 = 1
    bank_transfer = 1
    bank_transfer_list = 1
    base_date_setting = 1
    basic_information = 1
    boss = 1
    boss_company = 1
    boss_employee = 1
    boss_group = 1
    branch = 1
    branch_code = 1
    branch_search_description = 1
    break_add = 1
    break_time = 1
    business_description = 1
    business_info = 1
    career_inf = 1
    cash = 1
    catch_flg = 1
    change_language = 1
    change_password = 1
    change_password_annotation1 = 1
    change_password_annotation2 = 1
    change_password_annotation3 = 1
    closing = 1
    closing_date_unit = 1
    closing_term1 = 1
    closing_term2 = 1
    comment = 1
    common_route = 1
    commute_target_date = 1
    commuting_costs = 1
    company_address_description = 1
    company_amount = 1
    company_code = 1
    company_description = 1
    company_info = 1
    company_logo = 1
    company_regist = 1
    company_regist_description = 1
    confirm_company_regist = 1
    confirm_company_regist_description1 = 1
    confirm_company_regist_description2 = 1
    confirm_employee_delete = 1
    confirm_employee_delete_description1 = 1
    confirm_employee_delete_description2 = 1
    confirm_employee_regist = 1
    confirm_employee_regist_description1 = 1
    confirm_employee_regist_description2 = 1
    confirm_employee_update = 1
    confirm_employee_update_description1 = 1
    confirm_employee_update_description2 = 1
    copy_role_code = 1
    corporate_number_page = 1
    costs_from_the_next_month = 1
    count = 1
    created_salary = 1
    credit = 1
    cumulative_number_of_special_provisions = 1
    cumulative_time_of_special_provisions = 1
    currency = 1
    dashboard = 1
    data_none = 1
    data_type = 1
    date = 1
    day = 1
    days_5 = 1
    days_4 = 1
    days_3 = 1
    days_2 = 1
    days_1 = 1
    debit = 1
    dec = 1
    deduction = 1
    deduction_salary_item_code = 1
    default = 1
    default_work_schedule = 1
    delete = 1
    delete_national_holiday = 1
    dependent = 1
    deputy_apply_employee = 1
    deputy_approver_info = 1
    deputy_approver_info_ryaku = 1
    deputy_target_person = 1
    description_of_payslip_calculation = 1
    difference = 1
    display_date = 1
    display_range = 1
    dividing_group = 1
    division_group = 1
    early_departure_application = 1
    elapsed_date = 1
    employee_amount = 1
    employee_code = 1
    employee_count = 1
    employee_description = 1
    employee_group_term_from = 1
    employee_group_term_to = 1
    employee_info = 1
    employee_info_ryaku = 1
    employee_lunch = 1
    employee_team_term_from = 1
    employee_team_term_to = 1
    employment_insurance_rate_link = 1
    employment_insurance_subscription = 1
    end = 1
    end_time = 1
    enrolled_count = 1
    existing_closing_name = 1
    existing_employee_between = 1
    face_image = 1
    failure = 1
    favorite = 1
    feb = 1
    felica_download = 1
    filter_by = 1
    first = 1
    first_month_cost = 1
    fiscal_year = 1
    fixed_value = 1
    friday = 1
    friday_ryaku = 1
    google_play_logo_path = 1
    grade = 1
    group = 1
    group_by_employee = 1
    group_by_belongs = 1
    group_by_year = 1
    group_by_month = 1
    group_by_week = 1
    group_by_day = 1
    group_inf = 1
    half_amount = 1
    health_insurance_bonus_total_rate = 1
    health_insurance_salary_total_rate = 1
    help = 1
    hire = 1
    hire_employee_count = 1
    hire_year = 1
    holiday_info = 1
    hour = 1
    hourly_wage = 1
    hourly_wage_overtime_premium = 1
    hourly_wage_legal_holiday_premium = 1
    hourly_wage_midnight_premium = 1
    hours = 1
    icon = 1
    image_file = 1
    immediate_transmission = 1
    imprint_correction_time = 1
    imprint_correction_type = 1
    including_read = 1
    increase_amount = 1
    industry_description = 1
    insurance_nursing_choice = 1
    insurance_situation_description = 1
    integrated_group = 1
    in_kind = 1
    jan = 1
    jly = 1
    job_start = 1
    job_end = 1
    journal_list = 1
    jun = 1
    jul = 1
    label_approverl_data = 1
    label_delete = 1
    label_deputy_approverl_data = 1
    label_digestion_days = 1
    label_estimated_months_of_service = 1
    label_grant_days = 1
    label_header_target_date = 1
    label_less_than_a_day = 1
    label_new_check_password = 1
    label_new_password = 1
    label_old_password = 1
    label_paid_holiday = 1
    label_paid_holidays_of_use_this_year = 1
    label_paid_reference_date = 1
    label_special_paid_holiday = 1
    label_term_from = 1
    label_term_to = 1
    label_term_time_from = 1
    label_term_time_to = 1
    labor_insurance_number_text = 1
    late_application = 1
    late_early_departure_type = 1
    latlng = 1
    layout = 1
    ledger = 1
    legal_overwork = 1
    legal_holiday_job = 1
    legal_holiday_overwork = 1
    license_count = 1
    limit_job_one_day_minutes = 1
    limit_job_one_month_minutes = 1
    limit_job_one_month_minutes_sp = 1
    limit_job_one_year_minutes = 1
    limit_legal_one_day_minutes = 1
    limit_legal_one_month_minutes = 1
    limit_legal_one_month_minutes_sp = 1
    limit_legal_one_year_minutes = 1
    limit_overwork = 1
    login = 1
    login_page = 1
    login_user_info = 1
    logout = 1
    logout_ryaku = 1
    lunch = 1
    mail_address = 1
    mail_address_notset = 1
    management_parties_employee_name = 1
    management_parties_job_title_name = 1
    mar = 1
    max_length = 1
    max_length_decimal = 1
    max_length_integral = 1
    may = 1
    minute = 1
    mitsui = 1
    mizuho = 1
    monday = 1
    monday_ryaku = 1
    month = 1
    monthly = 1
    monthly_amount = 1
    monthly_check_items = 1
    months = 1
    national_holiday = 1
    new_add = 1
    new_closing_name = 1
    new_company = 1
    non_statutory_working_hours = 1
    notice_message = 1
    not_managed = 1
    nov = 1
    no_data = 1
    number_of_enrolled = 1
    number_of_legal_holidays_allowed_to_work = 1
    number_people = 1
    oct = 1
    office_description = 1
    office_info = 1
    one_day = 1
    one_month = 1
    one_year = 1
    operation = 1
    operating_company = 1
    OR = 1
    order = 1
    order_history_option = 1
    owner_mail_address = 1
    paid_annual_account = 1
    paid_holiday_inf = 1
    paid_holiday_setting = 1
    partner_account_name = 1
    partner_sub_account_name = 1
    password = 1
    payment = 1
    payment_amount = 1
    payment_description = 1
    payment_info = 1
    payment_salary_item_code = 1
    payslip_number = 1
    payslip_explanation = 1
    pending = 1
    pension_fund_contributions_subscription = 1
    people = 1
    privacy_policy = 1
    qrcode_login = 1
    read = 1
    reasons_over_work_contents_1 = 1
    reasons_over_work_contents_2 = 1
    reasons_over_work_contents_3 = 1
    reference = 1
    registered_user = 1
    remark = 1
    reservation_transmission = 1
    retirement = 1
    retirement_employee_count = 1
    re_ground = 1
    risona = 1
    role_allocation = 1
    role_or_approver = 1
    route_code = 1
    route_flag = 1
    route_name = 1
    rules = 1
    salary = 1
    salary_closing = 1
    salary_increase_simulation_description = 1
    salary_inf = 1
    salaryItem_detail_payment = 1
    salaryItem_detail_deduction = 1
    salaryItem_detail_description1 = 1
    salaryItem_detail_description2 = 1
    salaryItem_detail_description3 = 1
    salary_payment_method = 1
    saturday = 1
    saturday_ryaku = 1
    scheduled_transmission_date = 1
    screen_search = 1
    search_all = 1
    search_all_employees = 1
    search_bank = 1
    search_condition = 1
    search_result = 1
    second = 1
    select = 1
    selected_bank = 1
    select_description = 1
    send = 1
    sending_method = 1
    send_mail_payslip = 1
    send_mail_bonuspayslip = 1
    sep = 1
    serial_number = 1
    show_catch = 1
    show_password = 1
    show_payment = 1
    sign = 1
    simulation_result = 1
    skip_apply_employee = 1
    smile_mark_normal = 1
    special_provisions_year_count = 1
    special_provisions_rate_month = 1
    special_provisions_rate_year = 1
    start = 1
    start_time = 1
    status = 1
    success = 1
    sunday = 1
    sunday_ryaku = 1
    target = 1
    target_amount = 1
    target_employee = 1
    target_person = 1
    target_year = 1
    target_year_month = 1
    tax_cost = 1
    team_inf = 1
    term = 1
    terms_of_use = 1
    this_business_year = 1
    this_month = 1
    this_year = 1
    thursday = 1
    thursday_ryaku = 1
    today_stamp_time = 1
    total = 1
    total_amount = 1
    total_amount_of_money = 1
    total_break_time = 1
    total_payment_amount = 1
    total_time = 1
    transfer = 1
    transfer_information = 1
    transfer_amount_of_money = 1
    transfer_method = 1
    tuesday = 1
    tuesday_ryaku = 1
    type = 1
    type_of_day_monthly_summary = 1
    type_of_day_summary = 1
    ufj = 1
    unit_age = 1
    unit_byte = 1
    unit_day = 1
    unit_days_between = 1
    unit_hours = 1
    unit_mei = 1
    unit_minutes = 1
    unit_months = 1
    unit_people = 1
    unit_ratio = 1
    unit_times = 1
    unit_yen = 1
    unknown_screen = 1
    unread = 1
    updated_now = 1
    upper_group = 1
    variable_item_setting = 1
    violation = 1
    warning = 1
    warning_after_hours = 1
    warning_after_percent = 1
    warning_after_days = 1
    warning_after_number = 1
    warning_content = 1
    wednesday = 1
    wednesday_ryaku = 1
    week = 1
    working_days_5 = 1
    working_days_4 = 1
    working_days_3 = 1
    working_days_2 = 1
    working_days_1 = 1
    working_schedule = 1
    work_schedule_info = 1
    work_time = 1
    year = 1
    yearly = 1
    years = 1
    years_of_service = 1
    year_check_items = 1
    yen = 1
    yucho = 1
    after_change = 1
    agreement_parties_employee = 1
    agreement_validity_period = 1
    any = 1
    applicable_number = 1
    apply_weekday = 1
    authority_setting = 1
    average_working_hours_in_a_week = 1
    before_change = 1
    bonus_pay_slip_name = 1
    business_address = 1
    business_name = 1
    business_type = 1
    can_set = 1
    cancel_reservation = 1
    cannot_set = 1
    new_password = 1
    consumed_paid_holidays_count = 1
    copy_legal_rule = 1
    count_first = 1
    count_second = 1
    count_third = 1
    cumulative_number_of_special_provisions_count = 1
    cumulative_time_of_special_provisions_count = 1
    day_week = 1
    educational = 1
    eighteen_year_old = 1
    evaluation_period = 1
    extension_1 = 1
    extension_2 = 1
    extension_hour = 1
    extension_hour_holiday = 1
    forget_password = 1
    industrial_safety_health_pan_error_count = 1
    inoculation_venue = 1
    job_holiday = 1
    label_monthly_overwork_minutes = 1
    label_limit_legal_one_month_minutes = 1
    language_search_type1 = 1
    language_search_type2 = 1
    law_search = 1
    legal_holiday_job_1 = 1
    legal_holiday_job_2 = 1
    legal_holiday_overwork_count = 1
    legal_holiday_overwork_days_count = 1
    legal_overwork_count = 1
    less18_workers = 1
    limit_job = 1
    limit_job_time = 1
    limit_legal = 1
    limit_overwork_count_1 = 1
    limit_overwork_count_2 = 1
    limit_overwork_count_3 = 1
    limit_overwork_count_4 = 1
    limit_overwork_time_1_legal = 1
    limit_overwork_time_1_job = 1
    limit_overwork_time_2 = 1
    limit_overwork_time_3 = 1
    limit_overwork_time_4 = 1
    limit_overwork_one_month = 1
    limit_overwork_one_year_1 = 1
    limit_overwork_one_year_2 = 1
    limit_overwork_rate_1 = 1
    limit_overwork_rate_2 = 1
    limit_overwork_rate_3 = 1
    longest_working_days_in_specific_term = 1
    longest_working_days_in_target_term = 1
    longest_working_hours_in_a_day = 1
    longest_working_hours_in_a_week = 1
    management_parties_employee = 1
    maximum_consecutive_weeks_with_more_than_48_hours_worked = 1
    more_than_once = 1
    more_then = 1
    next_day = 1
    normal_working_time = 1
    number_of_legal_holidays_allowed_to_work_1 = 1
    number_of_legal_holidays_allowed_to_work_2 = 1
    number_of_inoculations = 1
    office_type = 1
    old_longest_working_day_working_time = 1
    old_longest_working_week_working_time = 1
    old_term = 1
    old_total_working_days = 1
    older_than = 1
    other_paper = 1
    over_18_target_amount_of_workers = 1
    over_48_hours_longest_weeks = 1
    over_48_hours_weeks = 1
    over_time = 1
    over18_workers = 1
    overtime_work = 1
    overtime_work_1 = 1
    overtime_work_2_1 = 1
    overtime_work_2_2 = 1
    paid_holiday_payment_pan_error_count = 1
    pay_slip_approved = 1
    pay_slip_unapproved = 1
    procedure_health_1 = 1
    procedure_health_2 = 1
    reasons_over_work_contents_1_1 = 1
    reasons_over_work_contents_1_2 = 1
    regulatory_grace_exclusion_help = 1
    remaining = 1
    reserve_date_of_sending_pay_slip = 1
    select_layout = 1
    special_number_of_consecutive_working_days = 1
    specific_content = 1
    starting_date = 1
    target_amount_of_workers = 1
    target_number_of_consecutive_working_days = 1
    tel_no = 1
    telework_flg = 1
    term_from_ryaku = 1
    term_to_ryaku = 1
    title_address = 1
    title_basic_info = 1
    title_group = 1
    title_paid_leave_info = 1
    title_private_address = 1
    title_saraly_info = 1
    title_skill = 1
    title_time = 1
    title_wokring_info = 1
    title_yen = 1
    total_amount_of_workers = 1
    total_time_count = 1
    total_working_days_in_a_term = 1
    transform_labor_time_term = 1
    transform_labor_time_term_year = 1
    transformation_monthly = 1
    transformation_term = 1
    transformation_weekly = 1
    transformation_yearly = 1
    unit_days = 1
    unit_price_pan_error_count = 1
    unit_stop_at = 1
    unit_weeks = 1
    unit_year = 1
    update_employee_ryaku = 1
    vaccination_count = 1
    vaccination_data = 1
    vaccination_serial_number = 1
    valid_term_of_application = 1
    weeks_with_more_than_48_hours_worked = 1
    work_history = 1
    worker_count = 1
    working_day_hours_in_a_month = 1
    working_hours_in_a_month = 1
    working_hours_in_a_week = 1
    ymd = 1
    overtime = 1
    late_early_departure = 1
    late_night = 1
    paid_holiday = 1
    paid_holiday_ryaku = 1
    wanna_know = 1
    pie_chart_title = 1
    pie_chart_subtitle = 1
    generation10 = 1
    generation20 = 1
    generation30 = 1
    generation40 = 1
    generation50 = 1
    generation60 = 1
    old_user_password = 1
    new_user_password = 1
    label_break = 1
    smile_mark = 1
    work_schedule = 1
    api = 1
    difference_amount = 1
    increase = 1
    decrease = 1
    registered_address = 1
    header_assign_to_screen = 1
    header_assign_to_employee = 1
    label_remaining_monthly_overwork_minutes = 1
    tranfer_date_remarks = 1
    job_start_end = 1
    required = 1
    paid_holiday_date = 1
    pie_chart_title2 = 1
    male = 1
    female = 1
    remaining_paid_holiday = 1
    address = 1
    unit_count = 1
    cash_transfer_list = 1
    boss_description = 1
    stamping_start_time_correction = 1
    stamping_end_time_correction = 1
    telework_flg_correction = 1
    work_schedule_correction = 1
    unit_num = 1
    check_this_day = 1
    before_imprint_correction_time = 1
    timeline_work = 1
    timeline_overwork = 1
    timeline_break = 1
    timeline_late = 1
    target_period_or_specific_period = 1
    notation_on_law = 1
    residents_card = 1
    residents_card2 = 1
    deputy_approverl_description1 = 1
    deputy_approverl_description2 = 1
    actual_work_start = 1
    actual_work_end = 1
    regular_holiday = 1
    hourly_annual_holiday = 1
    planned_holiday = 1
    core_time = 1
    flex_time = 1
    chat_support = 1
    check_no_stamp_only = 1
    paid_payment1 = 1
    paid_payment2 = 1
    vaccine = 1
    inoculation = 1
    not_processed = 1
    full_amount = 1
    item_name = 1
    widow = 1
    single_parent = 1
    is_working_student = 1
    no_target = 1
    is_notice = 1
    copy_add = 1
    working_day = 1
    correction_time = 1
    correction_time_employee_code = 1
    hand_correction = 1
    insured_person_reference_number = 1
    change_before_modification_date = 1
    change_before_grade_health_insurance_standard_monthly_salary = 1
    change_before_grade_welfare_pension_standard_monthly_salary = 1
    notification_date = 1
    modification_date = 1
    grade_health_insurance_standard_monthly_salary = 1
    grade_welfare_pension_standard_monthly_salary = 1
    owner_name = 1
    payment_due_date = 1
    force_password_change = 1
    violators_and_continuators_only = 1
    monitoring_items = 1
    data = 1
    violations = 1
    violation_details = 1
    imprint_correction_break_time = 1
    hint = 1
    new_hint = 1
    quick_tour = 1
    transformation_workschedule_name = 1
    max_9row_and_max_length = 1
    child_time_leave_hours = 1
    child_time_leave_days = 1
    day_before = 1
    picture = 1
    reflect_not_closed_months_description = 1
    is_send_registration_completion_email = 1
    labor_cost = 1
    total_labor_cost = 1
    total_number_of_people = 1
    desired_time = 1
    undecided_time = 1
    adjustment_time = 1
    fixed_date = 1
    payroll_month1 = 1
    salary_change = 1
    retroactive_payment_amount = 1
    working_hours = 1
    holiday = 1
    undecided = 1
    message_details = 1
    draft = 1
    last_send_date_personal = 1
    last_send_shift_schedule = 1
    supplier_name = 1
    search_3_years = 1
    closing_name = 1
    plan = 1
    achievements = 1
    summary_paid_holiday_days = 1
    summary_child_time_leave_days = 1
    authorizer = 1
    reviewer = 1
    stuff = 1
    breaktime_conditions = 1
    breaktime_range_message = 1
    special_collection_tax_amount = 1
    taxable = 1
    taxable_personnel = 1
    taxable_exempt_personnel = 1
    including_outside_period = 1
    notification_timing = 1
    not_available = 1


"""
Enum:Vue側のラベル管理
"""


class VueMessage(IntEnum):
    boss_pk_check = 1
    both_field_required = 2
    business_type_pk_check = 3
    cancellation_complete = 4
    cancellation_description = 5
    closing_date_continuous = 6
    closing_message = 7
    communication_error = 8
    company_delete_complete = 9
    company_regist_complete_title = 10
    company_regist_complete_description = 11
    confirm_to_cancellation = 12
    confirm_to_delete = 13
    confirm_to_delete_company = 14
    confirm_to_order = 15
    confirm_to_select_all_authority = 16
    contract_already_end = 17
    contract_not_enabled = 18
    day_not_deletable_at = 19
    decimal_field_required = 20
    decimal_field_higher = 21
    decimal_required = 22
    field_required = 23
    field_required_simple = 24
    field_work_time = 25
    ground_not_deletable_at = 26
    holiday_info_not_searched = 27
    inconsistent_time = 28
    inconsistent_time_at = 29
    incorrect_year_month_order = 30
    input_error = 31
    invalid_attendance_record = 32
    invalid_end_time = 33
    invalid_end_time_at = 34
    invalid_holiday_work_hours = 35
    invalid_late_night_overtime = 36
    invalid_overtime = 37
    invalid_start_time = 38
    invalid_start_time_at = 39
    is_approval_route_required = 40
    is_authority_required = 41
    is_confirm_last = 42
    is_different_integrated_group_selected = 43
    is_division_group_required = 44
    is_duplicate_group_code_selected = 45
    is_entered_new_check_password = 46
    is_entered_new_password = 47
    is_entered_old_password = 48
    is_end_time = 49
    is_integrated_group_required = 50
    is_item_number_for_row = 51
    is_item_required_for_row = 52
    is_mismatch_new_password = 53
    is_paid_holiday_management_required = 54
    is_paid_holiday_management_numeric = 55
    is_paid_holiday_payment_numeric = 56
    is_paid_holiday_payment_required = 57
    is_paid_holiday_payment_required_working_days = 58
    is_paid_holiday_payment_unique = 59
    is_role_or_approver_required = 60
    is_select_default_working_schedule_required = 61
    is_start_time = 62
    is_table_required = 63
    is_unusable_string_new_password = 64
    is_unusable_string_password = 65
    is_weakly_new_password = 66
    is_weakly_password = 67
    is_word_count_new_password = 68
    is_word_count_password = 69
    is_working_schedule_required = 70
    job_or_legal = 71
    login_input_error = 72
    max_value = 73
    min = 74
    min_value = 75
    month_day_duplicated = 76
    names_required = 77
    name_required = 78
    not_authorized = 79
    no_holiday = 80
    num_value = 81
    password_pattern = 82
    password_text = 83
    payment_info_not_registered = 84
    postalCode = 85
    release_message = 86
    report_confirmation = 87
    row_start_time_error = 88
    row_end_time_error = 89
    salaryItem_detail_calc_notedit = 90
    salaryItem_detail_payment_notedit = 91
    salaryItem_detail_system_notedit = 92
    system_error_title = 93
    tel = 94
    unexpected_error = 95
    unselectable_authority = 96
    upper_group_error = 97
    confirm_to_delete_attendance = 98
    limit_legal_one_weeks_minutes_required = 99
    transformation_term_from_required = 100
    legal_job_minutes_error = 101
    no_matching_options = 102
    no_difference_application = 103
    default_work_schdule_is_required = 104
    transformation_detail_is_required = 105
    transformation_detail_ground_is_required = 106
    transformation_detail_job_start_end_is_required = 107
    decimal_required_simple = 108
    credit_card_is_invalid = 109
    invalid_working_day_count = 110
    transformation_monthly_required = 111
    transformation_yearly_required = 112
    confirm_to_reset = 113
    is_examination_required = 114
    is_examination_required_workflow = 115
    flex_break_time_error = 116
    confirm_to_replace_ground = 117
    csv_confirmation = 118
    employee_paid_msg = 119
    attendance_delete_check = 120
    is_item_limit_number_for_row = 121
    transformation_month_term_is_out_of_range = 122
    transformation_year_term_is_out_of_range = 123
    combination_message = 124
    check_error = 125
    change_amount_message = 126
    confirm_to_insert1 = 127
    confirm_to_insert2 = 128
    confirm_to_insert3 = 129
    monthly_change_nothing = 130
    monthly_change_message = 131
    required_add_row = 132
    already_add_row = 133
    already_add_employee = 134
    employee_not_found = 135
    employee_not_found_description = 136
    no_calc = 137
    sending_information = 138
    attendance_check_unuse_workflow = 139
    attendance_delete_check_use_workflow = 140
    attendance_change_workschedule_check_use_workflow = 141
    invalid_forced_workflow = 142
    approverl_comment = 143


"""
Enum:Vue側のラベル管理
"""


class VueButton(IntEnum):
    accept_start = 1
    accept_end = 1
    add = 1
    addMonitoringConditions = 1
    add_row = 1
    add_to_dashboard = 1
    agree = 1
    allAllocationSelect = 1
    allAllocationRelease = 1
    allocation = 1
    apply = 1
    approve = 1
    assign_to_screen = 1
    assign_to_employee = 1
    auto_input = 1
    auto_input_with_end_of_month = 1
    back = 1
    bank_transfer_list = 1
    batch_print = 1
    break_end = 1
    break_start = 1
    button_change_password = 1
    calc = 1
    calculation = 1
    cancel = 1
    cancellation = 1
    clear = 1
    close = 1
    closing_attendance_record_close = 1
    closing_attendance_record_release = 1
    company_add = 1
    confirm = 1
    copy_company_data = 1
    delete = 1
    delete_company = 1
    delete_row = 1
    deny = 1
    detail = 1
    disagree = 1
    download = 1
    draft = 1
    drop = 1
    duplicate = 1
    employment_insurance_rate = 1
    execute = 1
    expand = 1
    forced_approve = 1
    go_payment_page = 1
    hold = 1
    job_start = 1
    job_end = 1
    journal_list = 1
    judge = 1
    login = 1
    logout = 1
    lunch = 1
    migrate_from_corpus = 1
    move = 1
    next = 1
    next_month = 1
    new = 1
    no = 1
    order_history = 1
    popup_cancel = 1
    postal_code_search = 1
    postal_code_search_simple = 1
    precede_approve = 1
    previous_month = 1
    print = 1
    print_all = 1
    pull_back = 1
    reapply = 1
    reflect_all_months = 1
    release = 1
    reload = 1
    remand = 1
    reserve = 1
    reserve_simple = 1
    reset_all_months = 1
    reset_specific_month = 1
    search = 1
    select = 1
    send = 1
    send_payslip = 1
    send_bonuspayslip = 1
    show_actual = 1
    show_current_ground = 1
    skip_approve = 1
    this_month = 1
    understand = 1
    unread = 1
    update = 1
    upload = 1
    view = 1
    yes = 1
    apply_to = 1
    cancel_fix = 1
    cancel_reservation = 1
    clear_all = 1
    edit = 1
    edit_all = 1
    fix = 1
    reprint = 1
    show_attendance_record = 1
    update_credit_card = 1
    cash_transfer = 1
    select_file = 1
    expand_attendance_record = 1
    shrink_attendance_record = 1
    csv = 1
    update_invoice = 1
    reflect_not_closed_months = 1
    force_approve = 1
    reset = 1
    create_csv = 1
    create_bonus = 1
    batch_printing = 1
    send_all_select = 1
    send_all_cancel = 1
    cancel_reservation_all_select = 1
    cancel_reservation_all_cancel = 1
    change_absent_day = 1
    change_work_day = 1
    read = 1
    next_employee = 1
    back_employee = 1
    back_to_list_page = 1
    set_standard_values = 1
    google_oauth_deauthorization = 1
    google_oauth_fail = 1
    google_oauth_pass = 1
    reflect_above_content = 1
    office_master_setting = 1
    send_reservation = 1
    switch_to_number_of_people_display = 1
    switch_to_employee_display = 1
    pdf = 1


"""
Enum:Vue側のラベル管理
"""


class VuePlaceholder(IntEnum):
    account_number = 1
    amount = 1
    append_title = 1
    application_classification_code = 1
    application_classification_name = 1
    application_form_name = 1
    application_number = 1
    basic_pension_number = 1
    bank_code = 1
    branch_code = 1
    break_end_time = 1
    break_start_time = 1
    break_time_start = 1
    break_time_end = 1
    building = 1
    business_type = 1
    business_name = 1
    cancel_contents = 1
    city = 1
    closing_code = 1
    closing = 1
    closing_name = 1
    collection_day = 1
    company_code = 1
    company_name = 1
    contents = 1
    contract_renewal_date = 1
    corporate_number = 1
    date_of_collection = 1
    day = 1
    dependent_code = 1
    dependent_count = 1
    dependent_name = 1
    display_date = 1
    division_reservation_date = 1
    elapsed_date = 1
    emergency_contact = 1
    employee_classification_code = 1
    employee_classification_name = 1
    employee_code = 1
    employee_name = 1
    employment_insurance_date = 1
    employment_insurance_number = 1
    end_date = 1
    end_section = 1
    end_time = 1
    estimated_months_of_service = 1
    estimated_overtime_hours = 1
    event = 1
    executed_after_approverl = 1
    expiration_days = 1
    expiration_times = 1
    extension_number = 1
    fax = 1
    felica = 1
    first_month_cost = 1
    fixed_value = 1
    ground_code = 1
    ground_name = 1
    group_code = 1
    group_name = 1
    health_insurance_sign = 1
    health_insurance_no = 1
    hire_date = 1
    hold_days = 1
    hold_times = 1
    homepage = 1
    home_page = 1
    input_password = 1
    job_title_name = 1
    integrated_reservation_date = 1
    job_start = 1
    job_end = 1
    password = 1
    labor_insurance_number = 1
    labor_standards_inspection_office = 1
    lat = 1
    late_early_departure_content = 1
    late_early_departure_supplement = 1
    layout_code = 1
    layout_name = 1
    legal_day = 1
    legal_holiday_job_end = 1
    legal_holiday_job_start = 1
    legal_percent = 1
    legal_time = 1
    limit_job_one_day_minutes = 1
    limit_job_one_month_minutes = 1
    limit_job_one_year_minutes = 1
    limit_legal_one_day_minutes = 1
    limit_legal_one_month_minutes = 1
    limit_legal_one_year_minutes = 1
    lng = 1
    local_government_code = 1
    lunch_name = 1
    mail_address = 1
    message = 1
    my_number = 1
    need_to_exceed = 1
    notice_number = 1
    notification = 1
    notification_display_date_from = 1
    notification_display_date_to = 1
    notification_transmission_date = 1
    number_of_legal_holidays_allowed_to_work = 1
    number_of_working_days_per_week = 1
    office_code = 1
    office_name = 1
    other = 1
    overtime_content = 1
    overtime_reason = 1
    payment_date = 1
    payment_days = 1
    payment_times = 1
    pension_fund_contributions_date = 1
    place_code = 1
    place_name = 1
    post_code = 1
    postal_code = 1
    price = 1
    procedure_of_exceed_the_time_limit = 1
    purchase_date = 1
    quantity = 1
    reasons_over_work_contents = 1
    reason_for_retirement = 1
    reference_number = 1
    role_code = 1
    role_name = 1
    rounding_term = 1
    rounding_term_over_work = 1
    route_code = 1
    route_name = 1
    salary_closing_name = 1
    salary_closing = 1
    salary_item_name = 1
    social_insurance_date = 1
    sort_number = 1
    special_provisions_rate_month = 1
    special_provisions_rate_year = 1
    special_provisions_year_count = 1
    specific_content = 1
    start_date = 1
    start_section = 1
    start_time = 1
    supplier_name = 1
    target_date = 1
    task_name = 1
    team_code = 1
    team_name = 1
    tel = 1
    term_from = 1
    term_to = 1
    time = 1
    town = 1
    transfer_amount_of_money = 1
    transportation_name = 1
    unit_price = 1
    unit_price2 = 1
    work_schedule_code = 1
    work_schedule_name = 1
    working_system_abbreviation = 1
    abbreviated_name = 1
    address_change_supplement = 1
    age = 1
    agreement_date = 1
    bonus_pay_slip_name = 1
    choice_screen_code = 1
    commuting_route_change_supplement = 1
    contents2 = 1
    field_name = 1
    filing_date = 1
    icon_name = 1
    inoculation_venue = 1
    keyword = 1
    label_name = 1
    limit_legal_one_weeks_minutes = 1
    menu_code = 1
    number_of_inoculations = 1
    personal_information_change_supplement = 1
    release_version = 1
    screen_name = 1
    serial_number = 1
    skill = 1
    starting_date = 1
    vue_path = 1
    working_interval = 1
    limit_exemption_working_interval = 1
    api = 1
    help1 = 1
    help2 = 1
    help3 = 1
    help4 = 1
    help5 = 1
    help6 = 1
    help7 = 1
    help8 = 1
    help9 = 1
    help10 = 1
    help11 = 1
    help12 = 1
    help13 = 1
    help14 = 1
    help15 = 1
    message_id = 1
    correspondence_action = 1
    recruitment_category_name = 1
    meter = 1
    job_holiday_comment = 1
    report_name = 1
    shift_pattern_name = 1
    highlight_employees = 1
    csv_template_name = 1
    designated_number = 1
    addressee_number = 1
    resident_municipality_code = 1
    beneficiary_number = 1
    resident_tax_jun = 1
    resident_tax_jly = 1
    resident_tax_aug = 1
    resident_tax_sep = 1
    resident_tax_oct = 1
    resident_tax_nov = 1
    resident_tax_dec = 1
    resident_tax_jan = 1
    resident_tax_feb = 1
    resident_tax_mar = 1
    resident_tax_apl = 1
    resident_tax_may = 1
    remarks_others = 1


"""
Enum:Vue側のラベル管理
"""


class VueHelp(IntEnum):
    work_schedule_code = 1
    work_time = 1
    is_job_before_start_time = 1
    break_time = 1
    closing_name = 1
    target_year = 1
    office_code = 1
    reference_number = 1
    special_measures = 1
    employee_code = 1


"""
Enum:Vue側のラベル管理
"""


class VueMovie(IntEnum):
    boss = 1


"""
Enum:出退勤区分
JOB_START            出勤打刻
JOB_FINISH           退勤打刻
"""


class AttendanceType(IntEnum):
    JOB_START = 1
    JOB_FINISH = 2


"""
Enum:前後区分
BEFORE 前
AFTER 後
"""


class BeforeAfterFlag(IntEnum):
    BEFORE = 1
    AFTER = 2


class ReportTitle(IntEnum):
    # REPORT_01_002_001 = 1
    # REPORT_01_004_001 = 1
    # REPORT_01_004_002 = 1
    # REPORT_01_007_001 = 1
    REPORT_02_003_001 = 1
    # REPORT_02_003_002 = 1
    # REPORT_02_003_003 = 1
    # REPORT_02_003_004 = 1
    # REPORT_02_003_005 = 1
    REPORT_02_003_006 = 1
    # REPORT_02_003_007 = 1
    # REPORT_02_004_001 = 1
    # REPORT_02_004_002 = 1
    # REPORT_02_005_001 = 1
    # REPORT_02_100_001 = 1
    # REPORT_02_100_002 = 1
    # REPORT_03_005_001 = 1
    # REPORT_03_005_002 = 1
    # REPORT_03_035_001 = 1
    # REPORT_06_003_001 = 1
    # REPORT_07_002_001 = 1
    # REPORT_07_003_001 = 1
    # REPORT_07_004_001 = 1
    # REPORT_07_005_001 = 1
    # REPORT_07_005_002 = 1
    # REPORT_07_006_001 = 1
    # REPORT_07_007_001 = 1
    # REPORT_07_008_001 = 1
    # REPORT_07_009_001 = 1
    # REPORT_07_010_001 = 1
    # REPORT_07_011_001 = 1
    # REPORT_08_001_001 = 1
    # REPORT_08_002_001 = 1
    # REPORT_08_002_002 = 1
    # REPORT_08_003_001 = 1
    # REPORT_08_004_001 = 1
    # REPORT_08_005_001 = 1
    # REPORT_12_002_001 = 1
