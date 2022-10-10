from itertools import permutations


def permutation(str_list: list[str | int]) -> list[tuple[str | int]]:
    """ 找到数组的全部排序方式 返回列表元组 """
    temp = []
    for i in range(1, len(str_list) + 1):
        arr = permutations(str_list, i)
        temp += arr
    return temp


def permutation_to_str_list(str_list: list[str]) -> list[str]:
    """ 找到数组的全部排序方式 返回列表字符串 """
    return [''.join(item) for item in permutation(str_list)]


def create_pwd(path: str, file_name: str, file_type: str, content: str) -> None:
    """ 根据指定内容生成密码本 """
    content_list = permutation(list(content))
    with open(f'{path}/{file_name}.{file_type}', 'w', encoding='utf-8') as f:
        for item in content_list:
            f.write(item)
