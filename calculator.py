#adding something in and making something here

print("Hello, Welcome to the calculator program")
print("Here were are going to perform some math calcs")
# Enter a number
def calculator():
    print("Choose any one below")
    print("1.Addition")
    print("2.Subraction")
    print("3.Multiplication")
    print("4.Division")
    choice = int(input("Enter the choice in number: "))
# Conditional statement
    if choice<5 :
        if choice == 1:
            print("You have choosed Addition")
            a = int(input("Enter the first value you want to add: "))
            b = int(input("Enter the second value you want to add: "))
            c = a+b
            print("The sum of", a, "&", b , "is",c)
        elif choice == 2:
            print("You have choosed Subraction")
            a = int(input("Enter the first value you want to subract: "))
            b = int(input("Enter the second value you want to subract: "))
            c = a-b
            print("The difference between", a,"&", b , "is",c)

        elif choice == 3:
            print("You have choosed Multiplication")
            a = int(input("Enter the first value you want to multiply: "))
            b = int(input("Enter the second value you want to multiply: "))
            c = a*b
            print("The product of", a,"&", b , "is",c)

        else:
            print("You have choosed Division")
            a = int(input("Enter the first value you want to divide: "))
            b = int(input("Enter the second value you want to divide:  "))
            c = a/b
            print("The divided of", a, "&" , b , "is",c)

    else:
        print("Please enter the correct choice ","\n","\n")
        return calculator()

calculator ()