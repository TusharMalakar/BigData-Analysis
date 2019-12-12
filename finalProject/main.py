
docList = []
with open("project2_test.txt", 'r') as file:
    for document in file.readlines():
        for word in document.split():
            if document.split()[0] not in docList:
                docList.append(document.split()[0])
            if word.startswith('gene') and word.endswith('gene') or word.startswith('dis') and word.endswith('dis'):
                docList.append(word)

# print(docList)
numDoc = []
for ascii in docList:
   if 57 >= ord(ascii[0]) >= 48:
      numDoc.append(ord(ascii[0]))

matrix = []
for i in range(len(numDoc)):
   row = []
   for j, tr in zip(range(20), docList):
      if ord(tr[0]) <=47 or ord(tr[0]) >= 58:
         row.append(tr)
   matrix.append(row)
print(matrix)


