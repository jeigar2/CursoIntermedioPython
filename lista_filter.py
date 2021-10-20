my_list = [1,4,5,6,9,13,19,21]
# -- modo 1
# index = 0
# for i in my_list:
#     print (i, index, my_list)
#     if(i%2 == 0):
#         list2.append(i)
#     index += 1
# -- modo 2
#list2 = [i for i in my_list if i%2 != 0]
# -- modo 3
list2 = list(filter(lambda x: x%2 != 0, my_list))
print (list2)