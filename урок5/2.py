my_file = open('my_file.txt', 'r')
cont = my_file.readlines()
print(f'Кол-во строк : {len(cont)}')
x = 0
for i in cont:
    words = i.split(' ')
    x += 1
    print(f"Слов в строке {x} : {len(words)}")
