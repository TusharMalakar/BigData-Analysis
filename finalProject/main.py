


with open("project2_test.txt", 'r') as file:
    for document in file.readlines():
        for word in document.split():
            if word.startswith('gene') and word.endswith('gene') or word.startswith('dis') and word.endswith('dis'):
                print(document.split()[0], word)
