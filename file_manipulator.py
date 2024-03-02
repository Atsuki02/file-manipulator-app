import sys

manipulator = sys.argv[1]
input_path = sys.argv[2]
output_path = sys.argv[3]
newstring = sys.argv[4]


def main(input_path, output_path, manipulator):
    if manipulator == 'reverse':
        return reverse(input_path, output_path)
    
    elif manipulator == 'copy':
        return copy(input_path, output_path)
    elif manipulator == 'duplicate-contents':
        return duplicate_contents(input_path, output_path)
    elif manipulator == 'replace-string':
        return replace_string(input_path, output_path, newstring)
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

def replace_string(input_path, needle, newstring):
    # read input file
    with open(input_path) as f:
        contents = f.read()

    # replace needle with newstring
        replaced_string = contents.replace(needle, newstring)
        with open(input_path, 'w') as f:
            f.write(replaced_string)

        



# call function
main(input_path, output_path, manipulator)