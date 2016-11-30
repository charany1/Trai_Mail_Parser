import urllib2
import re
from bs4 import BeautifulSoup

url_list = ['http://trai.gov.in/Comments/OLD/27-Mar=to-10-Apr/27-mar.html',
			'http://trai.gov.in/Comments/11-APRIL/11-April.html',
			'http://www.trai.gov.in/Comments/12-April/12-April-p2/12-April-p2.html',
			]

soup = BeautifulSoup(urllib2.urlopen('http://trai.gov.in/Comments/OLD/27-Mar=to-10-Apr/27-mar.html').read())

table = soup.find("table")
table_rows = table.find_all("tr")

content_rows = table_rows[2:]

def replace_dot_and_at_in_email(mail):
	mail =  mail.replace("(at)","@")
	mail =  mail.replace("(dot)",".")
	return mail


for row in content_rows:
	name_email_combined = row.find_all("td")[1].get_text()
	print type(name_email_combined)
	quit
	









"""
print soup.findall(re.compile("&lt;(.*)&gt;"))

name_list = re.findall("<td>(.*)&lt;",open('source.html').read())
print len(name_list)
email_list = re.findall("&lt;(.*)&gt;", open('source.html').read())
print len(email_list)

#for i,mail in enumerate(email_list):
#	mail =  mail.replace("(at)","@")
#	mail =  mail.replace("(dot)",".")
#	email_list[i] = mail

#print len(email_list)

#for row in soup('table', {'class': 'spad'})[0].tbody('tr'):
#    tds = row('td')
#    print tds[0].string, tds[1].string

"""