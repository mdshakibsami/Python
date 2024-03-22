
cards = {1111,2,3,4,3623625,6,7,8,9,10203,10,100,10}
number_list = list(cards)
max = number_list[0]
for number in number_list:
    if number>max:
        max = number

print(max)
