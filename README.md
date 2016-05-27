# ASampleSpider
一个爬取豆瓣图书下所有标签下前20本书的名字、图片和评分的爬虫  

## main.py
调用spider类中start函数开始爬取

## spider.py
1、获取所有的标签
2、每一个标签都启动一个进程，没有使用pool所以进程比较多
3、根据每一个标签的网址启动爬取每一本书的名字，评分和图片的URL，保存到类中，将所有的类放到一个链表中
4、遍历所有的book，根据图片的URL下载到本地当前文件夹的\img中


## ItemInfo.py
1、Item类存放book的名称、评分和图片的URL
2、tag类存放tag的名称和URL

