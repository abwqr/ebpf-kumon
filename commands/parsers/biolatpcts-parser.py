import sys
import csv
import os


def main():
    filename = sys.argv[1]
    path = "/home/ubuntu/fyp/bcc_data/"
    filepath = path+filename+".csv"
    print(filepath)
    file_exists = os.path.exists(filepath)
    is_empty = 0
    if file_exists:
        file_size = os.stat(filepath)
        if file_size.st_size == 0:
            is_empty = 1
    else:
        is_empty = 1


    for line in sys.stdin:
        if is_empty:
            header = "operation,1,5,10,16,25,50,75,84,90,95,99,100\n"
            #csv_writer.writerow(header)
            print(header)
            with open(filepath, "a") as f: 
                f.write(header)
            is_empty = 0
            continue
            
        parts = line.split()

        if len(parts) >= 13:
            operation = parts[0]

            values = [f"{float(val[:-2]) / 1000:.3f}" if val.endswith('us') else f"{float(val[:-2]):.3f}" if val.endswith('ms') else val for val in parts[1:]]
            lineval = ""
            for data in values:
                if data == '-':
                    lineval = lineval+'0'+","    
                    continue
                lineval = lineval+data+","
            if operation == 'read' or operation == 'write':
                print(operation,lineval[:-1])
                with open(filepath, "a") as f: 
                    file_input = operation+','+lineval[:-1]+'\n'
                    f.write(file_input)

                
                
if __name__ == "__main__":
    main()

