import feedparser
import re

mdl = feedparser.parse("http://www.malwaredomainlist.com/hostslist/mdl.xml")

for entry in mdl.entries:
	match = re.search(ur"Host: ([\S.]+),", entry.description)
	if(match == False):
	    match = re.search(ur"IP address: ([\S.]+),", entry.description)

	print match.group(1)

