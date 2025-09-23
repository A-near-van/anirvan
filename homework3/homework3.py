# File: homework3.py

# --- 3. Print functions ---

# 3.1 Say Goodbye

def say_goodbye(name):
    print("Goodbye,", name)

say_goodbye("Ferran")

# 3.2 Area of a Circle

# Given r is radius:

def circle_area(r):
    print(3.14*(r**2))

circle_area(5)

# --- 4. Return functions ---

# 4.1 Subtract, Multiply, and Divide

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

# --- 5. Conditionals ---

# 5.1 What Should I Wear?

def what_to_wear(temperatures):
    # temperatures would be the list of temperatures obviously
    return(min(temperatures), max(temperatures))

september_15 = [15, 14, 17, 20, 23, 28, 20]

print(what_to_wear(september_15))

# 5.2 Check if it's the Weekend

Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6
Sunday = 7

def is_it_weekend(day):
    if day > 5:
        return True
        # Saturday and Sunday are greater than 5 so this would make Saturday and Sunday true values
    else:
        return False
        # All other days will otherwise give us false

print(is_it_weekend(Monday))

# 5.3 Fuel Efficiency Calculator

def fuel_efficiency(distance, fuel_used):
    return distance/fuel_used

print(fuel_efficiency(500, 20))

# 5.4 Secret Code

def encrypt(number):
    return str(number%10)+str(number//10)
        #Floor dividing the number by ten gives us the number to the tens place. 
        #The modulus of the number divided by ten gives us the number in the front.
        #To rearrange these components, we have to turn the number into the string. And voila!

print(encrypt(12345))

# --- 6. Loops ---

# 6.1 Oski Stole Your Power

def power(x, y):
    for i in range(1, y):
        x *= x
    # In essence, we are using the foor loop to conduct y multiplications of x by itself.
    return x    

print(power(4, 2))

# 6.2 Min & Max with Loops

# 6.2.1 For Loops

numbers = [1, 2, 3]

def minim(numbers):
    target_value = numbers[0]
        # first we assign a target number that we want to get out of the function. For simplicity's sake we start by making this value the first value
    for number in numbers:
        if number < target_value:
            target_value = number
        # The for loop then only reassigns the target value if the number in the list it's evaluating is less than the target value.
    return target_value

digit_set = [19,23,26,37,6]

print(minim(digit_set))

def maxim(numbers):
    target_value = numbers[0]
        # Similar approach for the maximum. Initialize a value...
    for number in numbers:
        if number > target_value:
            target_value = number
        # Then only reassign the target_value if we find a greater value.
    return target_value

print(maxim(digit_set))

# 6.2.2 While Loops

def minimum(numbers):
    x = 0 
        # Initializing an x value will be helpful to assign numbers for the function to evaluate.
    target_value = numbers[x]
    next_digit = numbers[x+1]
        # the target value starts out as the first number.
    while x+1 < len(numbers): # making sure we're evaluating within the range of the list...
        if target_value > next_digit: # In cases where a lower number is the next number in the list
            x += 1
            target_value = numbers[x] # we change the target_value to that next number
            if x+1 < len(numbers): # because we changed the value of x, we have to double check that we're not evaluating outside of the range...
                next_digit = numbers[x+1] # we move it along to the next number in the list...
        elif target_value < next_digit: # If the next digit isn't less than what we have...
            x += 1
            if x+1 < len(numbers):
                next_digit = numbers[x+1] # we chug along to the next number anyway...
    return target_value

# The maximum number function is essentially the same except we flip a couple inequalities

def maximum(numbers):
    x = 0
    target_value = numbers[x]
    next_digit = numbers[x+1]
    while x+1 < len(numbers):
        if target_value < next_digit:
            x += 1
            target_value = numbers[x]
            if x+1 < len(numbers):
                next_digit = numbers[x+1]
        elif target_value > next_digit:
         x += 1
         if x+1 < len(numbers):
              next_digit = numbers[x+1]
    return target_value

digit_set = [19,23,26,37,6]  

print(minimum(digit_set))

print(maximum(digit_set))

# 6.3 Calculate the sum

def summation(num):
    a = str(num) 
    b = list(a) # stringing up the number and putting each value in the list will individualize each digit in the number
    number_list = [int(i) for i in b] # But we have to convert them back to integers so we create a new list of numbers with the int function
    return sum(number_list) # And then we sum up the numbers in the list...
    
print(summation(1248))

# def encrypt(number):
#     return str(number%10)+str(number//10)
#          # Floor dividing the number by ten gives us the number to the tens place. 
#         # The modulus of the number divided by ten gives us the number in the front.
#         # To rearrange these components, we have to turn the number into the string. And voila!

# result = encrypt(1875)
# print(f"The result of Secret Code (5.4) with the number 1875 is {result}.")