import random

while True:
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))

    print("Select the operation:")
    print("1.Addition")
    print("2.Substraction")
    print("3.Mutiplication")
    print("4.Divison")

    operation=int(input("Enter the option:"))
    if operation == 1:
        result=num1+num2
        print("The addtion of two numbers is:",result)

    elif operation == 2:
        result=num1-num2
        print("The Substraction of two numbers is:",result)

    elif operation == 3:
        result=num1*num2
        print("The multiplication of two numbers is:",result)

    elif operation ==4:
        if num2!=0:
            result= num1/num2
            print("The Division of two numbers is:",result)
        else:
            print("Zero division error!")
    else:
        print("Invalid operation choice!")

    repeat=input("Do you want repeat again the process?(yes/no):")
    if repeat.lower()!="yes":
        break
    print("Thankyou for using the Calculator!")
