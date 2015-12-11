import os
import re
import string
import requests
import csv
from xml.etree import ElementTree

pubFilePath = "TestPublisherFiles"

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


allISBNs = []
for pubFile in os.listdir(pubFilePath):
    allISBNs = allISBNs + (findISBNs(pubFile,pubFilePath))

