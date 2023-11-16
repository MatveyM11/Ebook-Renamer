import os
import zipfile

def rename_epub_books(folder_path):
    # get all files in the specified folder
    files = os.listdir(folder_path)

    # iterate over the files
    for file in files:
        # check if the file is an epub file
        if file.endswith(".epub"):
            # open the epub file
            with zipfile.ZipFile(file, 'r') as myzip:
                # get the content.opf file from the epub archive
                opf_file = [f for f in myzip.namelist() if f.endswith('content.opf')][0]
                # read the content of the content.opf file
                opf_content = myzip.read(opf_file).decode('utf-8')

                # extract the title of the book from the content.opf file
                book_title = opf_content.split("<dc:title>")[1].split("</dc:title>")[0]

                # extract the author of the book from the content.opf file
                book_author = opf_content.split("<dc:creator>")[1].split("</dc:creator>")[0]

                # rename the file
                os.rename(file, book_title + " - " + book_author + ".epub")

# specify the folder containing the .epub files
folder_path = "./" #Current directory of the script

# rename the .epub books
rename_epub_books(folder_path)
