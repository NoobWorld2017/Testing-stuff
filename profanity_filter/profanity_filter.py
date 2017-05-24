import urllib.request

def read_from_file():
    file_to_open = open('test_document.txt')
    content = file_to_open.read()
    full_formated_string = str(content).replace('\n', ' ').replace(' ', '%20')
    file_to_open.close()
    check_profanity(full_formated_string)


def check_profanity(text_to_check):
    url = r"http://www.purgomalum.com/service/xml?text={}".format(text_to_check)
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf-8'))

read_from_file()