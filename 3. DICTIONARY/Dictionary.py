#1. Creating dict

my_dict = dict(one='uno', two='dos', three='tres')
#print(my_dict)
my_dict2 = {'one':'uno', 'two':'dos', 'three':'tres'}
#print(my_dict2)
my_dict3 = [('one','uno'), ('two','dos'), ('three','tres')]
#print(my_dict3)

#2. Update/add an element to the dictionary
myDict = {'name':'Edy', 'age':26,'address':'London','Education':'Master'}
myDict['address'] = 'London'
print(myDict)

#3. TRaversing through a dictionary
def traverseDict(dict):
    for key in dict:
        print(key, dict[key])
traverseDict(myDict)

#4. Search
def searchDict(dict,value):
    for key in dict:
        if dict[key] == value:
            return key,value
    return 'Not exist'

print(searchDict(myDict,26))

#5.Remove/delete from a dict
#del myDict['age']
print(myDict)

removed_element = myDict.pop('name',None)
print(removed_element)

#myDict.clear()

#6. Dictionary method
dict = myDict.copy()

#Create new dict using fromkeys
newDict ={}.fromkeys([1,2,3],0)
print(newDict)

#get, items, keys method
print(myDict.get('age',27))
print(myDict.items())

#keys 
print(myDict.keys())

#values
print(myDict.values())

#popitem method
print(myDict.popitem())
print(myDict)

#setdefault()
print(myDict.setdefault('name','added'))
print(myDict)

#pop()
print(my_dict.pop('name','not'))

#update
newDict2 = {'a':1, 'b':2, 'c':3}
myDict.update(newDict2)
print(myDict)