import scrapy
class QiuBaiSpider(scrapy.Spider) :
	name = "qiubai"
	start_urls = [
		"http://m.qiushibaike.com/hot/page/"
	]

	def parse(self, response) :
		tmp = response.xpath('//div[@class="author clearfix"]/a[2]/h2').extract()
		#tmp = response.xpath('//head/title').extract()
		for t in tmp :
			print t.encode('utf-8')