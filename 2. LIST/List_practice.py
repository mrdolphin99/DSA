''' #### 1.
Missing Number
Write a function to find the missing number in a given integer array of 1 to 100.

Example

missing_number([1, 2, 3, 4, 6], 6) # 5
'''
#Solution 1
def missing_number(arr,value):
    for i in range(1,len(arr)):
        if arr[i + 1] - arr[i] != 1:
            return arr[i] + 1 
    return 0
#Solution 2
def missing_num2(arr,value):
    sum_expect = value(value + 1) // 2
    real_sum = sum(arr)
    missing = sum_expect - real_sum
    return missing

''' #### 2.
Write a program to find all pairs of  intergers whose sum is 
equal to a given number

Problem? :
    - Does arr contain only positive or negative numbers
    - What if the same pair repeat twice, print it everytime?
    - If the reverse off the pair is acceptable?
    - Do we need to print only distinct pairs?
    - How big is a query?

Example

[2,6,3,9,11] 9-> [6,3]
'''
def two_Sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

#solution 2
def findPair(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]: continue
            elif nums[i] + nums[j] == target: 
                print(i,j)

''' #### 3.
How to check if an array contains a number 
'''

def findNum(arr,number):
    for i in range(len(arr)):
        if arr[i] == number:
            print(i)
    
#my_array = [1,2,3,4,5,51,23,12]
#findNum(my_array,3)

'''#### 4.
Max Product of Two Integers
Find the maximum product of two integers in an array where all elements are positive.

Example

arr = [1, 7, 3, 4, 9, 5] 
max_product(arr) # Output: 63 (9*7)
'''
def maxProduct(array):
    array.sort(reversed=True)
    return array[0]*array[1]

#solution 2:
def maxProduct2(arr):
    max1, max2 = 0, 0
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
        elif i < max1:
            max2 = i 
    return max2 * max1

'''#### 5.
Middle Function
Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

myList = [1, 2, 3, 4]
middle(myList)  # [2,3]
'''
def middle(lst):
    return lst[1:-1]
myList = [1, 2, 3, 4]
middle(myList)

"""#### 6.

2D Lists
Given 2D list calculate the sum of diagonal elements.

Example

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
diagonal_sum(myList2D) # 15

"""
def diagonal_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                sum = sum + matrix[i][j]
    return sum

#solution 2
def ds2(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    
    return sum

'''#### 7.
Best Score
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList) # 90 87
'''
def best_second_score(myList):
    max1, max2 = 0, 0
    for i in myList:
        if i > max1:
            max2 = max1 
            max1 = i 
        if i > max2 and i != max1:
            max2 = i 
    return max1, max2

'''#### 8.
Duplicate Number
Write a function to remove the duplicate numbers on given integer array/list.

Example

remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]
'''
def duplicate(arr):
    new_lst = []
    seen = set()
    for i in arr:
        if i not in seen:
            new_lst.append(i)
            seen.add(i)
    return new_lst

'''#### 9.

Pairs
Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

Example

pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']


Note:

4+3 comes from second and third elements from the main list.

3+4 comes from third and seventh elements from the main list.
'''
def pair_sum(myList, sum):
    result = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == sum:
                result.append(f'{myList[i]} + {myList[j]}')
    return result

'''#### 10.
Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :

Input: nums = [1,2,3,1]
Output: true
Hint: Use sets
'''

def contains_duplicate(nums):
    for i in range(len(nums)):
        if nums[i] in nums[i+1:]:
            return True
    return False

#solution2: 
def contains_duplicate2(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.append(i)
    return False

'''#### 10.
Permutation
'''

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False 
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True 
    else:
        return False
#EXP :
list1 = [1,2,3]
list2 = [2,4,5]
print(permutation(list1,list2))