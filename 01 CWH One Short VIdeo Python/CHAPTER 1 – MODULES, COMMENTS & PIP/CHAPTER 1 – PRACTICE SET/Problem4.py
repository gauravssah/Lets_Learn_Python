# 4. Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.

import os

# Specify the directory path
directory_path = '/23 DSA/06 Apna College'

# Get the list of all files and directories in the specified directory
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
