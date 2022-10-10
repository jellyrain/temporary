import re
from copy import deepcopy
from os import system, popen


def decorator_cmd(cmd: str):
    """ 包装刷数据方法以便 字典模板生成不同数据可以使用 """
    def t():
        return system(cmd)

    return t


def audio(url: str, path: str = './', file_name: str = 'music') -> int:
    """ 下载音频 """
    return system(f'you-get -o {path} -O {file_name} {url}')


def get_video_quality(url: str) -> str:
    """ 获取视频能下载的画质 """
    po = popen(f'you-get -i {url}')
    return po.buffer.read().decode('utf-8')


def str_json(context: str, url: str) -> dict:
    """ get_video_quality 获取到的字符串转 字典 """
    url_data = {}
    video_dict = {}
    video_type = ''

    def parse(line_str: str) -> None:
        global video_type
        if line_str.startswith(' '):
            regexp_result = re.findall('\[ (.*?) \]', line_str)
            if regexp_result:
                video_type = regexp_result[0]
                url_data[video_type] = []
            else:
                boolean = '#' in line_str
                line_str = line_str.replace('- format', 'format').replace('#', '')
                key, value = line_str.split(':')
                if boolean:
                    video_dict[key.strip()] = decorator_cmd(value.replace('#', '').replace('[URL]', url).strip())
                    url_data[video_type].append(deepcopy(video_dict))
                else:
                    video_dict[key.strip()] = value.replace('#', '').strip()
        else:
            if not len(line_str.strip()) == 0:
                key, value = line_str.split(':')
                url_data[key.strip()] = value.replace('#', '').strip()

    for line in context.split('\n'):
        parse(line)

    return url_data


def get_video(url: str) -> dict:
    """ get_video_quality 和 str_json 一起的语法糖 """
    return str_json(get_video_quality(url), url)
