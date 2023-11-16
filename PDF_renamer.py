import PyPDF2
import os

def rename_pdf_files(folder_path):
    # get all files in the specified folder
    files = os.listdir(folder_path)

    # counter to keep track of the problematic files
    problematic_file_counter = 1

    # iterate over the files
    for file in files:
        # check if the file is a PDF file
        if file.endswith(".pdf"):
            # open the PDF file
            try:
                with open(file, 'rb') as f:
                    pdf_file = PyPDF2.PdfReader(f)

                    # extract the title of the book from the PDF file
                    book_title = pdf_file.metadata.get('/Title', '')

                    # rename the file
                    if book_title:
                        os.rename(file, os.path.join(folder_path, book_title + ".pdf"))
                    else:
                        pass
            except Exception as e:
                # store the problematic file in a file called Failed.md
                with open("Failed.md", 'a') as f:
                    f.write(f"{problematic_file_counter}. {file}\n")
                    problematic_file_counter += 1

# specify the folder containing the .pdf files
folder_path = "./"

# rename the .pdf books
rename_pdf_files(folder_path)
