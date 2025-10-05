# File: homework4.py

# --- 3. Liss ---

# --- 3.1 List Operations ---

favorite_foods = ['mac and cheese', 'pasta', 'grilled chicken']

print(favorite_foods[1])

print(favorite_foods[-1])

favorite_foods.append('paneer')

print(favorite_foods)

favorite_foods.insert(0, 'apple')

# print(favorite_foods) 
# # I encountered a TypeError because I put the string before the index value.
# # I fixed it by swapping the index value and the string's order in the argument.

favorite_foods.remove(favorite_foods[2])

print(favorite_foods)

print(len(favorite_foods))

for i in favorite_foods:
    print(i.upper())

print(list(favorite_foods[::3]))

new_list = list(favorite_foods)

def is_there_potato(x):
    if bool('potato' in x) == True:
        print("A potato!")
    else:
        print("No potato!")
# # I accidentally iterated over every item in the list originally and got back 4 No Potatoes. I fixed it by removing the appropriate for statement.

is_there_potato(new_list)

# --- 3.2 Slicing and Striding --- 

numbers = list(range(0,21))

def get_first_15(nums):
    return nums[0:16]

def get_every_5th(lst):
    x = get_first_15(lst)
    return x[::5]

def reverse_and_stride(lst):
    x = get_every_5th(lst)
    y = x[::-1]
    return y[::3]
print(get_first_15(numbers))
print(get_every_5th(numbers))
print(reverse_and_stride(numbers))

# --- 3.3 Nested Lists ---

numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(numbers[2])
print(numbers[1][1])
numbers.append([10,11,12])

def sum_nested(lists):
    total = 0
    for list in lists:
        for i in list:
            total += i
    return total

print(sum_nested(numbers))

# --- 3.4 Create a 5x5 list ---

def make_5_by_5():
    nested_list = []
    for i in range(0,5):
        a = (5*i)+1
        x = list(range(a,a+5))
        nested_list.append(x)
    return nested_list

grand_list = make_5_by_5()

# # print(grand_list)

def multi_3(lst):
    for list in lst:
        for i in range(len(list)):
            if list[i]%3 == 0:
                list[i] = "?"
    return lst

b = multi_3(grand_list)

# # I originally wrote a for loop for i in range(list) instead of range(len(list)).

def summation_shenanigans(biglist):
    total = 0
    for list in biglist:
        for i in list:
            if i != "?":
                total += i
    return total

# print(summation_shenanigans(b))

# --- 4. Dictionaries ---

# --- 4.1 Dictionary Operations ---

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
    }

print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]
# print(ages)

for key, value in ages.items():
    print(f"{key} is {value} years old")

print(f"The sum of the final 5x5 list is {summation_shenanigans(b)}")