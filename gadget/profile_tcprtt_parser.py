import sys
import re
import os

filename = sys.argv[1]
node = sys.argv[2]
path = "/"
filepath = filename

input_data = sys.stdin
#next(input_data)  # Skip the first line

# Check if the file already exists and write header if necessary
file_exists = os.path.exists(filepath)
if not file_exists or os.stat(filepath).st_size == 0:
    with open(filepath, "a") as f:
        f.write("node,average\n")

# Regular expression pattern to extract the numeric value within "[AVG ]"
pattern = r"\[AVG (\d+\.\d+)\]"

for line in input_data:
    # Check if the line contains "All Addresses"
    if "All Addresses" in line:
        # Extract the numeric value using regular expression
        match = re.search(pattern, line)
        if match:
            avg_value = match.group(1)
            # Write the numeric value to the file
            with open(filepath, "a") as f:
                f.write(node + "," + avg_value + "\n")
            print(node,avg_value)  # Print the value for confirmation
