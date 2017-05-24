def read_from_file():
    file_to_open = open('test_document.txt')
    content = file_to_open.read()
    print(content)
    file_to_open.close()

read_from_file()