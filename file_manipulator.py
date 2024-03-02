import sys

manipulator = sys.argv[1]
input_path = sys.argv[2]
output_path = sys.argv[3]


def main(input_path, output_path, manipulator):
    if manipulator == 'reverse':
        return reverse(input_path, output_path)
    
    elif manipulator == 'copy':
        return copy(input_path, output_path)
    elif manipulator == 'duplicate-contents':
        return duplicate_contents(input_path, output_path)
    else:
        print(f"Unknown manipulator: {manipulator}")


def reverse(input_path, output_path):
    # read input file
    with open(input_path) as f:
        contents = f.read()

    # reverse contents and write
    with open(output_path, 'w') as f:
        f.write(contents[::-1])

def copy(input_path, output_path):
    # read input file
    with open(input_path) as f:
        contents = f.read()

    with open(output_path, 'w') as f:
        f.write(contents)

def duplicate_contents(input_path, n):
    # read input file
    with open(input_path) as f:
        contents = f.read()

    # duplicate input contents
    with open(input_path, 'w') as f:
        for _ in range(int(n) + 1):
            f.write(contents)

        



# call function
main(input_path, output_path, manipulator)