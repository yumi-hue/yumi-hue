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
def count():
    path1 = input("输入论文原文的文件的绝对路径：")
    path2 = input("输入抄袭版论文的文件的绝对路径：")
    if not os.path.exists(path1) :
        print("论文原文文件不存在！")
        exit()
    if not os.path.exists(path2):
        print("抄袭版论文文件不存在！")
        exit()
    str1 = file(path1)
    str2 = file(path2)
    text1 = filter(str1)
    text2 = filter(str2)
    similarity = calc_similarity(text1, text2)   #生成的similarity变量类型为<class 'numpy.float32'>
    result=round(similarity.item(),2)  #借助similarity.item()转化为<class 'float'>，然后再取小数点后两位
    return result


if __name__ == '__main__':
    result = count()
    save_path = input("输入指定文件路径: ")
    print("文章相似度： %.4f" % result)
    #将相似度结果写入指定文件
    f = open(save_path, 'w', encoding="utf-8")
    f.write("文章相似度： %.4f"%result)
    f.close()
