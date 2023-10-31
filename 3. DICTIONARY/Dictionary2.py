'''
Dictionary operations / builtin funct
Dictionary comprehension

'''

myDict = {
    3 : 'Three',
    5 : 'Five',
    9 : 'Nine',
    2 : 'Two',
    1 : 'One',
    4 : 'Four'
}

#Check key
print(3 in myDict)
#Check value
print('One' in myDict.values())
#Check len
print(len(myDict))
#all, any
print(all(myDict))
print(any(myDict))
#Sort 
print(sorted(myDict))

#Dictionaray comprehension
import random
city_names = ['Paris','London', 'Rome', 'Berlin', 'Madrid']
new_dict = {city:random.randint(20,30) for city in city_names}
print(new_dict)

city_temp = {city: tem for (city, tem) in new_dict.items() if tem>25}
print(city_temp)