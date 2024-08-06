import random
# # import re
# # Exercise 0: Example
# #
# # This is a practice exercise to help you understand how to write code "inside" a provided Python function.
# #
# # We'll create a function that checks a condition and prints a specific greeting message based on that condition.
# #
# # Requirements:
# # - The function is named `print_greeting`.
# # - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# # - Use a conditional statement to check if `python_is_fun` is `True`.
# # - If `python_is_fun` is `True`, print the message "Python is fun!"

# def print_greeting():
#     # Your code goes here. Remember to indent!
#     python_is_fun = True
#     if python_is_fun:
#         print("Python is fun!")

# # Call the function
# print_greeting()



# # Exercise 1: Vowel or Consonant
# #
# # Write a Python function named `check_letter` that determines if a given letter
# # is a vowel or a consonant.
# #
# # Requirements:
# # - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# # - It should handle both uppercase and lowercase letters.
# # - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# # - If the letter is a consonant, print: "The letter x is a consonant."
# # - Replace 'x' with the actual letter entered by the user.
# #
# # Hints:
# # - Use the `input()` function to capture user input.
# # - Utilize the `in` operator to check for vowels.
# # - Ensure to provide feedback for non-alphabetical or invalid entries.

# def check_letter():
#     # # Your control flow logic goes here
#     # not_alphabet_regex = '[^a-zA-Z]'
#     # vowels_regex = '[aeiouAEIOU]'
#     # letter = input('Enter a letter: ')
#     # if re.match(vowels_regex, letter):
#     #     print(f'The letter {letter} is a vowel.')
#     # elif re.match(not_alphabet_regex, letter):
#     #     print(f'{letter} is not a letter. Please enter a valid letter.')
#     # else:
#     #     print(f'The letter {letter} is a consonant.')
#     alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     vowels= 'aeiouAEIOU'

#     while True:
#         character = input('Please enter a letter: ')
#         if character == '':
#             print('Please enter a value.\n')
#         elif len(character) > 1:
#             print('Too many characters.\n')
#         elif character in vowels:
#             print(f'The letter {character} is a vowel.\n')
#             break
#         elif character in 'yY':
#             print(f'The letter {character} is sometimes a vowel.\n')
#             break
#         elif character not in alphabet:
#             print(f'{character} is not a letter')
#             break
#         else:
#             print(f'The letter {character} is a consonant.\n')
#             break

# # Call the function
# check_letter()



# # Exercise 2: Old enough to vote?
# #
# # Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# # Fill in the logic to perform the eligibility check inside the function.
# #
# # Function Details:
# # - Prompt the user to input their age: "Please enter your age: "
# # - Validate the input to ensure the age is a possible value (no negative numbers).
# # - Determine if the user is eligible to vote. Set a variable for the voting age.
# # - Print a message indicating whether the user is eligible to vote based on the entered age.
# #
# # Hints:
# # - Use the `input()` function to capture the user's age.
# # - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# # - Use a conditional statement to check if the age meets the minimum voting age requirement.

# def check_voting_eligibility():
#     # Your control flow logic goes here
#     voting_age = 18

#     while True:
#         try:
#             age = input('What is your age?\n')
#             if int(age) < 0:
#                 print('Please enter a valid age.\n')
#             elif int(age) < 18:
#                 print(int(age))
#                 if int(age) == 17:
#                     print(f'Ineligible to vote. You may vote in 1 year.\n')
#                     break
#                 else:
#                     print(f'Ineligible to vote. You may vote in {voting_age - int(age)} years.\n')
#                     break
#             elif int(age) >= 18:
#                 print('To the booths with you.\n')
#                 break
#         except ValueError:
#             print('Invalid input value.\n')

# # Call the function
# check_voting_eligibility()



# # Exercise 3: Calculate Dog Years
# #
# # Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# # Fill in the logic to perform the calculation inside the function.
# #
# # Function Details:
# # - Prompt the user to enter a dog's age: "Input a dog's age: "
# # - Calculate the dog's age in dog years:
# #      - The first two years of the dog's life count as 10 dog years each.
# #      - Each subsequent year counts as 7 dog years.
# # - Print the calculated age: "The dog's age in dog years is xx."
# # - Replace 'xx' with the calculated dog years.
# #
# # Hints:
# # - Use the `input()` function to capture user input.
# # - Convert the string input to an integer using `int()`.
# # - Apply conditional logic to perform the correct age calculation based on the dog's age.

# def calculate_dog_years():
#     # Your control flow logic goes here
#     while True:
#         try:
#             dog_age = input('Please enter dog\'s age in human years: ')
#             age_in_dog_years = int(dog_age) * 10 if int(dog_age) <= 2 else ((int(dog_age) - 2) * 7) + 20
#             print(f'The dog\'s age is {age_in_dog_years}.\n')
#             break
#         except ValueError:
#             print('Invalid value input.\n')

# # Call the function
# calculate_dog_years()



# # Exercise 4: Weather Advice
# #
# # Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
# #
# # Requirements:
# # - The script should prompt the user to enter if it is cold (yes/no).
# # - Then, ask if it is raining (yes/no).
# # - Use logical operators to determine clothing advice:
# #   - If it is cold AND raining, print "Wear a waterproof coat."
# #   - If it is cold BUT NOT raining, print "Wear a warm coat."
# #   - If it is NOT cold but raining, print "Carry an umbrella."
# #   - If it is NOT cold AND NOT raining, print "Wear light clothing."
# #
# # Hints:
# # - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

