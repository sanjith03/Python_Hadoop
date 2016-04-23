#!/usr/bin/env python

import sys


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py


    College,Name,Age,ID = line.split('\t')
    
    # currentKey = '%s\t%s' % (College,Name,Age,ID)

     #Write results to STDOUT
     
    print '%s\t%s\t%s\t%s' % (College,Name,Age,ID)

