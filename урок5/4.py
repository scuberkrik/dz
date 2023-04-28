with open('file4.txt', 'r') as file:
    lst = list()
    for y in file.readlines():
        lst.extend(y.split(' '))
rus_lst = ["Один", "Два", "Три", "Четыре"]

x = 0
for i in range(0, len(lst), 3):
    lst[i] = rus_lst[x]
    x += 1

out_file = open('file4.1.txt', 'w', encoding='UTF-8')
out_file.writelines(lst)
out_file.close()
