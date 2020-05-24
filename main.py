import sys
import os
from pathlib import Path

p = Path('.')
testing = open("kangewoon.java", "w")
for i in p.glob('**/*.java'):
    print(i.name)
    if i.is_file():
        print(i.absolute())
        with open(i.absolute()) as file:
            testing.write(i.name)
            testing.write(file.read())
