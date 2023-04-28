import re

with open('file6.txt') as file:
    my_dict = {}
    my_lines = file.readlines()
    for line in my_lines:
        if len(line):
            x = re.split("[: ]", line)
            hours_sum = 0
            for hours in x[1:]:
                if len(hours) > 1:
                    hours_sum += int(hours.split('(')[0])
            my_dict[x[0]] = hours_sum
    print(my_dict)
