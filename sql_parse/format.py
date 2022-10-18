import sqlparse
from enum import Enum


class Keyword_case(Enum):
    """ 关键字大小写 """
    lower = 'lower'
    upper = 'upper'
    capitalize = 'capitalize'


class Identifier_case(Enum):
    """ 标识符大小写 """
    lower = 'lower'
    upper = 'upper'
    capitalize = 'capitalize'


def format_sql(sql, keyword_case: Keyword_case = Keyword_case.upper,
               identifier_case: Identifier_case = Identifier_case.upper, strip_comments: bool = True,
               indent_width: int = 4, use_space_around_operators: bool = True, indent_tabs: bool = True) -> str:
    """ 格式化 SQL """
    return sqlparse.format(sql, reindent=True, keyword_case=keyword_case, identifier_case=identifier_case,
                           strip_comments=strip_comments, indent_width=indent_width,
                           use_space_around_operators=use_space_around_operators, indent_tabs=indent_tabs)


def split_sql(sql: str) -> list[str]:
    """ 拆分 SQL """
    return sqlparse.split(sql)


__all__ = ['format_sql', 'split_sql', 'Keyword_case', 'Identifier_case']
