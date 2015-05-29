import requests
import csv
from xml.etree import ElementTree

with open ("MatchedISBNsSummerFromCat.txt", "r") as infile:
    textbooks = [line.strip() for line in infile]

rows = []
for z in textbooks:
    urlz = 'http://xisbn.worldcat.org/webservices/xid/isbn/'+z+'?method=getMetadata&format=xml&fl=*&ai=mike.waugh'
    response = requests.get(urlz)
    tree = ElementTree.fromstring(response.content)
    for child in tree:
        rows.append(child.attrib)

with open ("MatchedExtextbooksSummer2015FromCat.csv", "w") as csvfile:
    fieldnames = rows[1].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n', extrasaction='ignore')
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
