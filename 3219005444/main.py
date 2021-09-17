import jieba
import gensim
import re
import os
import sys

path1 = sys.argv[1]
path2 = sys.argv[2]
path3 = sys.argv[3]
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
def part(string):
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

def count():
    str1 = file(path1)
    str2 = file(path2)
    text1 = part(str1)
    text2 = part(str2)
    if not os.path.exists(path1) :
        print("论文原文文件不存在！")
        exit()
    if not os.path.exists(path2):
        print("抄袭版论文文件不存在！")
        exit()

    similarity = sim(text1, text2)
    result=round(similarity.item(),2)  #取小数点后两位
    return result


if __name__ == '__main__':
    result = count()
    print("文章相似度： %.4f" % result)
    f = open(path3, 'w', encoding="utf-8")
    f.write("文章相似度： %.4f"%result)
    f.close()
