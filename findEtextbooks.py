import os
import re
import string
import requests
import csv
from xml.etree import ElementTree

pubFilePath = "TestPublisherFiles"
storeFilePath ="BookstoreFiles"
queryWebService = False

def findISBNs (filename, path):
    isbnPattern1 = re.compile(r'978(?:-?\d){10}')
    isbnPattern2 = re.compile(r'[A-Za-z]((?:-?\d){10})\D')
    isbnPattern3 = re.compile(r'[A-zA-Z]((?:-?\d){9}X)')
    isbnPattern4 = re.compile(r'a(\d{10})\D')
    isbns = []
    #with open("CRCRoughISBN.txt", encoding="utf8") as isbn_lines: #use for utf8
    with open(os.path.join(path, filename), "r") as isbn_lines:
        for line in isbn_lines:
            isbns.extend(isbnPattern1.findall(line))
            isbns.extend(isbnPattern2.findall(line))
            isbns.extend(isbnPattern3.findall(line))
            isbns.extend(isbnPattern4.findall(line))
    stripped = []
    for y in isbns:
        stripped.append(y.translate(str.maketrans('','','-')))
        stripped = list(set(stripped))
    return stripped

pubISBNs = []
for pubFile in os.listdir(pubFilePath):
    pubISBNs = pubISBNs + (findISBNs(pubFile,pubFilePath))

courseISBNs = []
for storeFile in os.listdir(storeFilePath):
    courseISBNs = courseISBNs + (findISBNs(storeFile,storeFilePath))

xCourseISBNs = []
#writing the results of webservice query (OCLC xISBN) to file - so as not to overstay our welcome
if queryWebService:
    for i in courseISBNs:
        url = 'http://xisbn.worldcat.org/webservices/xid/isbn/'+i+'?method=getEditions&format=xml&ai=mike.waugh'
        response = requests.get(url)
        tree = ElementTree.fromstring(response.content)
        for child in tree:
            xCourseISBNs.append(child.text)
    xCourseISBNs = list(set(xCourseISBNs))
    with open("expandedCourseISBNs.txt", "w") as outfile:
        for item in xCourseISBNs:
            outfile.write("%s\n" % item)
else:
    with open("expandedCourseISBNs.txt", "r") as courseFile:
        xCourseISBNs = [book.strip() for book in courseFile]



