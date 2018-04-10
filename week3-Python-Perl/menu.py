
# coding: utf-8

import os

#切换到目录
os.chdir('/Users/wangchenghao/Desktop/weekly_tasks/original_dirs')

##思路：利用os.walk遍历文件，将得到的文件夹名修改，再与文件夹所在的绝对路径相连，利用得到的新路径进行重命名
##出现问题：只能对最短的路径下的文件夹重命名，剩下的文件夹因为在遍历过程中路径发生改变而无法完成遍历
##改进思路：根据绝对路径的长短，将os.walk得到的生成器的顺序颠倒；从而先修改最长路径下的文件夹名，这样就不会妨碍剩余的遍历过程

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

