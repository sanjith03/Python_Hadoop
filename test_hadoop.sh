#!/bin/sh
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-file ./mapper_project.py -mapper ./mapper_project.py \
-file ./reducer_project.py -reducer ./reducer_project.py \
-input /user/hadoop/sample1/input/* \
-output /user/hadoop/test-output
