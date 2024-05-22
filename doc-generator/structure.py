import os
import sys


def generate_structure(directory):
    structure = ""
    for root, dirs, files in os.walk(directory):
        ignored_dirs = ["var", ".git", "vendor"] 
        for ignored_dir in ignored_dirs:
            if ignored_dir in dirs:
                dirs.remove(ignored_dir)
        depth = root.replace(directory, '').count(os.sep)
        indent = '    ' * depth
        if depth == 0:
            structure += f"{indent}- {os.path.basename(root)}\n"
        else:
            structure += f"{indent}+ {os.path.basename(root)}\n"
    return structure

def write_to_file(structure, output_file):
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(output_file, "w") as file:
        file.write("# Structure\n\n")
        file.write("```\n")
        file.write(structure)
        file.write("```\n\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 generator.py <directory> <output_file>")
        sys.exit(1)

    directory = sys.argv[1]
    output_file = sys.argv[2]

    structure = generate_structure(directory)
    write_to_file(structure, output_file)
