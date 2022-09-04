from itertools import product
import math
from tabnanny import check


print("----Vol of sphere----")

def vol(rad):
    return (4/3) * (math.pi) * (rad **3)

print(vol(2))    

print("----number is in a given range----")

def ran_check(num,low,high):
    if num in range(low,high + 1):
        return f"{num} is in the range between {low} and  {high}"

print(ran_check(7,2,7))

def ran_bool(num,low,high):
    return num in range(low,high + 1)

print(ran_bool(3,1,10))


print("---- calculates the number of upper case letters and lower case letters----")

def up_low(s):
    d = {'upper': [], 'lower': []}
    
    for word in s:
        if word.isupper():
            d["upper"].append(word)  
        elif word.islower():
            d["lower"].append(word)

    print(f"No. of Upper case characters : {len(d['upper'])} \nNo. of Lower case Characters : {len(d['lower'])}")

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

print("----list and returns a new list with unique elements----")

def unique_list(lst):
    return list(set(lst))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

print("---- multiply all the numbers in a list.----")

def multiply(numbers):
    result_product = 1
    for num in numbers:
        result_product *= num
    return result_product


print(multiply([1,2,3,-4]))

print("----checks whether a word or phrase is palindrome or not----")

def palindrome(s):
    str1 = s.replace(" ", "")
    return str1 == str1[::-1]

print(palindrome('race car'))


print("----check whether a string is pangram or not----")

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str2 = set(str1.lower().replace(" ", ""))

    
    in_alphabet = str2.symmetric_difference(alphabet)
    #print(str2.symmetric_difference(alphabet))
    return len(in_alphabet) == 0


print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("lazy boii"))