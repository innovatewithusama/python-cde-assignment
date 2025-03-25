# Question 1

vowels = set("aeiouAEIOU")
user_input = input("Enter a string: ")
vowel_count = 0

for letter in user_input:
    if letter in vowels:
        vowel_count += 1

print(f"Number of vowels in the string: {vowel_count}")

# Question 2

user_input = input("Enter you complete name: ")

uppercase = 0
lowercase = 0
digits = 0
whitespace = 0

for letter in user_input:
    if letter.isupper():
        uppercase += 1
    elif letter.islower():
        lowercase += 1
    elif letter.isdigit():
        digits += 1
    elif letter.isspace():
        whitespace += 1


print(f"Total number in uppercase: {uppercase}")
print(f"Total number in lowercase: {lowercase}")
print(f"Total number in digits: {digits}")
print(f"Total number in whitespaces: {whitespace}")
