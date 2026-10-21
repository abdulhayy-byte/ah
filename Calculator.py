import math
from math import remainder

print('''Choose and type one of the following supported functions:
Addition
Subtraction
Multiplication
Division
quit''')
while True:
    command=input(">")
    if command.lower() == "addition":
        first=int(input('enter first number:'))
        second=int(input('enter second number:'))
        answer= int(first)+int(second)
        print(f"{first} + {second} = {answer}")
    elif command.lower() =="subtraction":
        first = int(input('enter first number:'))
        second = int(input('enter second number:'))
        answer = int(first) - int(second)
        print(f"{first} - {second} = {answer}")
    elif command.lower() == "multiplication":
        first = int(input('enter first number:'))
        second = int(input('enter second number:'))
        answer = int(first) * int(second)
        print(f"{first} x {second} = {answer}")
    elif command.lower() == "division":
        div = int(input("""Which type of division would you like(write 1,2, or 3)):
1.With decimal
2.Division as a whole number
3.With remainder
>"""))
        if div == 1:
            first = int(input('enter first number:'))
            second = int(input('enter second number:'))
            if second == 0:
                print("You can't divide with zero...")
            else:
                answer = int(first) / int(second)
                print(f"{first} ÷ {second} = {answer}")
        elif div == 2:
            first = int(input('enter first number:'))
            second = int(input('enter second number:'))
            if second == 0:
                print("You can't divide with zero...")
            else:
                answer = int(first) // int(second)
                print(f"{first} ÷ {second} = {answer}")
        elif div == 3:
            first = int(input('enter first number:'))
            second = int(input('enter second number:'))
            if second == 0:
                print("You can't divide with zero...")
            else:
                answer = int(first) // int(second)
                remainder= int(first) % int(second)
                print(f"{first} ÷ {second} = {answer} r{remainder}")
        else:
            print('Use a valid number...')
    elif command.lower() == "quit":
        break
    else:
        print("Sorry, I don't understand that")