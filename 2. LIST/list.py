####### 1. Example of list
integers = [1,2,3,4]
#print(integers)

stringList = ['Milk', 'Cheese', 'Butter']
#print(stringList)

mixesList = [1,2,1.4,'spam']
#print(mixesList)

nestedList = [1,2,3,4,[1.45,1.6],['test']]
#print(nestedList)

empty = []
#print(empty)

######### 2. Accessing/traversing the list
shoppingList = ['Milk','Cheese','Butter']
#print(shoppingList[0])
#print('Bread' in shoppingList)
#print(shoppingList[-2])

#for i in shoppingList:
   # print(i)

#for i in range(len(shoppingList)):
    #shoppingList[i] = shoppingList[i] + '+'
   # print(shoppingList[i])

#empty = []
#for i in empty:
   # print("Empty")

########## 3.Update/insert a list
#Time : O(1) space : O(1)
List1 = [1,2,3,4,5,6,7]
#print(List1)
List1[2] = 33
List1[3] = 55
#print(List1)

#Insert : beginning - any given place - end - another list
myList = [1,2,3,4,5,6,7,8]
print(myList)
myList.insert(0,11) #O(n)
print(myList)

myList.append(55)#O(1) 
print(myList)

newList = [11,22,44]
myList.extend(newList)
print(myList)#o(n)


######### 4. slice/delete  from a list 
myList = ['a','b','c','d','e','f']
myList[0:2] = ['x','y']
print(myList[:])

#myList.pop() O(1)/O(n)
print(myList)

del myList[0:2] #O(n)
print(myList)

myList.remove('e')#O(n)
print(myList)

######### 5. Searching for an element in the list 
my_list = [10,20,30,40,50,60,70,80,90]
target = 50
if target in my_list:#time : O(n)
    print(f'{target} in my list')
else:
    print(f'{target} not found')

#linear search O(n)/O(1)
def linear_search(p_list, p_target):
    for i, value in enumerate(p_list): #O(n)
        if p_list[i] ==  p_target:
            return i
    return -1

print(linear_search(my_list,target))

######### 6. List operations/ functions
#Operations
a = [1,2,3]
b = [4,5,6]
c = a + b 
print(c)

d = [0,1]
d = d * 4
print(d)

#Function
e = [1,2,3,4,5,6,7]
print(len(e))
print(max(e))
print(min(e))
print(sum(e)/len(e))
#Exp :
total = 0
count = 0
while(True):
    inp = input('Enter your number: ')
    if inp == 'Done': break
    value = float(inp)
    total = total + value
    count += 1
    avg = total/count
print('Avg', avg)

my_new_list = list()
while(True):
    inp = input('Enter your number: ')
    if inp == 'Done': break
    my_new_list.append(float(inp))
print('Avg : ', sum(my_new_list) / len(my_new_list))

