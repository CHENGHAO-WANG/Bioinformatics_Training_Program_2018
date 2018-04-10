#用heatmap.2绘制heatmap

#安装gplots
#切换工作目录

library(gplots)

#读取数据
rt <- read.table("R.heatmap.txt", head=TRUE) #行名和列名会被自动区分出来
dat <- data.matrix(rt)
#若列名不能被区分，可以用rownames(matrix)<-rt[,1]来设定，这时矩阵需要从数据第二列开始读

#加入聚类命令
d1<- dist(dat,method="euclidean")
hc1<-hclust(d1)
rowc<-hc1$order
d2<- dist(t(dat),method="euclidean")
hc2<-hclust(d2)
colc<-hc2$order
dat2<-dat[rowc,colc]

#绘制heatmap
#设定颜色
my_color <- colorRampPalette(c("#c51b8a","#fa9fb5","#fde0dd"))(n=19)
#可以用英文设定颜色，也可以用hex码设定颜色；n表示渐变颜色数量

#设定生成的图像大小
png("~/Desktop/training program homework/plotHeatmap/heatmap8.png",
    width=5*300,height=5*300,res=300,pointsize=5)
#生成png图像；宽度和高度为1500像素，分辨率为300像素/英寸；字体大小为5


#生成图像
heatmap.2(dat2, main="my_heatmap",  #输入数据必须为matrix；main设定title；
          #cellnote=dat, notecol="black", #让每一个spot显示数值；设定数值显示的字体颜色
          density.info = "none", #不在color-key上显示value的分布曲线或直方图
          trace="none", #不在heatmap上显示沿行或沿列的value分布曲线或直方图
          margins=c(9,12), #设定图像周围的空白大小；默认c(5,5)
          col=my_color, #设定颜色
          dendrogram = "row",Colv="NA" #只设定行上有树状图，取消列的树状图
          #Colv = as.dendrogram(cluster)), #对行变量做聚类
          #RowSideColors = c(rep("gray",5),rep("green",3)), 
          #给行变量分组做labels；第一组为灰色，包含前5个；
          )

#给行变量分组labels做color legend
#par(lend = 2) #设定color legend 边框为矩形
#legend("topright",      # location of the legend on the heatmap plot
#legend = c("type I", "type II"), # category labels
#col = c("gray", "green"),  # color key
#lty= 1,             # line style
#lwd = 10            # line width
#)



dev.off()#写在最后；不写上就不会生成图像
