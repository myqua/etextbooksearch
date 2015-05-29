with open("expandedISBNsBOTH.txt", "r") as i:
    coursebooks = [book.strip() for book in i]
#match the files
with open('EbooksByItemCat201412.txt','r') as f:
    isbn = [line.strip() for line in f]
matches = []
for x in isbn:
    if x in coursebooks:
        matches.append(x)
with open("MatchedISBNsSummerFromCat.txt", "w") as outfile:
   for item in matches:
        outfile.write("%s\n" % item)
