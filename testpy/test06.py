# -*- coding:utf-8 -*-


#对字符串分割的list进行计数，以字典的形式输出，key为单词，value为出现次数
def make_dict(file):
    file = file.lower()
    file = file.replace(',', ' ')
    file = file.replace('.', ' ')
    file = file.replace('!', ' ')
    file = file.replace('?', ' ')
    words = file.split()#用“，”对字符串分割，并以list的形式输出到words中
    R = {}
    for w in words:
        if w in R:
            R[w] += 1
        else:
            R[w]=1 #某个单词第一次出现时，value默认为1
    return R
#读取文件，并先输出为字符串，再调用make_dict方法输出为list，再输出为字典
def file_count(fname):
    file = open(fname,'r').read()#读取文件，输出为字符串
    d = make_dict(file)#输出单词统计字典
    lst = [(d[w]) for w in d]
    lst.sort()#对list进行排序
    lst.reverse()#对list元素进行反排序
    print('\nThe most frequent word is: ')
    for k in d:
        if d[k]==lst[0]:  #反排序之后，索引为0的位置的元素即是出现次数最多的元素
            print k
    print ('The number is:')
    print(lst[0])

def main():
    file_count('test1.txt')
if __name__ == '__main__':
    main()
