# Function is a block of code which only runs when it's called
# Function can return results
# You can pass parameters to a function.
# Functions are used to perform certain actions.
###Why To use Function###
# To Reduce code and use it multiple Times.

####################################
# len()
# contain()

# Creating a function
name1 = "David"

names = ["John","Peter","Jack","David","Ken"]
# is name present
# if name is present then i want to print the name saying hello David you are already present

# for i in names:
for i in range(0, len(names)):
    if names[i] == name1:
        print(f'Hello {name1} You are present')


name2 = "Ken"

for i in range(0, len(names)):
    if names[i] == name2:
        print(f'Hello {name2} You are present')


# Calling a function

# Passing argument to a function

# Pass multiple arguments to a function  *kargs --> kargs[0]

# Calling function with argument name eg: call_me(name="Peter",address="Don Drive")

# Default Parameter def call_me(message="Good Morning") --> call_me()