# -*- coding:utf-8 -*-
import io
import re

class Counter:
  def __init__(self, path):
     self.mapping = dict()
     with open(path,encoding="utf-8") as file:
         data=file.read()
         words= [s.lower() for s in re.findall("\w+", data)]
         for word in words:
             self.mapping[word]=self.mapping.get(word,0)+1
             def most_appear(self,n):
                 assert n>0,"n should be large than 0"
                 return sorted(self.mapping.items(), key=lambda item: item[1], reverse=True)[:n]
 if __name__=='__main__':
     most_appear_5 = Counter("F:\123.txt").most_appear(5)
     for item in most_appear_5:
         print (item)




