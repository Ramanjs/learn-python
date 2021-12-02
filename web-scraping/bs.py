from bs4 import BeautifulSoup
# import os
# os.chdir('..\\portfolio-page\\')
html_file = open('..\\portfolio-page\\index.html') # as we used to open txt files without any mode

# making the soup
soup = BeautifulSoup(html_file) # returns the processed html file
# soup variable contains the processed html file
# print(soup.text)


print(soup.title)
print(soup.h1)