### 下面列出文件名与对应的作业要求

##### python-wk3.py
打开Bioinformatics_Training_Program_2018/week3-Python-Perl/test.txt文件，找出mRNA所在的行（id包含ENST）；
找出每条mRNA的最大表达值，以及表达平均值

##### gtf_to_bed.py
write a Python program to convert a GTF file to BED12 format
Please refer to (https://genome.ucsc.edu/FAQ/FAQformat.html#format1) for BED12 format and refer to (https://www.ensembl.org/info/website/upload/gff.html) for GTF format. 
The GTF file is weekly_tasks/gencode.v27.long_noncoding_RNAs.gtf.
Each line in the output file is a transcript with the 4th columns as transcript ID
The version number of the transcript ID should be stripped (e.g. ENST00000473358.1 => ENST00000473358).
The output file is sorted first by transcript IDs and then by chromosome in lexicographical order.
Column 5, 7, 8, 9 in the BED12 file should be set to 0.
Please do NOT use any external tools (e.g. sort, awk, etc.) in your program other than Python.
An example output can be found in weekly_tasks/transcripts.bed.

##### menu.py
write a Python program to add a prefix to all directories
Each prefix is a two-digit number starting from 00 and '-'. If the number is less than 10, a single '0' letter should be filled.
