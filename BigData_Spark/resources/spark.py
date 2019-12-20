#!/usr/bin/env python

import sys
import pyspark
from collections import Counter


def mapper(rdd):
    return map(lambda x: x, rdd.split())


def reducer(rdd):
    count = Counter(rdd)
    doc_frequency = count.most_common(len(rdd))
    return doc_frequency


def tf(document):
    term_sum, matrix = 0, []
    for term in document:
        term_sum += term[1]
    for i in document:
        matrix.append((i[0], float(i[1])/term_sum))
    return matrix


def mapper2(lines):
    """Mapper mapping to 2D Matrix"""
    mapped_matrix = []
    for word in lines.split():
        mapped_matrix.append((word.strip(",")))
    return mapped_matrix


def idf(freq_table, lines):
    accumulator = []
    for index in range(len(freq_table)):
        accumulator.append((freq_table[index][0], float(lines.count())/freq_table[index][1]))
    return accumulator


def frequency_table(accumulator, TF):
    freq_table = []
    for key in accumulator:
        count = 0
        for doc in TF:
            for term in doc:
                if key == term[0]:
                    count += term[1]
        freq_table.append((key, count))
    return freq_table


def all_Keys(matrix):
    all_terms = []
    for doc in matrix:
        if doc not in all_terms:
            all_terms.append(doc[0])
    return all_terms


def filter_Keys(RDD):
    accumulator = []
    for row in RDD:
        for key in row:
            if key not in accumulator:
                accumulator.append(key)
    return accumulator


def _tf_idf(tfidf, TF):
    accumulator = []
    for i_doc in tfidf:
        list_ = []
        for i, t in zip(i_doc, TF):
            list_.append((i[0], i[1]*t[1]))
        accumulator.append(list_)
    return accumulator


def driver():
    if len(sys.argv) != 3:
        print("Usage: pythonFile, <inputFile>, <OutputDirOne>")
        sys.exit(-1)
    sc = pyspark.SparkContext()
    lines = sc.textFile(sys.argv[1])
    rdd1 = lines.map(mapper)
    TF = rdd1.map(reducer)
    RDD_Keys = TF.map(all_Keys)
    accumulator = filter_Keys(RDD_Keys.collect())
    freq_table = frequency_table(accumulator, TF.collect())
    tfidf = idf(freq_table, lines)
    IT_IDF = _tf_idf(TF.collect(), tfidf)
    ITIDF = TF.map(lambda x: IT_IDF)
    print(ITIDF.collect())

    # ITIDF.saveAsTextFile('/out/one')
    # ITIDF.saveAsTextFile(sys.argv[2])


if __name__ == "__main__":
    driver()
