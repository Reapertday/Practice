#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# First, lets remember the different ways to make code
# If/and/or/else etc statements will check certain states and give an output based on the results
# We can make functions using def [function](parameter1, parameter2, ...):


# In[ ]:


# Ok let's try doing something basic first. Make an accurate calculator that won't break when adding weird prompts


# In[21]:


print("Welcome to this basic calculator. Please follow each instruction")
# First lets get all of the information we need
# We need both numbers, and how they will be used in the calculation

# This first function is set up to check if an input is a number
def number_check(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# We then set up a loop to ask for each prompt
while number1 != float:
    number1 = input("Enter first number: ")
    if number_check(number1) == True:
        break
    else:
        print("That is not a valid number. Please enter new number: ")
number1 = float(number1)

# This method check kinda sucks. I tried using or statements to simplify but it didn't properly check
# my responses no matter what I would input.
method_check = False
while method_check == False :
    method = input("What function are we using? (Enter +, -, x, or /): ")
    if method == "+" :
        method_check = True
        break
    elif method == "-" :
        method_check = True
        break
    elif method == "*" :
        method_check = True
        break
    elif method == "/" :
        method_check = True
        break
    else:
        print("That is not a valid function. Please enter +, -, *, or /: ")

while number2 != float:
    number2 = input("Enter second number: ")
    if number_check(number2) == True:
        break
    else:
        print("That is not a valid number. Please enter new number: ")
number2 = float(number2)


# In[24]:


# Here I make a calculator function to take the previous inputs and do the basic math
def calculator(c_number1, c_number2, c_method):
    if method == "+" :
        answer = c_number1 + c_number2
        return answer
    elif method == "-" :
        answer = c_number1 - c_number2
        return answer
    elif method == "*" :
        answer = c_number1 * c_number2
        return answer
    elif method == "/" :
        answer = c_number1 / c_number2
        return answer
    else:
        print("Something went wrong!")
        return

# Finally we can print their answer using the calculator function and the result it creates
print("Your answer is " + str(float(calculator(number1, number2, method))))


# In[ ]:




