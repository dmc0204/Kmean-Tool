from bs4 import BeautifulSoup
from bs4 import SoupStrainer
#import re
#import csv
import urllib2

goodLines = 1
global soup # Global soup variable to store all the data I want to collect -DC
page = urllib2.urlopen("https://discussions.apple.com/community/watch/using_apple_watch")
soup = BeautifulSoup(page, 'html.parser') # Turns the html into nested object structure -DC
soup = soup.find_all("h4") # Finds all the <h4> tags and extracts them and their content -DC

def appleExtract(): # Scrap each page of the forum pages 2-20 for h4 tags and content -DC

	for i in range(2, 15, 1):
		pagec = urllib2.urlopen("https://discussions.apple.com/community/watch/using_apple_watch?page="+ str(i))
		soupc = BeautifulSoup(pagec, 'html.parser')
		soupc = soupc.find_all("h4")
		global soup 
		soup += ''.join(str(e) for e in soupc)

def oddLines(text):

	for e in text.splitlines():
		global goodLines
		if goodLines % 2 == 0:
			print e
		goodLines += 1
			

appleExtract() # Calling the function that walks the pages of forum posts -DC		
soup = ''.join(str(e) for e in soup) # Changing the nested object structure into strings -DC
soup = soup.strip() # Cleaning up the strings (Extra whitespace) -DC
soup = BeautifulSoup(soup, 'html.parser')# Changing back to nested object structure to perform more scrubbing -DC
soup = soup.find_all('a') # Finds all the <a> tags and extracts them and their content -DC
soup = ''.join(str(e) for e in soup) # Changing the nested object structure into strings -DC
soup = soup.strip() # Cleaning up the strings (Extra whitespace) -DC
oddLines(soup)






# *****Below is methods I played around with for my desired output -DC******

#def testfunc():

	#for i in range(0, len(soup)):
		#startswith = soup.find('community:post')
		#endswith = soup.find("</a>", startswith)
		#testout = " "	
		#print soup[startswith:endswith]
		#print startswith
		#print endswith
		#startswith = endswith

#soup = soup.find_all(text=True)
#souptest = ''.join(str(e) for e in souptest)
#souptest2 = ''.join(str(e) for e in souptest2)
#souptest += str(souptest.split("</a>"))
#souptest2 += str(souptest2.split("</a>"))
#for each in souptest:
#	startswith = souptest.find(">")
#	endswith = souptest.find("</a>")
#	testout = souptest[startswith:endswith]
#soup += ''.join(str(e) for e in soupc)
#soupc = ''.join(str(e) for e in soup)
#startswith = 0
#endswith = 0
#appleExtract()
#print soup
#testfunc()
#souptest = re.search(r'>(.*)</a>', souptest)
#souptest = souptest.split(" , ")
#souptest = soup.splitlines()
#souptest = soup.split(',')
#soup = soup.find_all("h4").split("h4")
#testout = soupc.append(text.split("community:post")[1].split("</a>")[0].strip())
#lines = str(soupc).split('\n')
#soup_a_tag = soup.find_all("a")
#soup_h_tag = soup.find_all("h4")
#soupc_a_tag = soupc.find_all("a")
#soupc_h_tag = soupc.find_all("h4")
#soup_a_tag = ''.join(str(e) for e in soup_a_tag)
#soup_h_tag = ''.join(str(e) for e in soup_h_tag)
#soupc_a_tag = ''.join(str(e) for e in soupc_a_tag)
#soupc_h_tag = ''.join(str(e) for e in soupc_h_tag)
#soup_a_tag += str(soup_a_tag.split(","))
#soup_h_tag += str(soup_h_tag.split(","))
#soupc_a_tag += str(soupc_a_tag.split(","))
#soupc_h_tag += str(soupc_h_tag.split(","))
#souptest = soup.find_all("h4")
#souptest = souptest.find_all("community:post")
#print souptest
#souptest2 = soupc.find_all("h4")
#for i in lines:
#	str(soup) += str(soupc)
#page = soup.find_all("community:post")
#print testout
#print souptest
#print souptest2
#print startswith
#print endswith
#print testout
#print soup_a_tag
#print soup_h_tag
#print soupc_a_tag
#print soupc_h_tag

