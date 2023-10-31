# Create a tuple
newTuple = ('a','b','c','d','e')
tuple1 = tuple('12345412')
print(tuple1)

#Accessing an element in list
#print(newTuple[-1])
#print(newTuple[1:3])
#print(newTuple[:])

#Travering a tuple
for i in newTuple:
    print(i)

for i in range(len(newTuple)):
    print(newTuple[i])

#Search for an element in tuple
print('a' in newTuple)

print(newTuple.index('c'))
def search(any_tuple, element):
    for i in range(len(any_tuple)):
        if any_tuple[i] == element:
            return f'The element is found at {i} index'
    return 'Not FOUND'

#Tuple operation/method
myTuple = (1,23,5,12,56,12)
myTuple1 = (1,2,45,5,3,1,2,5)
#print(myTuple*2) #repeat the tuple
print(4 in myTuple )

print(myTuple1.count(2))
print(myTuple1.index(1))
print(tuple([1,2,3,4]))