def read_from_file():
    words = []
    file_to_open = open('test_document.txt')
    content = file_to_open.readlines()

    for lines in content:
        words.append(lines.split(' '))
    
    for word in words:
        print(word)


    file_to_open.close()

read_from_file()