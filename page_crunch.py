#! /usr/bin/python
from bs4 import BeautifulSoup
import requests
base_url = "http://gameofthrones.wikia.com/wiki/Category:Characters?title=Category%3ACharacters&page=1"
soup = BeautifulSoup(requests.get(base_url).content,"lxml")
chars = soup.find_all("div",{'class':'category-gallery-item'})
for index in range(0,16):
	print chars[index].a['href'],"#####",chars[index].a['title']
