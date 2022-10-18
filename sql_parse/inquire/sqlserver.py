from sql_parse.inquire.dbconnect import SqlServer


def get_all_database(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部数据库 """
    sql = "SELECT NAME FROM MASTER.DBO.SYSDATABASES ORDER BY NAME"
    return [i[0] for i in sqlserver.connect().execute(sql).fetchall()]


def get_object(sqlserver: SqlServer, xtype: str) -> str:
    """ 获取 sqlserver 数据库中对象的定义 """
    sql = f"SELECT NAME FROM SYSOBJECTS WHERE XTYPE='{xtype}' ORDER BY NAME"
    return [item[0] for item in sqlserver.connect().execute(sql).fetchall()]


def get_all_table(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部表 """
    return get_object(sqlserver, "U")


def get_column_table(sqlserver: SqlServer, table_name: str) -> list[dict[str, str]]:
    """ 获取 sqlserver 数据库中表的字段 """
    sql = f"SELECT COLUMN_NAME, ORDINAL_POSITION, IS_NULLABLE, DATA_TYPE, CHARACTER_OCTET_LENGTH FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'"
    return [{
        "column_name": i[0],
        "ordinal_position": i[1],
        "is_nullable": i[2],
        "data_type": i[3],
        "character_octet_length": i[4]
    } for i in sqlserver.connect().execute(sql).fetchall()]


def get_pk_table(sqlserver: SqlServer, table_name: str) -> list[str]:
    """ 获取 sqlserver 数据库中表的主键 """
    sql = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE TABLE_NAME = '{table_name}'"
    return [i[0] for i in sqlserver.connect().execute(sql).fetchall()]


def get_all_view(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部视图 """
    return get_object(sqlserver, "V")


def get_all_function(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部函数 """
    return get_object(sqlserver, "FN") + get_object(sqlserver, "IF") + get_object(sqlserver, "TF")


def get_all_user(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部用户 """
    sql = "SELECT NAME FROM SYSUSERS"
    return [i[0] for i in sqlserver.connect().execute(sql).fetchall()]


def get_all_role(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部角色 """
    sql = "SELECT NAME FROM SYSROLES"
    return [i[0] for i in sqlserver.connect().execute(sql).fetchall()]


def get_all_procedure(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部存储过程 """
    return get_object(sqlserver, "P")


def get_all_trigger(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部触发器 """
    return get_object(sqlserver, "TR")


def get_all_index(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部索引 """
    return get_object(sqlserver, "IN")


def get_all_synonym(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部同义词 """
    return get_object(sqlserver, "SN")


def get_all_sequence(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部序列 """
    return get_object(sqlserver, "SQ")


# 获取 sql server 一张表的 ddl 语句
def get_table_ddl(sqlserver: SqlServer, table_name: str) -> str:
    sql = f"SELECT OBJECT_DEFINITION(OBJECT_ID('{table_name}'))"
    return sqlserver.connect().execute(sql).fetchone()[0]
