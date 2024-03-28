import sys
import os
def parse_output(output,filename):
    parsed_data = []
    lines = output.split('\n')
    headers = lines[0].split()
    # for line in lines[1:]:
        
    #     if not line.strip():  # Skip empty lines
    #         continue

    fields = lines[0].split()
    parsed_entry = {}
    data = ""
    print("fields",fields)
    for i in range(0, len(fields)):
      if i == len(fields)-1: 
       

        if "µs" in fields[i]:
          fields[i] = fields[i].replace("µs", "")
          print("µs", fields[i])
        elif "ms" in fields[i]:
          fields[i] = fields[i].replace("ms", "")
          value = float(fields[i])
          value = value*1000 
       	  fields[i] = str(value)
          print("ms", fields[i])
        elif "s" in fields[i]: 
          fields[i] = fields[i].replace("s", "")
          value = float(fields[i])
          value = value*1000000 
       	  fields[i] = str(value)
          print(fields[i])

        
      data = data + fields[i] + ","

    print("data",data)
    
    with open(filename, 'a') as f:
        f.write(data[:-1] + '\n')
    # return parsed_data

def contains_headers(header, line):
    headers = header.split(',')
    return all(header in line for header in headers)
    
    # Check if the line contains the specified headers
    #headers = ["K8S.NODE", "K8S.NAMESPACE", "K8S.POD", "K8S.CONTAINER"]
    #return all(header in line for header in headers)
if __name__ == "__main__":
    print(len(sys.argv))
    if(len(sys.argv)>1):
        filename = sys.argv[1]
        header = sys.argv[2]
        #print(filename)
        for line in sys.stdin:
            
            try:
                if( os.stat(filename).st_size > 0): # false if not empty
                    if(not contains_headers(header,line)):   
                        parse_output(line,filename)
                else:
                    parse_output(header,filename)
                    #print(line)

            except FileNotFoundError:
                parse_output(header,filename)
                #print(line)
