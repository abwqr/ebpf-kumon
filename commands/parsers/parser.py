import sys
import re
import os

filename = sys.argv[1]
column_size = sys.argv[2]
column_size = int(column_size)
flags = 0
path = "parsers/"

filepath = path+filename+".csv"
print(filepath)
input_data = sys.stdin 

file_exists = os.path.exists(filepath)
if file_exists:
    file_size = os.stat(filepath)
    if file_size.st_size > 0:
        flags = 2
    else:
        flags = 1
tracing_line = 0
for line in input_data:

    if 'Socket' in line:
        continue
    if "Ctrl-C" in line:
        continue

    if 'COMM' in line and flags == 2:
        continue
    

    columns = re.split(r'\s+', line.strip())
    print(len(columns))
    if column_size < len(columns):
        loop_len = column_size
    else:
        loop_len = len(columns)
        
    data = ""
    for col in range(0, loop_len-1):
        data = data+columns[col]+','
            
    data = data+' '.join(columns[loop_len-1:])+"\n"
    with open(filepath, "a") as f: 
        f.write(data)
        print(data)
