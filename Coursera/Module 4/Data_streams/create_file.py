#!/usr/bin/env python3

import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)


# RUN BELOW IN CLI
# ./create_file.py example
# echo $?
# 0

# cat example 
# New file created
# ./create_file.py example
# Error, the file example already exists!
# echo $?
# 1