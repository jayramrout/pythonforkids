
# for loop
# while loop
# age = 10
# print(type(age))
#
# name = 'Peter'
# print(type(name))
#
# tup = [4,5,6,7,7]
# print(type(tup))


# While loop
i = 0
while i < 5:
    print("Hello I am running..")
    i = i+1

##### While with Break
i = 0
while True:
    print("Hello I am running..")
    i = i+1
    if i == 5:
        break

### while with continue

i =0
while i < 5:
    if i == 3:
        i = i + 1
        continue
    print("Hello I am running..", i)
    i = i+1

###### Assignments ###########

#Assignment 0:
# SETUP YOUR PyCharm

#Assignment 1:
# given a list [1,2,3,4,5,6,7,8]
# How would you loop and print all the number...

#Assignment 2:
# Program to add natural
# numbers up to
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

# Output:
#Enter n: 10
#The sum is 55

#Assignment 3:
#Write a Python program to calculate a dog's age in dog's years.
# Note: For the first two years, a dog year is equal to 10.5 human years.
# After that, each dog year equals 4 human years.
# Expected Output:
#
# Input a dog's age in human years: 5
# The dog's age in dog's years is 33


# Assignment 4:
# Given a list of integers eg: [2,5,66,77,11,33]
# Find the average of all the numbers using a while loop.

#Assignmet 5:
#Using while loop, and if statement ,
# iterate through the list and if there is a 100,
# print it with its index number. i.e.: "There is a 100 at index no: 5"


#Assignment 6:
# weather=["It's", "a", "...", "nice","weather"]
#Use a while looop to the above list to print
# It's a nice weather
# use continue to skip printing "..."


#Assignment 7:
#Uncomment the below program and just run it for fun.
"""
import turtle

for i in range(5):
    turtle.forward(150)
    turtle.right(144)

turtle.exitonclick()

"""