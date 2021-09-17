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
# 计算过滤后数据的余弦相似度
def sim(text1, text2):
    texts = [text1, text2]
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    article = dictionary.doc2bow(text1)
    cos = similarity[article][1]
    return cos
