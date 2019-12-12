
docList = []
with open("project2_test.txt", 'r') as file:
    for document in file.readlines():
        for word in document.split():
            if document.split()[0] not in docList:
                docList.append(document.split()[0])
            if word.startswith('gene') and word.endswith('gene') or word.startswith('dis') and word.endswith('dis'):
                docList.append(word)

