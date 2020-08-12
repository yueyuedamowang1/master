# 第一次作业介绍
## 爬虫介绍
网络爬虫（又称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。
## 连接
这是爬虫的[介绍](https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711?fr=aladdin)
## 程序介绍
### 下载图片部分
```python
import urllib.request
response = urllib.request.urlopen(web)
img1 = response.read()

with open(name+'.jpg.jpg','wb')as f:
    f.write(img1)
```
## 使用程序时注意
在运行时要准备好有空间的文件夹，图片会下载在程序所在的文件夹里