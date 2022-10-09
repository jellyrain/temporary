def select(table_name: str, where_data: dict[str, str | int] = {}, group_data: list[str] | str = [],
           having_data: dict[str, str | int] = {}, order_data: list[str] | str = [], column: list[str] | str = '*') -> str:
    if type(group_data) == str:
        group_data = [group_data]
    if type(order_data) == str:
        order_data = [order_data]
    if type(column) == str:
        column = [column]

    where_data = " and ".join([f"{key} = '{value}'" for key, value in where_data.items()])
    group_data = ", ".join(group_data)
    having_data = " and ".join([f"{key} = '{value}'" for key, value in having_data.items()])
    order_data = ", ".join(order_data)
    column = ", ".join(column).strip()

    return f'select {column} from {table_name}{"" if where_data == "" else " where " + where_data}{"" if group_data == "" else " group by " + group_data}{"" if having_data == "" else " having " + having_data}{"" if order_data == "" else " order by " + order_data};'


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


def delete(table_name: str, where_data: dict[str, str | int] = {}) -> str:
    """ 根据 where_data 生成 delete sql 语句 """
    where_string = " and ".join([f"{key} = '{value}'" for key, value in where_data.items()])
    return f'delete from {table_name}{"" if where_string == "" else " where " + where_string};'
