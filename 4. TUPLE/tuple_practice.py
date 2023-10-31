'''#### 1.
Sum and Product
Write a function that calculates the sum and product of all elements in a tuple of numbers.

Example

input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)  # Expected output: 10, 24
'''
def sum_product(input_tuple):
    sum = 0
    product = 1
    for i in input_tuple:
        sum = sum + i 
        product = product * i 
    return sum, product

'''#### 2.
Elementwise Sum
Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

Example

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)  # Expected output: (5, 7, 9)
'''
 
def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum,zip(tuple1,tuple2)))

#Solution 2
def tuple_elementwise_sum2(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError('MUST HAVE THE SAME LENGTH')
    result = tuple(a + b for a,b in zip(tuple1,tuple2))
    return result

'''#### 3.
Insert at the Beginning
Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.

Example

input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)  # Expected output: (1, 2, 3, 4)
'''

def inser_at_begin(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple

''' ####4.
Concatenate
Write a function that takes a tuple of strings and concatenates them, separating each string with a space.

Example

input_tuple = ('Hello', 'World', 'from', 'Python')
output_string = concatenate_strings(input_tuple)
print(output_string)  # Expected output: 'Hello World from Python'
'''

def concatenate_strings1(input_tuple):
    return ' '.join(input_tuple)

def get_diagonal(tup):
    temp = []
    for i in tup:
        temp.append([i])
    return temp
input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print(get_diagonal(input_tuple))