from sql_faker.prizes import one_value_prizes, zero_to_one_prizes


def value_and_null(value: int | str, probability: float) -> None | str:
    """ 设置返回 value 的概率，0~1之间的浮点数，根据概率返回 None 还是 值 """
    number = zero_to_one_prizes()
    print(number)
    return value if number >= probability else None


def range_data(func, number: int, *args) -> 'func':
    """ 传入一个方法，然后使用这个方法生成几个值，返回一个函数，功能：在这几个值中随机返回内容 """
    data_array = [func(*args) for _ in range(number)]

    def func() -> str:
        return one_value_prizes(data_array)

    return func


def decorator_func(func, *args):
    """ 包装刷数据方法以便 字典模板生成不同数据可以使用 """

    def t():
        return func(args) if len(args) != 0 else func()

    return t


def decorator_func_sugar(template: dict) -> dict[str, str | int]:
    """ 全部都使用默认值的情况下的语法糖 不需要自己一个个用 decorator_func 包装 """
    data = {}
    for key, value in template.items():
        data[key] = decorator_func(value)
    return data


def decorator_func_sugar_params(template: dict, **kwargs) -> dict[str, str | int]:
    """ 在 decorator_func_sugar 基础上支持 key=value 方式添加参数，value 必须是 decorator_func 包装后返回的函数"""
    data = decorator_func_sugar(template)
    for key, value in kwargs.items():
        data[key] = value
    return data


def build(template: dict[str, decorator_func]) -> dict[str, str | int]:
    """ 使用模板生成假数据 """
    data = {}
    for key, value in template.items():
        data[key] = value()
    return data
