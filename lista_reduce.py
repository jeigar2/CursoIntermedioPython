from functools import reduce

my_list = [2,2,2,2,2]
print(reduce(lambda x, y: x*y, my_list))