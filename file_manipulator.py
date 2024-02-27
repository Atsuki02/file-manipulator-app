import sys

input_path = sys.argv[2]
output_path = sys.argv[3]

print(input_path, output_path)


# read input file
with open(input_path) as f:
    contents = f.read()

# reverse contents and writ
with open(output_path, 'w') as f:
    f.write(contents[::-1])