task_list = []

for row in range(0, 25, 5):
    inner_list = []
    for column in range(row, row + 5):
        inner_list.append(column)
    task_list.append(inner_list)

new_list = [[column for column in range(row, row + 5)] for row in range(0, 25, 5)]

# https://gist.github.com/jon003/c51fa0523e1ac267b79550ea24c6ce4c
#Find all of the numbers from 1-1000 that are divisible by 7
# results = [value for value in range(1, 1001) if value % 7 == 0 ]
# print(results)

#Find all of the numbers from 1-1000 that have a 3 in them
# results = [value for value in range(1, 1001) if '3' in list(str(value))]
# print(results)


#Count the number of spaces in a string
# str_1 = 'Count the number of spaces'
# results = len([char for char in str_1 if char == ' '])
# print(results)
# print(str_1.count(' '))

#Remove all of the vowels in a string [make a list of the non-vowels]
# str_1 = 'Remove all the vowels'
# vowels = ['a', 'e', 'i', 'o', 'u', ' ']
# results = [letter for letter in str_1 if letter.lower() not in vowels]
# print(results)

#Find all of the words in a string that are less than 4 letters
# str_1 = 'Find all of the words in a string that are less than 4 letters'
# results = [word for word in str_1.split() if len(word) < 4]
# print(results)

# CHALLENGE!
#Use a dictionary comprehension to count the length of each word in a sentence.
# str_1 = 'Use a dictionary comprehension to count the length of each word in a sentence.'
# results = {word:len(word) for word in str_1.split()}
# print(results)

#Use a nested list comprehension to find all of the numbers from 1-1000 that
#are divisible by any single digit besides 1 (2-9)
# comprehension testing truth for divisibilty: [True for divisor in range(2,10) if number % divisor == 0]


#print(results)

#For all the numbers 1-1000, use a nested list/dictionary comprehension to
#find the highest single digit any of the numbers is divisible by.
# List comprehension for providing a list of all of the numbers a number is divisible by: divisor_list:
#       [divisor for divisor in range(1,1001) if number % divisor == 0]
# results = {number:max([divisor for divisor in range(1,10) if number % divisor == 0]) for number in range(1,1001)}
# print(results)