#Concept: Today's program will parse wikipedia and pull the names of all the cities. I may make it more complex and see if I can add 
#... additional information and sorting by specific values. 

#Outline:
#Import webscraper
#import library for opening Urls
#Make sure code can interface with wikipedia
#Request the headers of the wiki
#Open the wiki page
#Run web scraper across page
#Locate specifics for table and column titles
#Pull row data from column titles
#Output data once pulled.
#....


from bs4 import BeautifulSoup
import urllib2

wiki = "https://en.wikipedia.org/wiki/List_of_municipalities_in_Louisiana"
header = {'User-agent': 'Mozilla/5.0'} 
acq = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page)
print soup