# def weather_advice():
#     # Your control flow logic goes here
#     yn = 'ynYN'
#     yY = 'yY'
#     while True:
#         is_it_cold = input('Is it cold? (Y/N) ')
#         if is_it_cold not in yn:
#             print('Invalid input.\n')
#         else:
#             if is_it_cold in yY:
#                 is_cold = True
#                 break
#             else:
#                 is_cold = False
#                 break
    
#     while True:
#         is_it_rain = input('Is it raining? (Y/N) ')
#         if is_it_rain not in yn:
#             print('Invalid input.\n')
#         else:
#             if is_it_rain in yY:
#                 is_rain = True
#                 break
#             else:
#                 is_rain = False
#                 break

#     if is_cold and is_rain:
#         print('Wear a waterproof coat.\n')
#     elif is_cold and not is_rain:
#         print('Wear a warm coat.\n')
#     elif not is_cold and is_rain:
#         print('Carry an umbrella.\n')
#     elif not is_cold and not is_rain:
#         print('Wear light clothing.\n')

#     # if is_cold

# # Call the function
# weather_advice()



# # Exercise 5: What's the Season?
# #
# # Write a Python function named `determine_season` that figures out the season based on the entered date.
# #
# # Requirements:
# # - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# # - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# # - Determine the current season based on the date:
# #      - Dec 21 - Mar 19: Winter
# #      - Mar 20 - Jun 20: Spring
# #      - Jun 21 - Sep 21: Summer
# #      - Sep 22 - Dec 20: Fall
# # - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
# #
# # Hints:
# # - Use 'in' to check if a string is in a list or tuple.
# # - Adjust the season based on the day of the month when needed.
# # - Ensure to validate input formats and handle unexpected inputs gracefully.
# # 
# def determine_season():
#     # Your control flow logic goes here
#     months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#     winter_months = ['Dec', 'Jan', 'Feb', 'Mar']
#     spring_months = ['Mar', 'Apr', 'May', 'Jun']
#     summer_months = ['Jun', 'Jul', 'Aug', 'Sep']
#     fall_months = ['Sep', 'Oct', 'Nov', 'Dec']
#     months_with_31_days = ['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec']
#     months_with_30_days = ['Apr', 'Jun', 'Sep', 'Nov']
#     february = ['Feb']

#     while True:
#         month = input('Please enter a month (e.g. Jan): ').capitalize()
#         if month not in months:
#             print('Invalid month.')
#         else:
#             break
#     while True:
#         try:
#             day = int(input('Please enter a day: '))
#             if day <= 0:
#                 print('Invalid date.')
#             elif month in months_with_31_days and day > 31:
#                 print('Invalid date.')
#             elif month in months_with_30_days and day > 30:
#                 print('Invalid date.')
#             elif month in february:
#                 if day > 29:
#                     print('Invalid date.')
#                 elif day == 29:
#                     year = input('Is it a leap year? (Y/N) ')
#                     if year not in 'yYnN':
#                         print('Invalid input value')
#                     elif year in 'yY':
#                         break
#                     else:
#                         print('Invalid date.')
#                 else:
#                     break
#             else:
#                 break
#         except ValueError:
#             print('Invalid input value.')


#     if month in winter_months:
#         if month == 'Dec':
#             if day >= 21:
#                 print(f'{month} {day} is in Winter.')
#             elif day < 21:
#                 print(f'{month} {day} is in Fall.')
#         elif month == 'Mar':
#             if day <= 19:
#                 print(f'{month} {day} is in Winter.')
#             elif day > 19:
#                 print(f'{month} {day} is in Spring.')
#         else:
#             print(f'{month} {day} is in Winter.')
    
#     elif month in spring_months:
#         if month == 'Jun':
#             if day <= 20:
#                 print(f'{month} {day} is in Spring.')
#             elif day > 20:
#                 print(f'{month} {day} is in Summer.')
#         else:
#             print(f'{month} {day} is in Spring.')

#     elif month in summer_months:
#         if month == 'Sep':
#             if day <= 20:
#                 print(f'{month} {day} is in Spring.')
#             elif day > 20:
#                 print(f'{month} {day} is in Fall.')
#         else:
#             print(f'{month} {day} is in Summer.')

#     elif month in fall_months:
#         print(f'{month} {day} is in Fall.')


# # Call the function
# determine_season()



# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    # Your control flow logic goes here
    number = int(random.random() * 100) + 1
    title = 'Number Guess Game'.center(100, '=')
    print(''.center(100, '_'))
    print('\n', title, '\n')
    print(''.center(100, '_'))
    for attempt in range(5):
        if attempt < 4:
            while True:
                try:
                    print()
                    print('{:^100}'.format('Enter a number between 1 and 100'))
                    guess = input('Guess: '.rjust(51))
                    if int(guess) < number:
                        print('{:^100}'.format('Guess is too low.'))
                        break
                    elif int(guess) > number:
                        print('{:^100}'.format('Guess is too high.'))
                        break
                    else:
                        print('Congratulations, you guessed correctly!'.center(100))
                        print(f'Number was {number}.'.center(100))
                        return
                except ValueError:
                    print('Invalid input value.'.center(100))

        else:
            print('Last chance!'.center(100))
            while True:
                try:
                    print()
                    print('{:^100}'.format('Enter a number between 0 and 100'))
                    guess = input('Guess: '.rjust(51))
                    if int(guess) == number:
                        print('Congratulations, you guessed correctly!'.center(100))
                        print(f'Number was {number}.'.center(100))
                        print()
                        break
                    else:
                        print(f'Number was {number}.'.center(100))
                        print()
                        break
                except ValueError:
                    print('Invalid input value.'.center(100))


# Call the function
guess_number()

