
1)########Data Generator Script############## 
  
  a) Install the below fake factory for getting fake names used in our data generator.
      
     [root@localhost ~]# 
                          pip install fake-factory



  b) Run the data generator script ,please note that now i have given the range just 1000 so only 1000 lines will be generated i.e 29K .For generating 10GB of data we need to give 
350,000,000 as the range as per my calculation.

[localuser@localhost python_code]$ python data_generator.py



2)##########Mapper & Reducer Individual Run on the command line############


[localuser@localhost python_code]$ 
                                  cat input_data.csv|python mapper_project.py|sort

[localuser@localhost python_code]$ 
                                  cat input_data.csv|python mapper_project.py|sort|python reducer_project.py


3.#########Move files to hdfs:############


[localuser@localhost hadoop-2.6.0]$ 
                                    bin/hdfs dfs -copyFromLocal /home/localuser/python_code/input_data.csv /home/localuser/hadoop-2.6.0/input_localuser

[localuser@localhost hadoop-2.6.0]$ 
                                    bin/hdfs dfs -copyFromLocal /home/localuser/python_code/mapper_project.py /home/localuser/hadoop-2.6.0/mapreduce_codes

[localuser@localhost hadoop-2.6.0]$ 
                                    bin/hdfs dfs -copyFromLocal /home/localuser/python_code/reducer_project.py /home/localuser/hadoop-2.6.0/mapreduce_codes


4.############Run in Hadoop#############

[localuser@localhost hadoop-2.6.0]$  

bin/hadoop jar contrib/streaming/hadoop-*streaming*.jar \
-file /home/localuser/hadoop-2.6.0/mapreduce_codes/mapper_project.py    -mapper /home/localuser/hadoop-2.6.0/mapreduce_codes/mapper_project.py \
-file /home/localuser/hadoop-2.6.0/mapreduce_codes/reducer_project.py   -reducer /home/localuser/hadoop-2.6.0/mapreduce_codes/reducer_project.py \
-input /home/localuser/hadoop-2.6.0/input_localuser/input_data.csv -output /home/localuser/hadoop-2.6.0/output_localuser -output 


5.######### To Sort all partitions in the reducer globally use below in the command line######

-D mapreduce.partition.keypartitioner.options=-K1,1 
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner


