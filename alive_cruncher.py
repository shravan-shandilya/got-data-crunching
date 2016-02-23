#! /usr/bin/python
from bs4 import BeautifulSoup
import requests
base_url = "http://gameofthrones.wikia.com/wiki/Category:Status:_Alive?title=Category%3AStatus%3A_Alive&sort=mostvisited&amp%3Bdisplay=exhibition&page="
junk = open("characters_alive.txt","w+")
for page in range(1,27):
	url = base_url+str(page)
	print url
	char_soup = BeautifulSoup(requests.get(url).content,'lxml')
	chars = char_soup.find_all("div",{'class':'category-gallery-item'})
	for index in range(0,28):
		try:
			junk.write(chars[index].a['title']+"\n")
		except:
			break
junk.close()
