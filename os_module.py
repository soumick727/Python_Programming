# Write a python program to print the contents of a directory using the os module.

# ✅ Which function do we use from the os module?
# We can use os.listdir() to list the contents (files and folders) of a directory.

import os

directory_path = '.'  #for current directory

directory_path2 = 'D:\coding round problem(1)\coding-problems' #for a specific directory

contents = os.listdir(directory_path)

print("Contents of the directory:")
for item in contents:
    print(item)

contents2 = os.listdir(directory_path2)

print("Contents of the directory:")
for item in contents2:
    print(item)