# -*- coding:utf-8 -*-
Words = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z', ' ', '-', "'"}

#将文件中的大写英文字母转换为小写，并把所有小写字母，空格，横线，‘输出到字符串result中
def tostr(file):
    result = ''
    for n in file.lower():
        if n in Words:
            result += n
    return result

#对字符串分割撑的list进行计数，以字典的形式输出，key为单词，value为出现次数
def make_dict(strings):
    strings = tostr(strings)
    words = strings.split()#用“，”对字符串分割，并以list的形式输出到words中
    R = {}
    for w in words:
        if w in R:
            R[w] += 1
        else:
            R[w]=1 #某个单词第一次出现时，value默认为1
    return R
#对字符串的各种数值进行统计
def file_count(fname,path):

    file_strings = open(fname,'r').read()#读取文件，输出为字符串
    num_chars = len(file_strings)#计算字符串长度
    num_lines = file_strings.count('\n')#计算行数
    d = make_dict(file_strings)#输出单词统计字典
    num_words = sum(d[w] for w in d) ## 输出的字典包含多少个单词（key）

    lst = [(d[w],w) for w in d]
    lst.sort()#对list进行排序
    lst.reverse()#对list元素进行反排序

    print("This file '%s' has: " % fname)
    print('   %s characters' % num_chars)
    print('   %s lines'% num_lines)
    print('   %s words'% num_words)
    print('\nThe top 10 most frequent words are: ')
    i = 1
    for count,word in lst[0:10]:
        print('%2s. %4s %s' % (i,count,word))
        i += 1

def main():
    file_count('test1.txt','F:\test1.txt')
if __name__ == '__main__':
    main()
