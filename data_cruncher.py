#! /usr/bin/python
from bs4 import BeautifulSoup
import requests
base_url = "http://gameofthrones.wikia.com/wiki/Category:Characters?title=Category%3ACharacters&page="
junk = open("characters.txt","w+")
for page in range(1,57):
	url = base_url+str(page)
	print url
	char_soup = BeautifulSoup(requests.get(url).content,'lxml')
	chars = char_soup.find_all("div",{'class':'category-gallery-item'})
	for index in range(0,16):
		junk.write(chars[index].a['title']+"\n")
junk.close()
