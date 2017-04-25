import urllib2
import requests
import os
from bs4 import BeautifulSoup
url = "https://www.youtube.com/results?search_query="
search = raw_input("Enter search query: ")
search_list = search.split(' ')
for wd in search_list:
	url = url + "+" + str(wd)
r = requests.get(url)
counter = 0
soup = BeautifulSoup(r.content, "html.parser")
video = soup.find_all("h3", {"class": "yt-lockup-title"})
for vid in video:
	print '[', counter, ']', vid.find_all("a")[0].text
	counter = counter + 1
choice = raw_input("Enter choice : ")
video_ttl = soup.find_all("h3", {"class": "yt-lockup-title"})[int(choice)].find_all("a")[0].get("href")
video_url = "https://www.youtube.com" + str(video_ttl)
r = requests.get(video_url)
soup = BeautifulSoup(r.content, "html.parser")
video_title = soup.find_all("h1", {"class": "watch-title-container"})[0].find_all("span")[0].text
print "Downloading " +  str(video_title).strip() + " ..."
cmd = 'youtube-dl -q --extract-audio --audio-quality 0 --audio-format mp3 -o \'%(title)s.%(ext)s\' ' + video_url
os.system(cmd)