import urllib2, urllib, ItemInfo, re, os, multiprocessing

class Spider:

	def __init__(self):

	def Start(self):
		tags = self.GetAllTags()
		for tag in tags:
			p = multiprocessing.Process(target=self.GetBooksInTag, args=(tag,))
			p.start()
			
		
	
	def GetBooksInTag(self, tag):
		content = self.GetRequestContent(tag.url)
		bookList = self.GetBookList(content)
		self.DownLoadImg(bookList, tag.tagName)
	
	def GetAllTags(self) :
		tagList = []
		url = "https://book.douban.com/tag/?view=type&icn=index-sorttags-hot"
		try:
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
		except urllib2.URLError, e:
			if hasattr(e,"code"):
				print e.code
				return None
			if hasattr(e,"reason"):
				print e.reason
				return None
		content = response.read()
		pattern = re.compile('<td><a href="(.{0,30})" class="tag">(.*?)</a></td>', re.S)
		items = re.findall(pattern, content)
		for item in items:
			tagList.append(ItemInfo.Tag(item[0], item[1]))
		return tagList
	
	def GetRequestContent(self, url):
		try:
			request = urllib2.Request(url)	
			response = urllib2.urlopen(request)
			content = response.read().decode('utf-8')
			return content
		except urllib2.URLError, e:
			if hasattr(e,"code"):
				print e.code
				return None
			if hasattr(e,"reason"):
				print e.reason
				return None
					
	def GetBookList(self, content):
		pattern = re.compile('<li class="subject-item">.*?<img.*?src="(.*?)".*?width.*?title="(.*?)".*?"rating_nums">(.*?)</span>.*?</li>', re.S)
		items = re.findall(pattern,content)
		bookList=[]
		for item in items:
			bookList.append(ItemInfo.ItemInfo(item[1], item[2], item[0]))
		return bookList
		
		
	def DownLoadImg(self, bookList, tag):
		path="img\\" + tag.decode("utf-8")
		if not os.path.exists(path) :
			os.makedirs(path)

		for book in bookList:
			try:
				data = urllib.urlopen(book.imgUrl).read()
			except Exception, e: 
				print '\tError Download %s'%e
				continue
				
				
			filename = book.itemName + '.jpg'					
			
			
			try:
				filepath = os.path.join(path, filename)
				image=open(filepath, 'wb')
				image.write(data)
			except Exception, e:
				print "Write failed : %s"%e
				continue
			image.close
			del image