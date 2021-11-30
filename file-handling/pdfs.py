import PyPDF2
import os
os.chdir('..\\..\\backup\\books') # change to directory where books are stored
file = open('htmlguide-latest.pdf', 'rb') # open the pdf in read binary mode ('rb')
# reader object
# PdfFileReader() which takes argument the pdf file
# It returns a python processed pdf file
reader = PyPDF2.PdfFileReader(file)
page4 = reader.getPage(3)
text_content = page4.extractText()
print(text_content)