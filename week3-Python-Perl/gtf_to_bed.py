
# coding: utf-8

import gtfparse as gp
import os
import pandas as pd
from tqdm import tqdm
import numpy as np


#读取gtf文件为dataframe
df1 = gp.read_gtf("/Users/wangchenghao/Desktop/weekly_tasks/gene.gtf")

#求得gtf文件的行和列的数目
n=len(df1)
m=df1.shape[1]

df = pd.DataFrame(columns=list(range(m)))
df2 = pd.DataFrame(columns=list(range(12))) #生成空的dataframe

#挑出gene_id相同的行，以获取其exon的count和start的信息
j=0
a=[]
k=0
b=[]
count=0
c=[]
for i in tqdm(range(n)):
    if df1.at[i,'transcript_id']:
        a.append(df1.at[i,'transcript_id'])
        if j==0:
            df.loc[0]=list(df1.loc[i])
        else:
            if a[-1]==a[-2]:
                df.loc[j]=list(df1.loc[i])
            else:
                a=[]
                a.append(df1.at[i,'transcript_id'])
                #输出exon的count和start的信息
                for t in range(1,j):
                    if df.at[t,2]=='exon':
                        count+=1
                        size=df.at[t,4]-df.at[t,3]
                        b.append(size)
                        begin=df.at[t,3]-df.at[0,3]
                        c.append(begin)
                        
                df2.at[k,9]=count
                df2.at[k,10]=b
                df2.at[k,11]=c
                # 输出gtf中的其他信息
                df2.at[k,0]=df.at[0,0]
                df2.at[k,1]=df.at[0,3]
                df2.at[k,2]=df.at[0,4]
                df2.at[k,3]=df.at[0,14].split('.')[0]
                df2.at[k,5]=df.at[0,6]
                
                df=pd.DataFrame(columns=list(range(m)))
                df.loc[0]=list(df1.loc[i])
                j=0
                k+=1
                b=[]
                c=[]
                
        j+=1
 
#设定5，7，8，9列为0
df2[[4,6,7,8]]=0

df2=df2.sort_values(by=[3,0])

#保存结果
np.savetxt('bed.txt', df2.values, fmt='%s', delimiter="\t") 

