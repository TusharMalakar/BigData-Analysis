#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""
import sys
import pyspark
from collections import Counter


def mapper(lines):
    """Mapper mapping to 2D Matrix"""
    mapped_matrix = []
    for word in lines.split():
        mapped_matrix.append((word.strip(",")))
    return mapped_matrix


def merge(rdd):
    count = Counter(rdd)
    doc_frequency = count.most_common(len(rdd))
    return doc_frequency


def reducer():
    if len(sys.argv) != 3:
        print("Usage: pythonFile, <inputFile>, <OutputDir>" )
        sys.exit(-1)
    sc = pyspark.SparkContext()
    lines = sc.textFile(sys.argv[1])
    rdd1 = lines.map(mapper)
    rdd2 = rdd1.map(merge)
    # print(rdd2.collect())
    return rdd2


if __name__ == "__main__":
    print(reducer())
