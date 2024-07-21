
from functions import *

def main():
    # Infinite loop (keep console running)
    while(True):
        # Selecting file that will be checked
        while(True):
            file_path = input("Insert file path:\n")

            if check_file_format(file_path):
                break

        # Selecting language of the file
        while(True):
            language = input("Choose language:\n1 - English\n2 - Czech\n")
        
            if language == "1":
                language = "en"
                break
            elif language == "2":
                language = "cs"
                break
            else:
                print("Invalid choice.\n")


        dictionary = load_dictionary(language)

        find_typos(file_path, dictionary)

        action = input("\nChoose action:\n1 - Check another file\n0 - Exit\n")

        if action == "0":
            break






if __name__ == "__main__":
    main()