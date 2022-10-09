from faker import Faker

faker_en = Faker()
faker_zh = Faker('zh_CN')


def is_chinese(chinese: bool) -> Faker:
    """ 是否使用刷的数据是中文 """
    return faker_zh if chinese else faker_en


def name(chinese: bool = True) -> str:
    """ 姓名 """
    return is_chinese(chinese).name()


def name_male(chinese: bool = True) -> str:
    """ 姓名（男） """
    return is_chinese(chinese).name_male()


def name_female(chinese: bool = True) -> str:
    """ 姓名（女） """
    return is_chinese(chinese).name_female()


def msisdn() -> str:
    """ 完整手机号码(加了国家和国内区号) """
    return faker_en.msisdn()


def phone() -> str:
    """ 手机号 """
    return faker_en.phone_number()


def profile(chinese: bool = True) -> dict:
    """ 档案(完整) """
    return is_chinese(chinese).profile()


def simple_profile(chinese: bool = True) -> dict:
    """ 档案(简单) """
    return is_chinese(chinese).simple_profile()


def boolean() -> bool:
    """ 布尔值 """
    return faker_en.pybool()


def ssn(min_age: int = 18, max_age: int = 90) -> str:
    """ 身份证 """
    return faker_zh.ssn(min_age, max_age)


def uuid4() -> str:
    """ uuid4 """
    return faker_en.uuid4()


def job(chinese: bool = True) -> dict:
    """ 职位 """
    return is_chinese(chinese).job()


def email() -> str:
    """ 邮箱 """
    return faker_en.safe_email()


def mac_address() -> str:
    """ mac地址 """
    return faker_en.mac_address()


def ipv4() -> str:
    """ ipv4 """
    return faker_en.ipv4()


def date(pattern: str = "%Y-%m-%d", end_datetime: str = None) -> str:
    """ 日期字符串 """
    return faker_en.date(pattern, end_datetime)


def date_of_birth(tzinfo: str | None = None, minimum_age: int = 0, maximum_age: int = 115):
    """ 出生日期 """
    return faker_en.date_of_birth(tzinfo, minimum_age, maximum_age)


def company(chinese: bool = True) -> str:
    """ 公司名称 """
    return is_chinese(chinese).company()


def address(chinese: bool = True) -> str:
    """ 地址 """
    return is_chinese(chinese).address()


def postcode(chinese: bool = True) -> str:
    """ 获取邮编 """
    return is_chinese(chinese).postcode()


def license_plate(chinese: bool = True) -> str:
    """ 获取车牌照 """
    return is_chinese(chinese).license_plate()


def color() -> dict:
    """ 返回一个对象，返回不同颜色的生成方法 """
    faker = faker_en
    return {
        'color_name': faker.license_plate,
        'hex_color': faker.hex_color,
        'rgb_color': faker.rgb_color,
        'rgb_css_color': faker.rgb_css_color,
        'safe_color_name': faker.safe_color_name,
        'safe_hex_color': faker.safe_hex_color
    }


def md5(raw_output: bool = False) -> str:
    """ 随机生成 md5 值 """
    return faker_en.md5(raw_output)
