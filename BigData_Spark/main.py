#!/usr/bin/env python

import sys
import math
import pyspark
from collections import Counter


def filterFile(line):
    return filter(lambda x: x.startswith('dis') or x.startswith('gene'), line.split())


def mapReduce(rdd):
    count = Counter(rdd.split())
    doc_frequency = count.most_common(len(rdd))
    return doc_frequency


def tremFrequency(line):
    length = reduce(lambda x, y: x + y[1], line, 0)
    return map(lambda (x, y): (x, (float(y)/length)), line)


def multi(x, y):
    try:
        return x*y
    except ValueError:
        print(None)


def driver():
    if len(sys.argv) != 2:
        print("Usage: pythonFile, <inputFile>")
        sys.exit(-1)
    sc = pyspark.SparkContext()
    file = sc.textFile(sys.argv[1])
    reduced = file.map(mapReduce)
    # print(reduced.collect())
    tf = reduced.map(tremFrequency)
    # print(tf.collect())

    # log(number_of_documents / number_of_times_term_exist_in_all_documents)
    numDoc = tf.count()
    keys = tf.flatMap(lambda r: r).keys()
    # print(keys.collect())
    di = keys.map(lambda word: (word, 1)).reduceByKey(lambda x, y: x + y)
    # print(di.collect())
    tempIdf = di.map(lambda (a, b): (a, math.log10(numDoc / float(b))))
    # print(tempIdf.collect())
    record = tempIdf.collect()
    idf = tf.map(lambda x: record)
    print(idf.collect())
    # rdd_temp = tf.zip(idf)
    # print(rdd_temp.collect())


if __name__ == "__main__":
    driver()
