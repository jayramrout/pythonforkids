text = input("Enter a string")
print(f'<{text}>')
text = text.lstrip()
print(f'After removing from left <{text}>')
text = text.lower()
print(f'After making it to lower case {text}')

position_of_my = text.find('my')
print(f'Position of my is {position_of_my}')

if position_of_my > 5 :
    print("Good Job")
else:
    print('OOPS!!')
