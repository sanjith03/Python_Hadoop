#!/bin/sh
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-libjars itu-1.0-SNAPSHOT-jar-with-dependencies.jar \ 
-partitioner com.itu.bigdata.StudentPartitioner \
-jobconf mapreduce.partition.keypartitioner.options=-K1,2 \
-jobconf mapred.reduce.tasks=4 \ 
-numReduceTasks 10 \
-file mapper_project.py \   
-mapper mapper_project.py \
-file reducer_project.py   \
-reducer reducer_project.py \
-input project/sample1/input/* \
-output project/sample/output3
