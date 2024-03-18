import sys
import re
import os
import time

filename = sys.argv[1]
node = sys.argv[2]
#column_size = int(column_size)
path = "/"

filepath = filename

input_data = sys.stdin 
next(input_data)
print(input_data)

substring = "Hit Ctrl-C"
file_exists = os.path.exists(filepath)
if file_exists:
    file_size = os.stat(filepath)
    if file_size.st_size == 0:
        with open(filepath, "a") as f: 
            f.write("node,min_usecs,max_usecs,count\n")
else:
    with open(filepath, "a") as f: 
        f.write("node,min_usecs,max_usecs,count\n")        
"""
for line in input_data: 
    if substring in line:
        next(input_data)
        break


if substring in input_data:
    next(input_data)
"""  
for line in input_data: 
    line = line.replace(' ','')

    if '->' not in line:
        continue
        """
        if ':' in line:
    	    header = line.split(":")
    	    for col in header:
    	        print(col+",")
    	        continue

        else:
            continue
        """


    parts = line.split(":")
    msecs_range = parts[0].strip().split('->')
    min_msecs = msecs_range[0].strip()
    max_msecs = msecs_range[1].strip()
    count = parts[1].strip('|')[0].strip()
    data = node+','+min_msecs+','+max_msecs+','+count+"\n"     
    if(count != '0'):
        #time.sleep(2)
        with open(filepath, "a") as f: 
            f.write(data)
        print(data)

