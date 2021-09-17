import jieba
import gensim
import re
import os


# 获取文件的内容
def file(path):
    string = ''
    get_file = open(path, 'r', encoding='UTF-8')
    line = get_file.readline()
    while line:
        string = string + line
        line = get_file.readline()
    get_file.close()
    return string


# 过滤特殊符号，然后进行结巴分词
def filter(string):
    pattern = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")
    string = pattern.sub("", string)
    result = jieba.lcut(string)
    return result
