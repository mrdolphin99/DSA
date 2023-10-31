######### 7. Strings and lists
a = 'spam'
b = list(a)
c = 'Spam spam spam'
d = c.split()
c2 = 'Spam-spam-spam'
delimiter = '-'
delimiter2 = 'a'
d2 = c2.split(delimiter)
print(d2)
print(d)
print()

######### 8.  list comprehension
prev_list = [1,2,3]
new_list = [i*2 for i in prev_list]
print(prev_list)
print(new_list)

######### 9.  list comprehension with condition
prev =  [-1,10,20,2,-1234,123,1223]
new = [num*num for num in prev if num > 0]
print(new)

sentence  = 'My name is Loc'
def is_consonant(letter):
    vowels = 'aieou'
    return letter.isalpha() and letter.lower() not in vowels

print(is_consonant('t'))
consonant = [i for i in sentence if is_consonant(i)]
print(consonant)

new2 = [num if num > 0 else 0 for num in prev]
print(new2)

def get_number(number):
    if number > 0: return number
    else: return 'Negative number'

new3 = [get_number(num) for num in prev]
print(new3)