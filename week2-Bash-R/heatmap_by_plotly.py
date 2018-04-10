#用plotly绘制heatmap

#安装plotly
#切换工作目录

library(plotly)
#需要在plotly官网注册；点击个人账户>settings>API keys 设置API key
Sys.setenv("plotly_username"="CHENGHAO-WANG")
Sys.setenv("plotly_api_key"="og1fMZw6XXtHrw4MG3GR")


#读取数据
dat <- read.table("~/Desktop/training program homework/plotHeatmap/R.heatmap.txt", head=TRUE) 
#行名和列名会被自动区分出来
library(scales)
dat <-apply(dat,2,rescale) #以列为基准对数据进行变换，使每一行都变成［0,1］之间的数字。
hp <-plot_ly(z=data.matrix(dat), x=colnames(dat), y=rownames(dat), 
             #输入的数据类型需要是dataframe格式，但这样有可能出错；上一行的代码就是一种替代方案
             type='heatmap',
             alpha=1, #设定透明度（0～1），默认为1
             colors = colorRampPalette(c('#ffffd9','#edf8b1','#c7e9b4','#7fcdbb','#41b6c4','#1d91c0','#225ea8','#253494','#081d58'))(n=9),
             #colorscale='Greys', #用colorscale生成颜色；自定义colorscale的方式见最后
             width=1200,
             height=2000 #设定图片的宽度和高度，单位为像素
           
        )
hp<-layout(hp,  title='Heatmap by plotly') #设置标题
api_create(hp, filename = "heatmap14") #图片保存到你的plotly个人中心；图片的命名如果重复，会覆盖旧图
hp

##自定义colorscale的方式
### R语言没有多行注释，写一个永远为假的if语句是一个不错的替代
if (1>10) {
  vals <- unique(scales::rescale(c(dat))) #这里输入数据集
  o <- order(vals, decreasing = FALSE)
  cols <- scales::col_numeric("Blues", domain = NULL)(vals) #选择一个色系
  colz <- setNames(data.frame(vals[o], cols[o]), NULL)
  #colz就是你定义的colorscale；使用时令选项colorscale=colz即可
}
