#!/bin/bash
#思路：把file1-file5的md5码输出到文件中，用文件比较命令来比较

#首先切换到file1-file5和md5sum.txt所在目录下

#将file1-file5的md5码依次记录到txt文件中
md5sum -t file1 > md5test.txt
md5sum -t file2 >> md5test.txt
md5sum -t file3 >> md5test.txt
md5sum -t file4 >> md5test.txt
md5sum -t file5 >> md5test.txt
#md5sum 产生md5码；-t表示以文本类型来读取
# >表示传入到文件中，覆盖原有内容；若文件不存在则会被创建； >>表示传入文件中原先内容的后面

cat md5test.txt | awk '{print $1}' > md5test1.txt
#只保留第一列；因为第二列是文件名，不去掉的话会不利于接下来的比较

#读取md5sum.txt的第四列，即md5码所在的那一列，并与md5test.txt进行比较
head -n 5 md5sum.txt | awk '{print $4}' | diff - md5test1.txt
#diff表示按行进行文件比较；- 表示管道之前的STANDOUT 
#期望输出为 4c4 ；表示左边文件的第四行被右边文件的第四行所替换；说明 file4 is truncated
