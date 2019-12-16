#!/usr/bin/env python

import sys
import collections
from MapReduce.mapper import mapper


def reducer():
    documents = mapper(sys.argv[1])
    matrix = []
    for tuplesList in documents:
        doc_key = []
        for tr in tuplesList:
            doc_key.append(tr[0])
        count = collections.Counter(doc_key)
        matrix.append(count.most_common(len(doc_key)))
    return matrix


if __name__ == "__main__":
    print(reducer())
