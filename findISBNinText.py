import re
import string
import requests
import csv
from xml.etree import ElementTree

isbnPattern1 = re.compile(r'978(?:-?\d){10}')
isbnPattern2 = re.compile(r'[A-Za-z]((?:-?\d){10})\D')
isbnPattern3 = re.compile(r'[A-zA-Z]((?:-?\d){9}X)')
isbnPattern4 = re.compile(r'a(\d{10})\D')
isbns = []
#with open("CRCRoughISBN.txt", encoding="utf8") as isbn_lines: #use for utf8
with open("SummerTextbooks2015.txt") as isbn_lines:
    for line in isbn_lines:
        isbns.extend(isbnPattern1.findall(line))
        isbns.extend(isbnPattern2.findall(line))
        isbns.extend(isbnPattern3.findall(line))
        isbns.extend(isbnPattern4.findall(line))
stripped = []
for y in isbns:
    stripped.append(y.translate(str.maketrans('','','-')))
    stripped = list(set(stripped))
expandedisbns = []
# only run this part when you need to query webservice
for z in stripped:
    urlstripped = 'http://xisbn.worldcat.org/webservices/xid/isbn/'+z+'?method=getEditions&format=xml&ai=mike.waugh'
    response = requests.get(urlstripped)
    tree = ElementTree.fromstring(response.content)
    for child in tree:
           expandedisbns.append(child.text)
           
#need to print these out to get around xisbn throttling of webservice requests
with open("expandedISBNSummer2.txt", "w") as outfile:
    for item in expandedisbns:
        outfile.write("%s\n" % item)
with open("expandedISBNSummer2.txt", "r") as i:
    coursebooks = [book.strip() for book in i]
#match the files
with open('AllPublisherISBNs.txt','r') as f:
    isbn = [line.strip() for line in f]
with open ("EbooksByItemCat201412.txt", "r") as catfile:
    catlines = [r.strip() for r in catfile]
isbn = list(set(isbn + catlines))
matches = []
for x in isbn:
    if x in coursebooks:
        matches.append(x)
with open("MatchedISBNsSummer2.txt", "w") as outfile:
   for item in matches:
        outfile.write("%s\n" % item)
        
# get metadata from xisbn
rows = []
for z in matches:
    urlz = 'http://xisbn.worldcat.org/webservices/xid/isbn/'+z+'?method=getMetadata&format=xml&fl=*&ai=mike.waugh'
    response = requests.get(urlz)
    tree = ElementTree.fromstring(response.content)
    for child in tree:
        rows.append(child.attrib)

# print to csv
with open ("MatchedEtextbooksSummer2015-2.csv", "w") as csvfile:
    fieldnames = rows[1].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n', extrasaction='ignore')
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
