import re
import string
import requests
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
stripped = ['9781118162286','9781118083390']
#for y in isbns:
#   stripped.append(y.translate(str.maketrans('','','-')))
#   stripped = set(stripped)
expandedisbns = []
for z in stripped:
    urlstripped = 'http://xisbn.worldcat.org/webservices/xid/isbn/'+z+'?method=getEditions&format=xml&ai=mike.waugh'
    response = requests.get(urlstripped)
    tree = ElementTree.fromstring(response.content)
    for child in tree:
            expandedisbns.append(child.text)
#need to print these out to get around xisbn throttling of webservice requests
with open("expandedISBNs.txt", "w") as outfile:
    for item in expandedisbns:
        outfile.write("%s\n" % item)
print (expandedisbns)
#match the files
#with open('AllPublisherISBNs.txt','r') as f:
#    isbn = [line.strip() for line in f]
#matches = []
#for x in isbn:
#    if x in stripped:
#        matches.append(x)
#print (matches)

