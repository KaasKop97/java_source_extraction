import sys
import os
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description="Gets the source code of provided extension from a directory.")
parser.add_argument("directory", type=str)
parser.add_argument("file_extension", type=str)

args = parser.parse_args()
if args.directory:
    if args.file_extension:
        directory = Path(args.directory).absolute()
        with open(str(directory) + "/complete_source.txt", "w") as resulting_file:
            for i in directory.glob('**/*' + args.file_extension):
                if i.is_file():
                    with open(i.absolute()) as file:
                        resulting_file.write("Filename: " + i.name)
                        resulting_file.write("\n\n")
                        resulting_file.write(file.read())
                        resulting_file.write("\n\n")
