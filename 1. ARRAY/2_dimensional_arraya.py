import numpy as np

#1. Create 2D array
#Time complexity : O(m.n) - space : O(m.n)
twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)

#2. Insert into 2 D array
newTwoDArray = np.insert(twoDArray,1,[[1,2,3,4]], axis = 0)
print(newTwoDArray)

newTwoDArray1 = np.append(twoDArray,[[1,2,3,4]], axis = 0)
print(newTwoDArray1)

#3. Access an element of 2d array
def accessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]): #O(1)
        print("incorrect index")#O(1)
    else:#O(1)
        print(array[rowIndex][colIndex])#O(1)
    
accessElement(twoDArray,1, 2)

#4. Traversing 2D array 
def traverse(array):
    for i in range(len(array)): #Loop through row time : O(mn)
        for j in range(len(array[0])): #loop through col O(n)
          print(array[i][j]) 
traverse( twoDArray)
# O(n^2) space O(1)

#5. Searching 2D array linear search
def search(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at index ' + str(i) +" "+ str(j)
    return 'Not Found'
print(search(twoDArray, 12))
# O(n^2) space O(1)