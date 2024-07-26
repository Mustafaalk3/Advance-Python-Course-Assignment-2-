'''importing reduce'''
from functools import reduce


'''Exercise 1: Basic Lambda Functions. Question: Create a lambda function that
multiplies two numbers and returns the result. Use this lambda function to multiply 5 by 7.
'''
multiply_by_eachother = lambda x, y: x * y
print(multiply_by_eachother(5 ,7))

#--------------------------------------------------------------------------------------------
'''Exercise 2: Using map with Lambda Functions. Question: You have a list of numbers [1, 2, 3, 4, 5].
Use the map function and a lambda function to create a new list where each number is increased by 10.'''
numbers = [1, 3, 10, 12, 5, 6,]
doubled = list(map(lambda x: x + 10, numbers))

print(doubled)

#--------------------------------------------------------------------------------------------
'''Exercise 3: Combining filter and reduce with Lambda Functions. Question: Given a list of 
numbers [3, 6, 9, 12, 15, 18, 21], use the filter function to select numbers greater than 10. 
Then, use the reduce function to calculate the sum of the filtered numbers.
'''
numbers = [1, 3, 11, 12, 15, 16, 2, 13,]
filterd_num = list(filter(lambda x: x > 10, numbers))
def my_sum(x, y):
    return x + y
total_sum = reduce(my_sum, numbers)

print(total_sum)

#--------------------------------------------------------------------------------------------
'''Question: You have a list of strings ['apple', 'banana', 'cherry', 'date', 'elderberry']. 
Use the filter function and a lambda function to create a new list that contains only the 
strings with more than 5 characters.
'''

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

filterd_fruits = list(filter(lambda x: len(x) > 5, fruits))
print(filterd_fruits)

#--------------------------------------------------------------------------------------------
'''Question: Given a list of numbers [2, 4, 6, 8, 10], first use the map function and a lambda 
function to double each number. Then, use the reduce function to find the product of the doubled numbers.'''

numbers = [2, 4, 6, 8, 10]
doubled_func = list(map(lambda  x: x + x, numbers))
print(doubled_func)

final_sum = reduce(lambda x, y: x * y, doubled_func)
print(final_sum)
