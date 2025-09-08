#File: homework1.py

# --- Variables and Data Types ---

#a = 10 
#print(a)
#print(type(a)) # a is an integer, a whole number with no decimals

#b = 1.5
#print(b)
#print(type(b)) # b is a float, a number that has a decimal point

#c = 3j
#print(c)
#print(type(3j)) # c is a complex data type, which is composed of a combination of integers, floats, strings, or other complex data types

#d = "hello"
#print(d)
#print(type(d)) # d is a string, a sequence of characters or text

#e = [1,2,3]
#print(e)
#print(type(e)) # e is a list, and an ordered collection of numbers

#f = {"name": "Ellen", "favorite fruit": "strawberry"}
#print(f)
#print(type(f)) # f is a dictionary, which stores different types of values sorted by their key

#g = (1,2)
#print(g)
#print(type(g)) # g is a tuple, an immutable sequence that stores a collection of items

#h = ["apple", "banana", "strawberry"]
#print(h)
#print(type(h)) # h is a list of strings

#i = True
#print(i)
#print(type(i)) # i is a boolean, a data type that takes on one of two values, in this case true or false

#j = None
#print(j)
#print(type(j)) # j is a nonetype. this represents a value not being present

#k = [True, "blue", 12]
#print(k)
#print(type(k)) # k is a mixed list with a boolean, a string, and an integer

#l = str(14)
#print(l)
#print(type(l)) #l is a function that turns the input into a string

#m = 1e4
#print(m)
#print(type(m)) # m is a float that includes e4 to multiply 1 by 10 to the fourth power

#n = frozenset(["star", "planet", "galaxy"]) # This is no. 5
#print(n)
#print("quasar" in n)
#print(type(n)) # n is a frozenset, a set whose contents can't be modified

# --- Questions ---

# 1. I found 9 different data types

# 2. Strings, Floats, Integers, Complex, Lists, Dictionaries, Booleans, Nonetype, and Tuples

# 3. e, h, and k all have lists and l is a string

# 4. 14 is a string and not an integer because the str() function converted 14 into a string, equivalent to putting 14 between quotation marks

# --- Booleans ---

#print(10 > 9) # True, 10 is greater than 9

#print(10==9) # False, 10 is not equal to 9

#print(10<=9) # False, 10 is not less than or equal to 9

#print(bool("abc")) # True, abc is not inherently contradictory

#print(bool(123)) # True, 123 is also non-contradictory

#print(bool(["apple", "cherry", "banana"])) # True, a list of fruits should not be false

#print(bool(True)) # True, the statement true should be true (?)

#print(bool(False)) # False, the statement false should be false (!)

#print(bool(0)) # False, 0 is a false-y value since false corresponds to a 0 in python

#print(bool("")) # False, the boolean function isn't evaluating anything

#print(bool(" ")) # True, the boolean is evaluating the space between the quotations, which has no reason to be false

#print(bool(())) # False, the boolean is evaluating nothing

#print(bool([])) # False, the boolean is evaluating nothing

#print(bool({})) # False, the boolean is evaluating nothing

#print(bool(True and False)) # False, something can't be true and false at the same time (?)

#print(bool(True and True)) # True, the object is doubly true

#print(bool(False and False)) # False, the object is doubly false

#print(bool(True or False)) # True, if an object is true or false, this should be inherently true

#print(bool(True or True)) # True, if an object is true or true, it should return true nonetheless

#print(bool(False or False)) # False, if an object is false or false, it should return false nonetheless

#print(bool(not(False))) # True, since the opposite of false is true

#print(bool(not(True))) # False, since the opposite of true is false

# --- Questions ---

# 1. Expressions returning True or False only occur when a statement is put into the boolean function

# 2. The boolean for True and False yielding no answer was surprising because I would assume that any object can't be true and false at the same time, so the boolean would return false.

# 3. 2 + 2 == 4: this statement will return true because adding 2 to 2 is equal to 4

# 4. 2 + 1 >= 5: 2 + 1 or 3 is not greater than or equal to 5

# --- Operators ---  

# --- Arithmetic Operators ---

#print(10+5) # 15, + performs addition

#print(10-5) # 5, - performs subtraction

#print(2*4) # 8, * performs multiplication

#print(6/3) # 2, / performs division

#print(5 % 2) # 1, % returns the remainder of a division

#print(3**2) # 9, ** takes a number to some exponent

#print(15//2) # 7, // performs a division and returns only the integer

# --- Comparison Operators ---

#print(5 == 2) # False, == sets two values equal to each other

#print(10 !=10) # False, != sets two values not equal to each other

#print(2<5) # True, < sets one value less than another

#print(12>5) # True, > sets one value greater than another

#print(5 <= 6) # True, <= sets one value less than or equal to another

#print(1>=10) # False, >= sets one value greater than or equal to another

# --- Assignment Operators ---

#x = 5
#x += 5
#x -= 4
#x *= 3
#print(x)

# --- Logical Operators ---

#y = ["cherry", "blueberry"]

#print(bool("cherry" in y))

#print(bool("apple" in y))

#print(bool("cherry" in y and "apple" in y))

# 1. The operator 'and' connects two arguments, usually within an operation like the one above.

#print(bool("cherry" in y or "apple" in y))

# 2. The 'or' operator considers two arguments within the same brackets, but doesn't connect the two arguments.

#print(bool("apple" not in y))

# 3. The operator 'not' assumes the opposite of the argument described, in this case 'apple in y'.

# --- More Questions ---

# 1. The difference between / and // is that / returns a float while // returns an integer.

# 2. The difference between % and // is that // returns the quotient in a division and % returns the remainder.

# 3. I would use % to calculate the remainder. Eg:

# print(7%5)

# 4. Assignment operators modify the variable directly instead of needing to print the modification of a variable i.e x += 5 vs print(x+5).

