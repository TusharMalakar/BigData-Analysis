# My HADOOP:
   - C:\hadoop\sbin
   - window host: c:\Windows\System32\Drivers\etc\hosts
# Hadoop Window CMD
1. hdfs namenode -formate
2. start-all.cmd
3. resource-manager: all map-reduce programs that are executed in the system
	- http://localhost:8088/cluster
4. namenode UI:
	- http://localhost:50070/dfshealth.html#tab-overview
5. make directory in hadoop file system:
	- hadoop fs -mkdir "filename"
6. show hadoop directory
    - hadoop fs -ls /
    - hadoop fs -ls /dir_name
7. copy file to hadoop 

   
# Implement using cloud platform 100+20
- input is file: (insert file)
    - filter the file, keeping disease and name
    - insert in hdfs
- Query from the HDFS get the related doc (document) similarity
    - OUTPUT list of similar doc (document)  



