# Tushar Malakar
# Class : Big Data 

Project Description:
====================
- This Project was built in Google Cloud Platform using google DataProc. DataProc is a hadoop dependend file system.



Test using Google Cloud DataProc Console 
========================================
- To submit a job:
    - Fist the source file :  MapReduc.py
    - Fist Argument: Input file
    - Second Argument : output directory
    ![submit](https://user-images.githubusercontent.com/35859780/71210538-17923100-227b-11ea-8bf2-51ff34f92387.PNG)


check the job status:
=======================
![hdfs](https://user-images.githubusercontent.com/35859780/71210535-17923100-227b-11ea-8558-a7801fd65801.PNG)

    
- I am writing in hadoop file system
![ls](https://user-images.githubusercontent.com/35859780/71210536-17923100-227b-11ea-920c-678f40caf909.PNG)

- I am writing in Google Cloud Storage Bucket
![gcpBucket](https://user-images.githubusercontent.com/35859780/71210537-17923100-227b-11ea-9f20-6cc1065bd049.PNG)





Query a similarity from hadoop file system via SSH to Cluster:
=============================================================
hdfs dfs -cat /home/output/result/part-00001| grep 'gene_egfr_kinase_gene'
    
# ======================================================================

- open VM instance SSH
- ls /usr/lib/hadoop-mapreduce/


- hdfs dfs -mkdir /home
- hdfs dfs -mkdir /home/input
- hdfs dfs -mkdir /home/output
- hdfs dfs -ls /home/
- hdfs dfs -put bigdata.csv /home/input/


- mkdir tmp
- cd tmp
- cp /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar .
- cp /usr/lib/hadoop-mapreduce/hadoop-streaming.jar .
- cp /usr/lib/hadoop-mapreduce/hadoop-streaming-2.9.2.jar .
- unzip hadoop-mapreduce-examples.jar
- yarn jar  /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount /home/input/ /home/output/wc1
- hdfs dfs -get /home/output* ./tmp/.

- gsutil cp MapReduce.py gs://hdspark/sources/


# ======================================================================
# My HADOOP:
   - C:\hadoop\sbin
   - window host: c:\Windows\System32\Drivers\etc\hosts
# Hadoop Window CMD
1. hdfs namenode -formate
2. start-all.cmd (or) start-dfs.cmd && start-yarn.cmd
3. resource-manager: all map-reduce programs that are executed in the system
	- http://localhost:8088/cluster
4. namenode UI:
	- http://localhost:50070/dfshealth.html#tab-overview
5. start spark
    - spark-shell.cmd

	
# "hadoop fs" to see all cmd 
5. make directory in hadoop file system:
	- hadoop fs -mkdir "filename"
6. show hadoop directory
    - hadoop fs -ls /
    - hadoop fs -ls /dir_name
7. copy file (bigdata.csv) to hadoop "/bigdata"
    - hadoop fs -put bigdata.csv /bigdata/
8. download a file from hahoop to your current directory
    - hadoop fs -get /bigdata/testfolder/bigdata.txt hadoop_data.txt
9. hadoop display a file 
    - hadoop fs -cat /bigdata/testfolder/bigdata.txt

   
# Implement using cloud platform 100+20
- input is file: (insert file)
    - filter the file, keeping disease and name
    - insert in hdfs
- Query from the HDFS get the related doc (document) similarity
    - OUTPUT list of similar doc (document)  
    
    
    
# run "map reduce in window"
- type bigdata.csv | python mapper.py | python reducer.py
- hadoop streaming jar
    - C:\hadoop\share\hadoop\tools\lib\hadoop-streaming-2.8.0.jar



# hadoop jar hadoop-streaming-2.2.0.jar  -file C:\hadoop\BigData_Spark\MapReduce\mapper.py -mapper mapper.py -file   C:\\Users\\tusha\\PycharmProjects\\Machine-learning-using-BigData\\BigData_Spark\\MapReduce\\reducer.py -reducer reducer.py -input /bigdata/bigdata -output /bigdata//Wordcount

- https://muhammadbilalyar.github.io/blogs/How-to-Run-Hadoop-wordcount-MapReduce-Example-on-Windows-10/
- mapreduce client : https://github.com/MuhammadBilalYar/HADOOP-INSTALLATION-ON-WINDOW-10/blob/master/MapReduceClient.jar
- input_file.txt :  https://github.com/MuhammadBilalYar/HADOOP-INSTALLATION-ON-WINDOW-10/blob/master/input_file.txt
- hadoop fs -mkdir /input_dir
- hadoop fs -put C:/input_file.txt /input_dir
- hadoop fs -ls /input_dir/ 
- hadoop dfs -cat /input_dir/input_file.txt
- hadoop jar C:\hadoop\share\hadoop\mapreduce\cli.jar wordcount /input_dir /output_dir
- hadoop dfsadmin –safemode leave
- hadoop fs -rm -r /iutput_dir/input_file.txt
- hadoop fs -rm -r /iutput_dir


