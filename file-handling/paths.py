# Way to a file is its path
# C:\Users\Ramanjeet Singh\Documents\learn-python\file-handling\paths.py
# Folder aka directory
# Current working directory
import os # operating system
wd = os.getcwd()
print(wd)

# Absolute vs relative paths
# Path which starts from root (C:)
# Relative path is the path from our current point of view
# \some-folder\new-file
# to go backward we write two dots
# ..\basics\flow-control.py

# Change directory
os.chdir(r'some-folder')
wd = os.getcwd()
print(wd)


# File handling
# in read mode we can only read it
# new_file = open('new-file.txt')
# text_content = new_file.read()
# print(text_content)
# new_file.close()

# Writing to files
# opening file in write mode
# in write mode we can read as well as edit the file
new_file = open('new-file.txt', 'w')
new_file.write('New World!')
# Write function overides the existing text
new_file.close()

new_file = open('new-file.txt', 'r')
print(new_file.read())

# Append mode
# Adding on text
new_file = open('new-file.txt', 'a')
new_file.write('\nAdding new line at the end')
new_file.close()

# Reoppening in read mode
new_file = open('new-file.txt')
print(new_file.read())


# Newline character is \n
# 
# string_var = "This is\n a line"
# print(string_var)