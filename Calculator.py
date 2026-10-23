prompt = ('''Choose and type one of the following supported functions:
Addition
Subtraction
Multiplication
Time Table
Division
Help (to see this prompt again)
quit
Note: Type the function name as shown (capitals don't matter).''')
print(prompt)
while True:
    command=input(">")
    if command.lower() == "addition":
        first= input('enter first number:')
        second= input('enter second number:')
        if first.isdigit() == True and second.isdigit() == True:
            answer = int(first) + int(second)
            print(f"{first} + {second} = {answer}")
        else:
            print("Please type a number..")
    elif command.lower() =="subtraction":
        first = input('enter first number:')
        second = input('enter second number:')
        if first.isdigit() == True and second.isdigit() == True:
            answer = int(first) - int(second)
            print(f"{first} - {second} = {answer}")
        else:
            print("Please type a number..")
    elif command.lower() == "multiplication":
        first = input('enter first number:')
        second = input('enter second number:')
        if first.isdigit() == True and second.isdigit() == True:
            answer = int(first) * int(second)
            print(f"{first} x {second} = {answer}")
        else:
            print("Please type a number..")
    elif command.lower() == "time table":
        times_table = input("Which times table would you like? ")
        if times_table.isdigit() == True:
            for multiplication in range(0, 13):
                answer = int(times_table) * multiplication
                print(f"{times_table}x{multiplication}={answer}")
        else:
            print("Please type a number..")
    elif command.lower() == "division":
        div = input("""Which type of division would you like (1,2, or 3):
1.With decimal
2.Division as a whole number
3.With remainder
>""")
        if div == '1':
            first = input('enter first number:')
            second = input('enter second number:')
            if first.isdigit() and second.isdigit():
                if int(second) == 0:
                    print("You can't divide with zero...")
                else:
                    answer = int(first) / int(second)
                    print(f"{first} ÷ {second} = {answer}")
            else:
                print("Please type a number..")
        elif div == '2':
            first = input('enter first number:')
            second = input('enter second number:')
            if first.isdigit() and second.isdigit():
                if int(second) == 0:
                    print("You can't divide with zero...")
                else:
                    answer = int(first) // int(second)
                    print(f"{first} ÷ {second} = {answer}")
            else:
                print("Please type a number..")
        elif div == '3':
            first = input('enter first number:')
            second = input('enter second number:')
            if first.isdigit() and second.isdigit():
                if int(second) == 0:
                    print("You can't divide with zero...")
                else:
                    answer = int(first) // int(second)
                    remainder = int(first) % int(second)
                    print(f"{first} ÷ {second} = {answer} r{remainder}")
            else:
                print('Please type a number..')
        else:
            print('Use a valid number...')
    elif command.lower() == "help":
        print(prompt)
    elif command.lower() == "quit":
        break
    else:
        print("Sorry, I don't understand that")
