# Way to a file is its path
# C:\Users\Ramanjeet Singh\Documents\learn-python\file-handling\paths.py
# Folder aka directory
# Current working directory
import os # operating system module
wd = os.getcwd()
print(wd)

# Absolute vs relative paths
# Path which starts from root (C:)
# Relative path is the path from our current point of view
# \some-folder\new-file
# to go backward we write two dots
# ..\basics\flow-control.py

# Change directory
os.chdir('.\\some-folder')
wd = os.getcwd()
print(wd)


# File handling
# in read mode we can only read it
new_file = open('new-file.txt')
text_content = new_file.read()
print(text_content)
new_file.close()

# Writing to files
# opening file in write mode
# in write mode we can read as well as edit the file
new_file = open('new-file.txt', 'w')
new_file.write('New World!')
# Write function overites the existing text
new_file.close()

# new_file = open('new-file.txt', 'r')
# print(new_file.read())

# Append mode
# Adding on text
new_file = open('new-file.txt', 'a')
new_file.write('\nAdding new line at the end')
new_file.close()

# Reoppening in read mode
new_file = open('new-file.txt')
print(new_file.read())


# Newline character is \n
string_var = "This is\n a line"
print(string_var)

# plaintext and binary files
# .txt are plaintext 
# pdf, word, excel, binary files
# We need to download external module to edit binary files


# Escape characters and raw strings
# in raw strings python ignores escape characters
# Newline character
string_var = r"This is\n a string"
print(string_var)

# Tab character
string_var = "this is\t a string"
print(string_var)

string_var = "this is\\ a string"
print(string_var)

# Opening a nonexistant filename in write or append mode will create that file
new_file = open('myfile.txt', 'w')
new_file.write('Just created this file from inside py program')
new_file.close()

# shutil copy and move functions
import shutil
# copy() funciton takes two arguments 
# ('source', 'destination') 
# single dot means current directory
# double dot means parent directory
shutil.copy('new-file.txt', '.\\new-folder\\other-name.txt')
# ..\file-handling\new-file.txt
# cut and paste -> move()
shutil.move()