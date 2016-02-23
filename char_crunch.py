#! /usr/bin/python
from bs4 import BeautifulSoup
import requests
base_url = "http://gameofthrones.wikia.com/wiki/Daenerys_Targaryen"
soup = BeautifulSoup(requests.get(base_url).content,"lxml")
