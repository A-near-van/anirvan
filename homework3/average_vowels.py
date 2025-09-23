# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

def counting_vowels_and_consonants(text):
    every_character = list(text) # turn every character in the string into an item in a list
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] # set the letters that count as vowels
    v = 0 # vowel counter
    c = 0 # consonant counter
    for character in every_character: # evaluating each character in the list
        if character.isalpha() == True: # filter out punctuation and spaces
            if bool(character in vowels) == True: # checks if the alphabetic character qualifies as a vowel from the list above
                v += 1
            else:
                c += 1
    return (v,c)


# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(writing):
    lines_1 = writing.split('.') # first we split the string based on periods
    lines_2 = lines_1[0].split('!') # then we split those strings if they have an exclamation point
    lines_1.remove(lines_1[0])
    lines_final = list(lines_2 + lines_1) # Then we add the two while removing redundancy
    lines_final.remove('')
    NOS = len(lines_final) # NOS = number of sentences
    every_character = [] # starts a list to sort all the characters into after splitting into individual lines
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    v = 0
    c = 0
    for line in lines_final:
        for character in line: 
            every_character.append(character)
            if character.isalpha() == True: # Then repeat the process from the previous problem
                if bool(character in vowels) == True:
                    v += 1
                else:
                    c += 1
    return(NOS, v/NOS, c/NOS)

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

# print(counting_vowels_and_consonants(paragraph))
# print(average_vowels_and_consonants(paragraph))
print(f"This paragraph has {counting_vowels_and_consonants(paragraph)[0]} vowels and {counting_vowels_and_consonants(paragraph)[1]} consonants")

print(f"This paragraph has {average_vowels_and_consonants(paragraph)[0]} sentences, {average_vowels_and_consonants(paragraph)[1]} vowels per sentence, and {average_vowels_and_consonants(paragraph)[2]} consonants per sentence")