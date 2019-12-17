#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""
import sys
import pyspark


def mapper(lines):
    """Mapper mapping to 2D Matrix"""
    mapped_matrix = []
    for word in lines.split():
        mapped_matrix.append((word.strip(","), 1))
    return mapped_matrix


def reducer2(rdd):
    rdd_matrix = []
    for row in rdd:
        print(row)
    return rdd


def reducer():
    if len(sys.argv) != 3:
        print("Usage: pythonFile, <inputFile>, <OutputDir>" )
        sys.exit(-1)
    # documents = mapper(sys.argv[1])
    sc = pyspark.SparkContext()
    lines = sc.textFile(sys.argv[1])
    rdd1 = lines.map(mapper)
    rdd2 = rdd1.map(reducer2)
    print(rdd2.collect())


    # matrix = []
    # for tuplesList in documents:
    #     RDD = sc.parallelize(tuplesList)
    #     matrix.append(sorted(RDD.countByKey().items()))
    # RDD.saveAsTextFile(sys.argv[2])
    # return matrix


if __name__ == "__main__":
    print(reducer())
