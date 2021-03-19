def add_two_number(num1, num2):
    total = num1 + num2
    return total

age1 = 10;
age2 = 20;
final_age_1 = add_two_number(age1,age2)
age3 = 4;
age4 = 30;
final_age_2 = add_two_number(age3,age4)
final_final_age = add_two_number(final_age_1,final_age_2)

# print(f'Final Final age = {final_final_age}')


# This is been overridden...
# method signature...
def print_name(name , message="Welcome to the python course...") :
    print(f'Hello {name} {message} ')

print_name('Peter')
print_name('Jack')
print_name('Ken','You are very good in python...!!!!')