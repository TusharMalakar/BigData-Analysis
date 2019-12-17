import math
from collections import Counter


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
   number_of_times_term_in_document / len(document)
   :param document:
   :return: tf of individual document
   """
   counter = Counter(document)
   doc_frequency = counter.most_common(len(document))
   freq_table = []
   for doc in doc_frequency:
      # pushing as tuple
      freq_table.append((doc[0], doc[1]/len(document)))
   return freq_table



def all_terms(matrix):
   """
   :param matrix:
   :return: all terms from all documents
   """
   all_terms = []
   for row in matrix:
      for doc in row:
         if doc not in all_terms:
            all_terms.append(doc)
   print("terms ", len(all_terms))
   return all_terms



def tf_idf(matrix):
   """
   log(number_of_documents / number_of_times_term_exist_in_all_documents)
   :param matrix:
   :return: TF-IDF
   """
   numbers_of_documents, count_doc, terms = len(matrix), 0, all_terms(matrix)
   idf = []
   for term, doc in zip(terms, matrix):
      if term in doc:
         count_doc += 1
         idf.append((term, math.log(numbers_of_documents / count_doc)))
   for i_idf in idf:
      print(i_idf[1])
   return idf


def semantic_similarity():
   """
   :return:
   """
   pass


if __name__ == "__main__":
   # matrix = make_matrix("project2_test.txt")
   # print(matrix)
   #
   #
   # tf_idf(matrix)
   # for term in matrix:
   #    print(tf(term))  # for  individual document
   #
   #
   # with open("bigdata.csv", 'w') as data:
   #    for line in matrix:
   #       data.write(str(line).strip('[]'))
   #       data.write("\n")
   # data.close()
   matrix = [['q', 'k'], ['l', 'o']]
   term = ['o', 'k']
   for row in matrix:
      for tr in term:
         if tr in row:
            print(tr, row)

