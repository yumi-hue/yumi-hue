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
