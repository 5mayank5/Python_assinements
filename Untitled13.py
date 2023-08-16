#!/usr/bin/env python
# coding: utf-8

# In[1]:


#test Questions


# In[3]:


#Question 1: Counting Odd Numbers
#Write a program that continuously takes input from the user until they enter a negative number.
#The program should then print the count of all the odd numbers entered.


# In[5]:


def count_odd_numbers():
    count = 0
    while True:
        num = int(input("Enter a number: "))
        if num < 0:
            break
            if num % 2 != 0:
                count += 1

    print("Count of odd numbers entered:", count)

count_odd_numbers()


# In[6]:


#Question 2: Guessing Game
#Create a guessing game where the computer generates a random number between 1 and 100, and the player has to guess it.
#The game should provide feedback on whether the guess is too high or too low, and it should continue until the player guesses the correct number.


# In[34]:


import random

def guessing_game():
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the Guessing Game! Try to guess the secret number between 1 and 100.")

    while guess != secret_number:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")

    print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")

guessing_game()



# In[ ]:


#Password Validation
#Write a program that repeatedly asks the user for a password. The program should keep asking until the user enters a password that meets the following criteria:

#Contains at least 8 characters
#Contains at least one uppercase letter
#Contains at least one lowercase letter
#Contains at least one digit


# In[9]:


def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    return True

def password_validation():
    while True:
        password = input("Enter a password: ")
        
        if validate_password(password):
            print("Password is valid. Good job!")
            break
        else:
            print("Password does not meet the requriments. Please try again.")

password_validation()


# In[10]:


#Questions on Conditional Staements
#Question 1: Grade Classifier Write a program that takes a student's numerical grade as input and prints their corresponding letter grade according to the following scale:

#90 or above: A 80-89: B 70-79: C 60-69: D Below 60: F


# In[11]:


def grade_classifier():
    numerical_grade = float(input("Enter the student's numerical grade: "))
    
    if numerical_grade >= 90:
        letter_grade = 'A'
    elif numerical_grade >= 80:
        letter_grade = 'B'
    elif numerical_grade >= 70:
        letter_grade = 'C'
    elif numerical_grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    
    print(f"The student's letter grade is: {letter_grade}")

grade_classifier()


# In[12]:


#Question 2: Even or Odd Write a program that takes an integer as input and determines whether it is even or odd.

#Question 3: Leap Year Checker Write a program that checks if a given year is a leap year. A leap year is either divisible by 4 but not by 100, or divisible by 400.

#Question 4: Positive, Negative, or Zero Write a program that takes a number as input and prints whether it is positive, negative, or zero.



# In[13]:


def even_or_odd():
    number = int(input("Enter an integer: "))
    
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

even_or_odd()


# In[14]:


def leap_year_checker():
    year = int(input("Enter a year: "))
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

leap_year_checker()


# In[15]:


def positive_negative_zero():
    number = float(input("Enter a number: "))
    
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

positive_negative_zero()


# In[16]:


#Question 5: Triangle Type Write a program that takes the lengths of three sides of a triangle as input and determines whether it's an equilateral, isosceles, or scalene triangle.


# In[19]:


def triangle_type():
    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))
    
    if side1 == side2 == side3:
        print("It's an equilateral triangle.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("It's an isosceles triangle.")
    else:
        print("It's a scalene triangle.")

triangle_type()


# In[20]:


#Questions on For Loop
#Question 1: Print Even Numbers Write a program that prints all even numbers between 1 and 20.

#Question 2: Calculate Factorial Write a program that calculates the factorial of a given positive integer.

#Question 3: Print Multiplication Table Write a program that takes an integer as input and prints its multiplication table up to 10.

#Question 4: Calculate Sum of Digits Write a program that calculates the sum of the digits of a given number.

#Question 5: Calculate Fibonacci Series Write a program that generates the Fibonacci series up to a given number of terms.


# In[21]:


def print_even_numbers():
    for number in range(2, 21, 2):
        print(number)

print_even_numbers()


# In[23]:


def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

num = int(input("Enter a positive integer: "))
print(f"The factorial of {num} is {calculate_factorial(num)}")


# In[24]:


def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter an integer: "))
print_multiplication_table(num)


# In[26]:


def calculate_sum_of_digits(number):
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    return digit_sum

num = int(input("Enter a number: "))
print(f"The sum of digits of {num} is {calculate_sum_of_digits(num)}")



# In[27]:


def generate_fibonacci_series(terms):
    fib_series = [0, 1]
    for i in range(2, terms):
        next_term = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_term)
    return fib_series

num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
fibonacci_series = generate_fibonacci_series(num_terms)
print("Fibonacci series:", fibonacci_series)


# In[28]:


#Question 2: Hollow Square Pattern
#Write a program to print a hollow square pattern of asterisks (*) with a side length of 5.

# ***
#*   *
#*   *
#*   *
# ***


# In[31]:


def print_hollow_square(side_length):
    for i in range(side_length):
        for j in range(side_length):
            if i == 0 or i == side_length - 1 or j == 0 or j == side_length - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_hollow_square(5)


# In[32]:


#Question 3: Right Triangle Number Pattern
#Write a program to print a right triangle number pattern
#1
#12
#123
#1234
#12345


# In[33]:


def print_right_triangle_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

print_right_triangle_pattern(5)


# In[ ]:




