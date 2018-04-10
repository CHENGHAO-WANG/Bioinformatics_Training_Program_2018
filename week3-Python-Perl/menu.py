
# coding: utf-8

import os

os.chdir('/Users/wangchenghao/Desktop/weekly_tasks/original_dirs')

u=sorted([x for x in os.walk('/Users/wangchenghao/Desktop/weekly_tasks/original_dirs')],key=lambda p: p[0],reverse = True )

t=0
for uu in u:
    for i in uu[1]:
        s="%02d" % t
        ww="{}/{}".format(uu[0], i)
        w="{}-{}".format(s, i)
        w="{}/{}".format(uu[0], w)
        os.rename(ww, w)
        t+=1
    t=0

