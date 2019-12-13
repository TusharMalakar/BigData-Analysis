from pyspark.sql import SparkSession


sparkSession = SparkSession.builder.appName("example-pyspark-read-and-write").getOrCreate()
data = [('First', 1), ('Second', 2), ('Third', 3), ('Fourth', 4), ('Fifth', 5)]
df = sparkSession.createDataFrame(data)

"""
   hdfs://                       - protocol type
   localhost                     - ip address(may be different for you eg. - 127.56.78.4)
   54310                         - port number
   /folder/fileName.txt          - Complete path to the file you want to load.
"""
# Write into HDFS
df.write.csv("hdfs://localhost:9000//bigdata/testfolder/example.csv")
