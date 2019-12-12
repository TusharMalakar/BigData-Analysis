
def make_matrix(project2_test):
   """
   :param project2_test:
   :return: matrix
   """
   with open(project2_test, 'r') as file:
       columns = []
       for document in file.readlines():
          columns.append(filter_document(document))
       return columns


def filter_document(document):
   """
   :param document:
   :return: filtered_document
   """
   row = []
   for term in document.split():
      # if document.split()[0] not in row:
      #    row.append(document.split()[0])
      if term.startswith('gene') and term.endswith('gene') or term.startswith('dis') and term.endswith('dis'):
         row.append(term)
   return row


def print_matrix(matrix):
   """
   :param matrix:
   :return: None
   """
   for row in matrix:
      # print(row, "\n")
      print(len(row), row, "\n")


def tf(document):
   """
   :param document:
   :return: tf
   """
   for word in document:
      if 'gene' in word:
         print(word)
      if 'dis' in word:
         print(word)
   pass


def tf_idf():
   """
   :return: TF-IDF
   """
   pass


def semantic_similarity():
   """
   :return:
   """
   pass


if __name__ == "__main__":
   matrix = make_matrix("project2_test.txt")
   # print_matrix(matrix)
   tf(matrix[0])





