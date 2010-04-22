import feedparser
import re
import time

def normalize_description(string):
	found = re.search(ur"Description\s*:\s*(.+)", string).group(1)
	return found


filename = r".\mURL.txt"
mdl = feedparser.parse("http://www.malwaredomainlist.com/hostslist/mdl.xml")

match = re.compile(ur"^Host: (\S+),")
ipmatch = re.compile(ur"IP\s+address:\s+(\S+),")

fn = file(filename, "w")


for entry in mdl.entries:
	print entry.description
	found = match.search(entry.description).group(1)
	if found == False or found == '-':
		found = ipmatch.search(entry.description).group(1)
		if found == False:
			found = "None"


	now = time.localtime()
	fn.write("%s.%s.%s|" % (now[2], now[1], now[0]))
	fn.write(found+'|')
	fn.write(normalize_description(entry.description)+'\n')

fn.close()



