from sql_parse.inquire.dbconnect import SqlServer


def get_all_database(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部数据库 """
    sql = "SELECT NAME FROM MASTER.DBO.SYSDATABASES ORDER BY NAME"
    return [i[0] for i in sqlserver.connect().execute(sql).fetchall()]


def get_object(sqlserver: SqlServer, xtype: str) -> str:
    """ 获取 sqlserver 数据库中对象的定义 """
    sql = f"SELECT OBJECT_DEFINITION(OBJECT_ID('{object_name}'))"
    return sqlserver.connect().execute(sql).fetchone()[0]


def get_all_table(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部表 """
    sql = f"SELECT NAME FROM SYSOBJECTS WHERE XTYPE='U' ORDER BY NAME"
    return [i[0] for i in sqlserver.connect().execute(sql).fetchall()]


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
    sql = "SELECT NAME FROM SYSOBJECTS WHERE XTYPE='V' ORDER BY NAME"
    return [i[0] for i in sqlserver.connect().execute(sql).fetchall()]


def get_all_function(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部函数 """
    sql = "SELECT NAME FROM SYSOBJECTS WHERE XTYPE='FN' ORDER BY NAME"
    return [i[0] for i in sqlserver.connect().execute(sql).fetchall()]
