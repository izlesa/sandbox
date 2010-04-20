import feedparser

mdl = feedparser.parse("http://www.malwaredomainlist.com/hostslist/mdl.xml")

print mdl.feed.title

for entry in mdl.entries:
	print entry