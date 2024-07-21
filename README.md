# PDF-Typos

Simple console application to spot typos in pdf files. Application navigation is done in console where user needs to input path to the pdf file, that will be checked, and language of that file. Supported languages are English and Czech. Result is also printed to the console in "Page: ,Word: " format. Same print is also written to a text file. The result text file is named "typos.txt" and is located in the same directory as "functions.py" file.

## Functionality

Text is loaded from file using PyMuPDF package. As words dictionary word lists are used (these lists were taken from https://github.com/kkrypt0nn/wordlists). Every word of the loaded text is trying to be found in the dictionary. If the word isn't there it is printed to the console and to the result text file.

*Note: Because of word lists solution some words are assessed as a typos but actually they are correct (they are just not mentioned in the word list)*