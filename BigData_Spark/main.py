#!/usr/bin/python
import sys
import math
from MapReduce import reducer


def all_terms(matrix):
    """
    :param matrix:
    :return: all terms from all documents
    """
    all_terms = []
    for doc in matrix:
        if doc not in all_terms:
            all_terms.append(doc[0])
    return all_terms


def semantic_similarity():
    """
    :return:
    """
    pass


def tf(document):
    term_sum, matrix = 0, []
    for term in document:
        term_sum += term[1]
    for i in document:
        matrix.append((i[0], float(i[1])/term_sum))
    return matrix


def tf_idf(RDD):
    """
    log(number_of_documents / number_of_times_term_exist_in_all_documents)
    :param matrix:
    :return: TF-IDF
    """
    numbers_of_documents, count_doc, terms = len(RDD), 0, all_terms(RDD)
    idf = []
    for term, doc in zip(terms, RDD):
        if term in doc:
            count_doc += 1
        idf.append((term, math.log(float(numbers_of_documents) / count_doc)))
    return idf


def driver():
    RDD = reducer()
    RDD1 = RDD.map(tf)
    RDD2 = RDD1.map(tf_idf)
    print(RDD2.count())
    print(RDD2.collect())
    # RDD2.saveAsTextFile(sys.argv[2])


if __name__ == "__main__":
    driver()
