import sys
import os

def mass_renamer(d, nf, x):
    '''
    mass renamer: rename shit 
    '''
    counter = 1

    current_dir = os.getcwd()

    os.chdir(d)

    file_list = os.listdir(d)
    file_list.sort(key=os.path.getmtime)

    for file in file_list:
        if str(file).endswith(x):
            print('Renaming File: {} to File: {}'.format(file, nf + str(counter) + x))
            os.rename(file, nf + str(counter) + x)
            counter += 1

    os.chdir(current_dir)

def main():
    '''
    doc stringy
    '''
    directory, newFileName, ext = sys.argv[1], sys.argv[2], sys.argv[3]

    mass_renamer(directory, newFileName, ext)

if __name__ == '__main__':
    main()
