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

#####################
# Day 2 - Exercise 1
#####################


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


#####################
# Day 2 - Exercise 2
#####################

PEMDAS (left to right)
()
**
* /
+ -


# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# print(type(height))
# print(type(weight))
flt_height = float(height)
flt_weight = float(weight)
# print(type(flt_height))
# print (flt_height)
flt_bmi = (flt_weight / (flt_height * flt_height))
print (int(flt_bmi))


# round numbers 
print(round(8 / 3))
# round by 2 decimal places
print(round(8 / 3, 2))

# when dividing, output always a floating point num

# use // to remove decimals - doesnt round up
print (8 // 3)

# add 1 to a variable 'user-score' current value
user-score += 1
# can also use -+ /= *=

# mix data types

# f-string

score = 0
height = 1.8
isWinning = True
print (f"your score is {score} {height} {isWinning}")


# format a number to give 2 decimal places in case of currency

rndTotalPerPerson = "{:.2f}".format(totalPerPerson)

#####################
# Day 2 - Exercise 3
#####################

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


int_age = int(age)
#print(type(int_age))
max_age = 90
years_remaining = max_age - int_age
#days
days = (max_age - int_age) * 365
#print(days)
#weeks 
weeks = years_remaining * 52
#print(weeks)
#months
months = years_remaining * 12
#print(months)
print (f"You have {days} days, {weeks} weeks, and {months} months left.")

