
def makeMatrix(project2_test):
   with open(project2_test, 'r') as file:
       columns = []
       for document in file.readlines():
          columns.append(filterDocument(document))
       return columns


def filterDocument(document):
   row = []
   for term in document.split():
      if document.split()[0] not in row:
         row.append(document.split()[0])
      if term.startswith('gene') and term.endswith('gene') or term.startswith('dis') and term.endswith('dis'):
         row.append(term)
   return row


def print_matrix(matrix):
   for pp in matrix:
      print(pp, "\n")


if __name__ == "__main__":
   matrix = makeMatrix("project2_test.txt")
   print_matrix(matrix)




