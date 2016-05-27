class ItemInfo:
	itemNums = 0
	def __init__(self, itemName, score, url = None):
		self.itemName = itemName
		self.score = score
		self.imgUrl = url
		ItemInfo.itemNums+=1
		
class Tag:
	tagNums = 0
	def __init__(self, tagUrl, tagName):
		self.tagName = tagName
		self.url = 'https://book.douban.com' + tagUrl + '?start=0&type=T'
		Tag.tagNums+=1