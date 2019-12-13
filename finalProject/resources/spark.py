from pyspark.sql import SparkSession
import sys
import os

#
# os.environ['HADOOP_HOME'] = "C:\\hadoop"
# sys.path.append("C:\\hadoop\\bin")


sparkSession = SparkSession.builder.appName("example-pyspark-read-and-write").getOrCreate()
data = [('First', 1), ('Second', 2), ('Third', 3), ('Fourth', 4), ('Fifth', 5)]
df = sparkSession.createDataFrame(data)


# Write into HDFS
df.write.csv("hdfs://localhost:9000//bigdata/testfolder/example.csv")
