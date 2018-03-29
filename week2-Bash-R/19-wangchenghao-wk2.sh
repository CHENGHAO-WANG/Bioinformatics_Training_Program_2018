#!/bin/bash

#让awk读入文件时只按照tab来做separator
cat filename | awk 'BEGIN {FS="\t"} $1 == "IV" {print $5-$4+1 "\t" $7}'
#cat为读取文件的操作，filename为文件名；可以替换成任何读取文件的命令，如grep，head，tail等命令都可以通过管道连接awk命令
#BEGIN设定从第一行开始执行separate操作
#FS表示分隔符号，默认为tab和空格；
#$1 == "IV" 是一个判断选项；这里表示判断第一个字段是否为“IV”，只保留符合条件的行；这里可以写其他的判断语句，也可以不写
# {print }表示输出目的字段；字段之间可以进行运算，也可以输出时插入字符
#awk后面可以连接多对条件判断和动作的指令

#如果不写BEGIN，第一行就不会按照FS所设定的分隔符号进行分隔
cat filename | awk '{FS="\t"} $1 == "IV" {print $5-$4+1 "\t" $7}'
