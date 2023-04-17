new_file = open('file5.txt', 'w')
num = input('Введите числа через пробел: ')
new_file.write(num)
new_file = open('file5.txt', 'r')
my_list = new_file.read().split()
n = 0
for i in my_list:
    n += int(i)
print(n)
