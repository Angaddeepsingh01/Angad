# calculator 
def cacl():
    try :
        num1 = int(input("Enter the first number :  "))
        num2 = int(input("Enter the second number :  "))
        action = input("Enter the action you want to do('/','*','-','+') :  ")
        if (action == "*" ):
                print(num1*num2)
        elif (action == "/" ):
            if  num2 == 0:
                print("number can not be divided by 0")
            else:
                print(num1/num2)
        elif (action == "+" ):
            print(num1+num2)
        elif (action == "-" ):
            print(num1-num2)
    except Exception as e :
            print("Please enter a number")

cacl()
