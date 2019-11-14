#  Python zip Function


# all=dir('__builtin__')
# print( 'zip' in all)

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

zipped=zip(letters , numbers)
# print(zipped)
# print(list(zipped))


my_zip=zip()

# next return a ittrator 

# print(next(my_zip))




from itertools import zip_longest
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
flotas=range(12)

combined_list=[]
zipped=zip_longest(flotas, letters , numbers ,fillvalue='?')
for i in list(zipped):
    for j in i:
        combined_list.append(j)

# print(zipped)



# python dictionaries

dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
     print(k1, '->', v1)
     print(k2, '->', v2)



# dict_one={'name':'Usman' , 'name':'Imran' ,'name':'asad'}
# for name_v , name  in zip(dict_one.items):
#     print(f'{name_v} of {name} is {name} ')












