#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION

def calculate_sum(start, end):
    #Calculate the sum of numbers within the specified range.
# 1. initialize variable for the sum of numbers to iterate from, start.
    total_sum = 0
      #Arguments:
        #start (int): The starting number of the range (inclusive).
        #end (int): The ending number of the range (inclusive).

# 2. write a for loop that iterates through the range 
# adding each number in the range to the previous number. 
    for num in range(start, end + 1):
       
# 3. use += to update the value of a variable by adding 
# another value to it
       total_sum += num

    #Return:
        #int: The sum of numbers within the range.
    return total_sum

# 4. call function with arguements 1 and 5 
# to find sum of the numbers in that range.
result = calculate_sum(1, 5)
#print(result)

    # TODO: Implement the logic to calculate the sum of numbers within the range.
    # TODO: Return the calculated sum.


def find_smallest_number(start, end):
    #Find the smallest number within the specified range.
# 1. initiate smallest to the start value
    smallest = start
    #Arguments:
        #start (int): The starting number of the range (inclusive).
        #end (int): The ending number of the range (inclusive).
# 2. write a for loop that iterates through the range 
#looking for smallest number
    for number in range(start, end + 1):
        if number < smallest:

# 3. update smallest if a smaller number is found
            smallest = number
        
    #Return:
     #   int: The smallest number within the range.
    return smallest
    
    # TODO: Implement the logic to find the smallest number within the range.
    # TODO: Return the found smallest number.

# 4. call function with arguements 3 and 9 
# to find smallest number in that range.
result = find_smallest_number(3, 9)
#print(result)


def find_largest_number(start, end):
        #Find the largest number within the specified range.
# 1. initialize variable for largest number
    largest = end
    #Args:
        #start (int): The starting number of the range ( inclusive).
        #end (int): The ending number of the range (inclusive).
# 2. write a for loop that iterates through the range 
# looking for the largest number
    for number in range(start, end + 1):
        if number > largest:
#
#  3. update smallest if a smaller number is found
            largest = number

    #Return:
      #  int: The largest number within the range.
    return largest
    
    # TODO: Implement the logic to find the largest number within the range.
    # TODO: Return the found largest number.
# 4. call function with arguements 10 and 20 
# to find largest number in that range.
result = find_largest_number(10, 20)
#print(result)


def count_even_numbers(start, end):
    #Count the number of even numbers within the specified range.
# 1. initialize variable for even number
    even = 0
    # Args:
         #start (int): The starting number of the range (inclusive).
         #end (int): The ending number of the range (inclusive).
# 2. write a for loop that iterates through the range 
# counting for the even numbers
    for number in range(start, end +1):
        if number % 2 == 0:

# 3. update even count
            even += 1
    
        #Return:
    return even
       # int: The count of even numbers within the range.

    # TODO: Implement the logic to count even numbers within the range.
    # TODO: Return the count of even numbers.
# 4. call function with arguements 1 and 10 
# to count even numbers in that range.
result = count_even_numbers(1, 10)
# print(result)

def count_odd_numbers(start, end):
    #Count the number of odd numbers within the specified range.
    odd = 0
    #Args:
      #  start (int): The starting number of the range (inclusive).
       # end (int): The ending number of the range (inclusive).
# 2. write a for loop that iterates through the range 
# counting for the odd numbers
    for number in range(start, end +1):
        if number % 2 != 0:
               

# 3. update odd count
            odd += 1
   # Return:
    #    int: The count of odd numbers within the range.
    return odd
    
# 4. call function with arguements 15 and 25 
# to count odd numbers in that range.
    # TODO: Implement the logic to count odd numbers within the range.
    # TODO: Return the count of odd numbers.
result = count_odd_numbers(15, 25)
#print(result)
   
