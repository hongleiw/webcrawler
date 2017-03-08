from bs4 import BeautifulSoup
sina = BeautifulSoup(open("CrawlerSina.html"))
for a in sina.find_all('a') :
	try :
		tag = a.name
		print a.string
		print a['href']
	except :
		pass
	
