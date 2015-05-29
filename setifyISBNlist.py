with open("Summer2015LSU-isbn.txt") as bunchesISBNs:
    isbns = [line.strip() for line in bunchesISBNs]
print (len(isbns))
isbns = set(isbns)
print (len(isbns))
with open("SetSummer2015LSU-isbn.txt", "w") as outfile:
    for item in isbns:
        outfile.write("%s\n" % item)
