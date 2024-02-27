import sys

manipulator = sys.argv[1]
input_path = sys.argv[2]
output_path = sys.argv[3]


def operate(input_path, output_path, manipulator):
    if manipulator == 'reverse':
        return reverse(input_path, output_path)
    else:
        print(f"Unknown manipulator: {manipulator}")


def reverse(input_path, output_path):
    # read input file
    with open(input_path) as f:
        contents = f.read()

    # reverse contents and write
    with open(output_path, 'w') as f:
        f.write(contents[::-1])

# call function
operate(input_path, output_path, manipulator)