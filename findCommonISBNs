with open('AllPublisherISBNs.txt','r') as f:
    isbn = [line.strip() for line in f]
matches = []
for x in isbn:
    if x in open('Spring2015BookstoreListWithAltISBNs.txt').read():
        matches.append(x)
print (matches)
