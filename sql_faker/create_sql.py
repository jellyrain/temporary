def insert(table_name: str, data: dict[str, str | int]) -> str:
    """ 根据 data 生成 insert sql语句 """
    column = ','.join(data.keys())
    value = ','.join([str(item) if type(item) == int else f"'{item}'" for item in data.values()])
    return f'insert into {table_name}({column}) values({value});'


def insert_all(number: int, table_name: str, data: dict[str, str | int]) -> str:
    """ 一次性创建 number 条的 insert 语句 """
    return ';'.join([insert(table_name, data) for _ in range(number)])


def update(table_name: str, set_data: dict[str, str | int], where_data: dict[str, str | int] = {}) -> str:
    """ 根据 set_data 和 where_data 生成 update sql语句 """
    set_string = ", ".join([f"{key} = '{value}'" for key, value in set_data.items()]).strip()
    where_string = " and ".join([f"{key} = '{value}'" for key, value in where_data.items()])

    return f'update {table_name} set {set_string}{"" if where_string == "" else " where " + where_string};'