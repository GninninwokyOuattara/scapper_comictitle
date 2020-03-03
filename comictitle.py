#!/usr/bin/env python3

#print last comic title from  xkcd.com
#If given a number on run, print (numbers) comics title from xkcd.com

import bs4, requests, sys



url = "https://xkcd.com"

def getStuff(url):
	res = requests.get(url)
	soup = bs4.BeautifulSoup(res.text, "html.parser")
	return soup.select("#ctitle")[0].text, soup

def nextUrl(soup):
	elems = soup.select("#middleContainer > ul:nth-child(4) > li:nth-child(2) > a")[0]
	return "https://xkcd.com"+elems['href']

#comic_title, soup = getStuff(url)
#print(comic_title)
#url = nextUrl(soup)
#
#for i in range(200):
#	comic_title, soup = getStuff(url)
#	print(comic_title)
#	url = nextUrl(soup)

if len(sys.argv)>1:
	if sys.argv[1].isnumeric():
		for i in range(int(sys.argv[1])):
			comic_title, soup = getStuff(url)
			print(comic_title)
			url = nextUrl(soup)
else:
	comic_title, soup = getStuff(url)
	print(comic_title)
	url = nextUrl(soup)



