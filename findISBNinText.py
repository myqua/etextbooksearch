import re
import string
#regex1 = r'978(?:-?\d){10}'
#regex2 = r'a(\d{10})\D'
isbnPattern1 = re.compile(r'978(?:-?\d){10}')
isbnPattern2 = re.compile(r'[A-Za-z]((?:-?\d){10})\D')
isbnPattern3 = re.compile(r'[A-zA-Z]((?:-?\d){9}X)')
isbnPattern4 = re.compile(r'a(\d{10})\D')
isbns = []
#with open("CRCRoughISBN.txt", encoding="utf8") as isbn_lines:
with open("LALE.isbn_list.txt") as isbn_lines:
#with open("UpdatedListSpring2015.txt") as isbn_lines:
    for line in isbn_lines:
        isbns.extend(isbnPattern1.findall(line))
        isbns.extend(isbnPattern2.findall(line))
        isbns.extend(isbnPattern3.findall(line))
        isbns.extend(isbnPattern4.findall(line))
stripped = []
for y in isbns:
    stripped.append(y.translate(str.maketrans('','','-')))
for x in range(10):
    print (stripped[x])
#with open("ProjectMuseISBNOnly.txt", "w") as outfile:
#with open("SummerISBNOnly.txt", "w") as outfile:
with open("LALE-ISBNs.txt", "w") as outfile:
    for item in stripped:
        outfile.write("%s\n" % item)

