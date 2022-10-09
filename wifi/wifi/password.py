def permutation(s: list[str]) -> list[str]:
    if len(s) <= 1:
        return [s]
    else:
        temp_list = []
        for i in range(len(s)):  # 遍历字符串 s 中的每个字符
            for j in permutation(s[0:i] + s[i + 1:]):  # 把除了s[i]字符以外的字符组成字符串然后让它迭代
                temp_list.append(s[i] + ''.join(j))
        return temp_list


def create_pwd(path: str, file_name: str, file_type: str, content: str) -> None:
    """ 根据指定内容生成密码本 """
    content_list = permutation(list(content))
    with open(f'{path}/{file_name}.{file_type}', 'w', encoding='utf-8') as f:
        for item in content_list:
            f.write(item)
