names = ['Tom', 'Owen', 'Sarah', 'Janet']
age =[34, 14, 36, 64]

zipped_list = zip(names, age)

for i in zipped_list:
    print('Name = ' + i[0] + ' Age = ' + str(i[1]))
