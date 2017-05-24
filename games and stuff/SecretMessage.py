import os

def rename_files():
    # get the file names from a given folder
    file_names = os.listdir(r'D:\pythonProjects\prank')
    # get the current working directory
    saved_directory = os.getcwd()
    # Change the current working directory
    os.chdir(r'D:\pythonProjects\prank')
    #rename the files

    #get the file name from the list of file names and rename  the file to the file name but with out any numbers
    for file in file_names:
        print('Renaming file: {} to : {}'.format(file, file.lstrip("0123456789")))
        os.rename(file, file.lstrip("0123456789"))
    # Change the current directory back to the orignal working directory
    os.chdir(saved_directory)
    
rename_files()