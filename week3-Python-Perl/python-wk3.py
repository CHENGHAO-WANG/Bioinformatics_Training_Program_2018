# coding: utf-8

import numpy as np
import pandas as pd
import re

#读取文件
data = pd.read_csv('test.txt', sep="\t", header=None)

##获得id包含ENST的行的索引
col1=list(data[1])
j=0
g=[]
for kind in col1:
    if re.match(r'ENST*',kind):
        g.append(j)
    j=j+1

dfg = pd.DataFrame(columns=[0,1,2])#生成空的dataframe
k=0
#将结果保存到dataframe中
for x in g:
    dfg.loc[k]=list(data.loc[x])
    k+=1

#导出成txt文件
np.savetxt('test2.txt', dfg.values, fmt='%s', delimiter="\t", header="'0'\t'1'\t'2'") 

#获得表达量的最值和平均值
exp=dfg[2]  #提取表达量所在那一列
dfe = pd.DataFrame(columns=['celltype','id','maximum','mean'])
k=0
#将结果保存到dataframe中
for e in exp:
    ei=np.array(e.split(','),dtype='int32')
    maximum=np.max(ei)
    mean=np.mean(ei)
    dfe.loc[k]=[dfg.at[k,0],dfg.at[k,1],str(maximum),str(mean)]
    k+=1

#导出成txt文件
np.savetxt('test3.txt', dfe.values, fmt='%s', delimiter="\t", header="'celltype'\t'id'\t'maximum'\t'mean'") 

