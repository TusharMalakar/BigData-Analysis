from pyspark import SparkContext
from operator import add


sc5 = SparkContext("local", "Collect app")
words = sc5.parallelize(
   ["scala",
   "java",
   "hadoop",
   "spark",
   "akka",
   "spark vs hadoop",
   "pyspark",
   "pyspark and spark"]
)
coll = words.collect()
print("Elements in RDD -> %s" % (coll))


# sc4 = SparkContext("local", "Filter app")
# words = sc4.parallelize (
#    ["scala",
#    "java",
#    "hadoop",
#    "spark",
#    "akka",
#    "spark vs hadoop",
#    "pyspark",
#    "pyspark and spark"]
# )
# words_filter = words.filter(lambda x: 'spark' in x)
# filtered = words_filter.collect()
# print("Fitered RDD -> %s" % (filtered))
#
#
# sc3 = SparkContext("local", "Map app")
# words = sc4.parallelize (
#    ["scala",
#    "java",
#    "hadoop",
#    "spark",
#    "akka",
#    "spark vs hadoop",
#    "pyspark",
#    "pyspark and spark"]
# )
# words_map = words.map(lambda x: (x, 1))
# mapping = words_map.collect()
# print ("Key value pair -> %s" % (mapping))
#
#
# sc2 = SparkContext("local", "Reduce app")
# nums = sc2.parallelize([1, 2, 3, 4, 5])
# adding = nums.reduce(add)
# print("Adding all the elements -> %i" % (adding))
#
#
# sc0 = SparkContext("local", "Join app")
# x = sc0.parallelize([("spark", 1), ("hadoop", 4)])
# y = sc0.parallelize([("spark", 2), ("hadoop", 5)])
# joined = x.join(y)
# final = joined.collect()
# print("Join RDD -> %s" % (final))
#
#
# sc1 = SparkContext("local", "Cache app")
# words = sc1.parallelize (
#    ["scala",
#    "java",
#    "hadoop",
#    "spark",
#    "akka",
#    "spark vs hadoop",
#    "pyspark",
#    "pyspark and spark"]
# )
# words.cache()
# caching = words.persist().is_cached
# print("Words got chached > %s" % (caching))
