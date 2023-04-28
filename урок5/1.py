my_file = open('file.txt', 'w')
while True:
    my_text = input('Введите текст, для завершения оставте поле пустым')
    if my_text == '':
        break
    my_file.write(my_text+'\n')
my_file.close()
