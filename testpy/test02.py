# -*- coding: UTF-8 -*-
import pprint

str01='从前，从前，有个人爱你很久'
count = {}
for i in str01:
    count[i]=count.setdefault(i,0)
    count[i] +=1
#pprint.pprint(count)
for k, v in count.items():
    print (k+':'+str(v))


