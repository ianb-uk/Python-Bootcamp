# print("hello world")

# nested functions
# get users name with input, then use Len() to count the characters
print(len(input("What is your name? ")))

# variables

name = "Jack"
print (name)

name = "Sarah"

print (name)


comment out a line # (shortcut = CTRL+/) 

# nested functions
# get users name with input, then use Len() to count the characters
print(len(input("What is your name? ")))


# Integer 
# underscores are ignored. only used for visual thousand markers for humans!
123_333_333

#float
3.146

# boolean
# note - capatalised first letter
True 
False

# checking data type 
type(variable_name)
print(type(variable_name))

# convert data type
# convert a number into a string
str(number_char)
new_number_char = str(number_char)

# Day 2 - Exercise 1

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# print(type(two_digit_number))
num_digit_no1 = int(two_digit_number[0])
# print(num_digit_no1)
num_digit_no2 = int(two_digit_number[1])
# print(num_digit_no2)
# print(type(num_digit_no1))
# print(type(num_digit_no2))
print (num_digit_no1 + num_digit_no2)