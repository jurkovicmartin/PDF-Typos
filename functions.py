
import pymupdf
import re
import os

def load_dictionary(language: str) -> set:
    """
    Loads words from word list and returns them as set. 
    """
    if language == "en":
        try:
            with open("word_lists/english.txt", "r", encoding="utf-8") as file:
                return set(word.strip() for word in file)
        except FileNotFoundError:
            return
    elif language == "cs":
        try:
            with open("word_lists/czech.txt", "r", encoding="utf-8") as file:
                return set(word.strip() for word in file)
        except FileNotFoundError:
            return
    else:
        raise Exception("Unsupported language.")
    

def check_file_format(path: str) -> bool:
    """
    Checks for .pdf file format.
    """
    _, extension = os.path.splitext(path)

    if extension == ".pdf":
        return True
    else:
        print("You must insert path to .pdf file.")
        return False



def find_typos(path: str, dictionary: set):
    """
    Finds typos in a pdf file and print them to console and "typos.txt" file.
    """
    if not dictionary:
        print("Error. Word list has not been found.")
    
    # Open file for writing typos
    try:
        with open("typos.txt", "w", encoding="utf-8") as file:
            # Open the pdf
            doc = pymupdf.open(path)
            
            for page in doc:
                # Get text from a page
                text = page.get_text()
                # Clear the text from punctuation
                text = re.sub(r"[^a-zA-Z0-9\sáčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]", "", text)
                # Split text to words
                words = text.split()

                # Page typos counter
                typos = 0

                for word in words:
                    # Search the dictionary and print the word if it isn't there
                    if word.lower() not in dictionary:
                        print(f"Page: {page.number + 1}, Word: {word}")
                        file.write(f"Page: {page.number + 1}, Word: {word}\n")

                        typos += 1

                print(f"Summary: Page {page.number + 1} has {typos} typos.")
                file.write(f"Summary: Page {page.number + 1} has {typos} typos.\n\n")
                        
            doc.close()
            print("Checking has been completed. Result can be also found in typos.txt file.")

    except pymupdf.FileNotFoundError:
        print("File that had to been checked does not exists.")