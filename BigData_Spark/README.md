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


