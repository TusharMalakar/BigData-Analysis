from pyspark.sql import SparkSession, Row
from pyspark import conf, SparkContext


Spark = SparkSession.builder.master("local").appName("BigData").getOrCreate()
data_frame = [('First', 1), ('Second', 2), ('Third', 3), ('Fourth', 4), ('Fifth', 5)]
df = Spark.createDataFrame(data_frame)
hdfs_path = "hdfs://localhost:9000//bigdata/"


def write_hdfs(file):
   """
      hdfs://                       - protocol type
      localhost                     - ip address(may be different for you eg. - 127.56.78.4)
      54310                         - port number
      /folder/fileName.txt          - Complete path to the file you want to load.
   """
   print("writing to hdfs....")
   df.write.csv(hdfs_path+file)



def hdfs_show(file):
   """
   Read from HDFS
   'hdfs://localhost:9000//bigdata/bigdata.csv'
   :param file:
   :return:
   """
   print("Reading file from =>", hdfs_path+file)
   df_load = Spark.read.csv(hdfs_path+file)
   df_load.show()


if __name__ == "__main__":
   hdfs_show("bigdata.csv")

   """
   Stop the session
   """
   Spark.stop()
