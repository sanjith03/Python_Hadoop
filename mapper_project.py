#!/usr/bin/env python
 
import sys
 
# input comes from STDIN (standard input)
for line in sys.stdin:
    try: 
         
        # remove leading and  trailing whitespaces
        line = line.strip()
         
        split_columns = line.split(",")
        ID = split_columns[0]
        Name = split_columns[1]
        College = split_columns[2]
        Age = split_columns[3]
        
        print '%s\t%s\t%s\t%s' % (College,Name,Age,ID)
    except: #Erros are going to make your job fail if you want otherwise just pass it
        pass

