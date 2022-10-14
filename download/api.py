from os import system


def download(url: str) -> int:
    """ 下载 """
    return system(f'you-get {url}')


def download_path(url: str, path: str = './', file_name: str = 'music') -> int:
    """ 下载 并且自定义名字和路径 """
    return system(f'you-get -o {path} -O {file_name} {url}')


__all__ = ['download', 'download_path']
