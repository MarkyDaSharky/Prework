#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    """A greeting with user input to greet any name"""
    user_name = print("Hello_" + user_name + "!" +"\nWhat would you like to do today?")

hello_name("mark")


#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """Function printing odd numbers between 1-100"""
    for number in range(1, 100, + 1):
        if(number % 2 != 0):
            print(number)

print(first_odds())
        


#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """Function to pull max number from a list"""
    a_list.sort()
    print(a_list[-1])

max_num_in_list([5, 1, 2, 6, 10,12])

    
                
#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
        
def is_leap_year(a_year):
    """If a year is leap year return the answer as a true or false"""
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else: 
            return True
    else:
        return False

print(is_leap_year(2000))



#Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    """Function to check if all numbers in a list are consecutive"""
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))


randomlist = [1,5,4,3,2]
print(is_consecutive(randomlist))







