import math

while True:
    print("select an oprator")
    print("+")
    print("-")
    print("*")
    print("/")
    print("power")
    print("sin")
    print("log")
    print("tan")
    print("exit")
    op = input("please enter oprator: ")

    if op == "exit":
        break

    elif op == "+" or op == "-" or op == "/" or op == "*" or op == "power" :
        Number1 = int(input("please enter first number: "))
        Number2 = int(input("please enter second number: "))
        if op == "+":
            print("result: ", Number1 + Number2)
        elif op == "-" :
            print("result: ", Number1 - Number2)
        elif op == "*" :
            print("result: ", Number1 * Number2)
        elif op == "power" :
            print(math.pow(Number1, Number2))
        elif op == "/" :
            if Number2 == 0 :
                print("please change number2")
            else:
                print("result: ", Number1 / Number2)
    else:
        Number1 = int(input("please enter number: "))
        if op == "sin" :
            print("result: ", math.sin(Number1))
        elif op == "log" :
            print("result: ", math.log(Number1))
        elif op == "tan" :
            print ("result: ", math.tan(Number1))
