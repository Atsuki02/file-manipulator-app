import sys

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: <script> manipulator input_path output_path [newstring]")
        sys.exit(1)

manipulator = sys.argv[1]
input_path = sys.argv[2]
output_path = sys.argv[3]
newstring = sys.argv[4] if len(sys.argv) > 4 else None


def main(input_path, output_path, manipulator):

    contents = read_file(input_path)

    if manipulator == 'reverse':
        result = reverse(contents)
    
    elif manipulator == 'copy':
        result = copy(contents)
    elif manipulator == 'duplicate-contents':
        result = duplicate_contents(contents, output_path)
        output_path = input_path
    elif manipulator == 'replace-string':
        result = replace_string(contents, output_path, newstring)
        output_path = input_path
    else:
        print(f"Unknown manipulator: {manipulator}")

    write_file(output_path, result)


def read_file(file_path):
    # read input file
    with open(file_path, 'r') as f:
        return f.read()

def write_file(file_path, contents):
    # write contents in file_path
    with open(file_path, 'w') as f:
        f.write(contents)


def reverse(contents):
    # reverse contents and write
    return contents[::-1]

def copy(contents):
    # copy contents
    return contents

def duplicate_contents(contents, n):
    # duplicate input contents
    result = ''
    for _ in range(int(n) + 1):
        copy += contents
    return result

def replace_string(contents, needle, newstring):
    # replace needle with newstring
    return contents.replace(needle, newstring)


        



# call function
main(input_path, output_path, manipulator)