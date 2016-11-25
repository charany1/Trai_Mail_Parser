import urllib2
import re
import json
from bs4 import BeautifulSoup

url_list = ['http://trai.gov.in/Comments/OLD/27-Mar=to-10-Apr/27-mar.html',
			'http://trai.gov.in/Comments/11-APRIL/11-April.html',
			'http://www.trai.gov.in/Comments/12-April/12-April-p2/12-April-p2.html',
			'http://www.trai.gov.in/Comments/13-April-15/13-April.html',
			'http://www.trai.gov.in/Comments/14-April-1/14-April-1.html',
			'http://www.trai.gov.in/Comments/14-April-2/14-April-2.html',
			'http://www.trai.gov.in/Comments/14-April-3/14-April-3.html',
			'http://www.trai.gov.in/Comments/14-April-4/14-April-4.html',
			'http://trai.gov.in/Comments/15-April/15-April.html',
			'http://www.trai.gov.in/Comments/16-April/16-April/16-April.html',
			'http://www.trai.gov.in/Comments/16-April/16-April-p2/16-April-p2.html',
			'http://trai.gov.in/Comments/17-April/17-April.html',
			'http://trai.gov.in/Comments/18-April/18-April.html',
			'http://trai.gov.in/Comments/19-April/19-April.html',
			'http://trai.gov.in/comments/20-April/20-April.html',
			'http://www.trai.gov.in/Comments/21-April/21-April.html',
			'http://www.trai.gov.in/Comments/22-April/22-April.html',
			'http://trai.gov.in/comments/OLD/23-April/23-April.html',
			'http://trai.gov.in/comments/24-April/24-April.html'
			]

def replace_dot_and_at_in_email(mail):
	mail =  mail.replace("(at)","@")
	mail =  mail.replace("(dot)",".")
	return mail

total_count = 0

for url in url_list:
	soup = BeautifulSoup(urllib2.urlopen(url).read())

	table = soup.find("table")
	table_rows = table.find_all("tr")

	content_rows = table_rows[2:]



	name_email_list = []

	print url,total_count
	for row in content_rows:
		total_count += 1
		name_email_combined = row.find_all("td")[1].get_text()
		#str_name_email_combined = str(name_email_combined)
		#print  , str(re.findall("<(.*)>",name_email_combined))
		
		name  = str(re.findall("(.*)<",name_email_combined))
		email = str(re.findall("<(.*)>",name_email_combined))
		email = replace_dot_and_at_in_email(email)
		name_email_list.append((name,email))
		with open('mails.json','a') as outfile:
			json.dump(name_email_list,outfile)


print total_count


	
