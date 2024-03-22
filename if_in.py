int_list = [1,3,5,3,6,9,38,28]
# for i in int_list:
#     if i%2 == 0:
#         int_list2.append(i)

# print(int_list2)


int_list2 = [i for i in int_list if i%2 == 0]

print(int_list2)