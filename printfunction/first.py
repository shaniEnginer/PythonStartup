
# # #  Experiment with print function in Python 

# # 'A line of text.\n'.rstrip()




# # #  Formating string 

# # name="Entity"


# import  os 

# print(f' Hello {os.getlogin()} ')

# # None is a key word In Python 
# # print(None)


# #  Seprater In Pyton 
# # print('hell','World' , sep=" \n")

# # my_list=['Inran' , 'Ali' ]
# # print(my_list ,'Test', sep=" - ")

# print(*['print '])


# # print(' Test ' ,end=" ..")

# # print(f' {name} ')


# # my_list = [1, 2, 3]
# # print(*my_list)
# # sum_integers_args_3.py

# def my_sum(*args):
#     result = 0
#     for x in args:
#         result += x
#     return result

# list1 = [1, 2, 3]
# list2 = [4, 5]
# list3 = [6, 7, 8, 9]

# print(my_sum(*list1, *list2, *list3))


print('home', 'user', 'documents', sep='/')
# help(print)














with open('first.txt') as txtfile:
    for txt in txtfile:
        print(txt ,end='')



