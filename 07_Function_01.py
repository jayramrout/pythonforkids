# Creating a function
def find_and_print(name, names):
    for i in names:
        if i == name:
            print(f'Hello {name} You are present')

names = ["John","Peter","Jack","David","Ken"]

find_and_print("David",names)
# find_and_print("Ken",names)
# find_and_print("Ron",names)

# Calling a function
def call_me():
    print('Hello World 1')
    print('Hello World 2')



# Passing argument to a function
def print_name(fname , lname) :
    print(f'*********************Hello {fname} {lname} *********************')
# print_name('Peter','Pan')

def add_two_number():
    pass

age1 = 10;
age2 = 20;

final_age_1 = age1 + age2;

print(f'Final Number ={final_age_1}')

age3 = 4;
age4 = 30;

final_age_2 = age3 + age4
final_final_age = final_age_1 + final_age_2
print(f'Final Final age = {final_final_age}')