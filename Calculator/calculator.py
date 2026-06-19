def addition(n1, n2):
    return n1 + n2

def subtraction(n3,n4):
    return n3 - n4

def division(n5,n6):
    return n5 / n6

def multiplication(n7 ,n8):
    return n7 * n8

operations = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiplication,
    "/" : division,
}
def calculator():
    print(r"""
     _____________________
    |  _________________  |
    | |                 | |
    | |   CALCULATOR    | |
    | |_________________| |
    |  ___ ___ ___   ___  |
    | | 7 | 8 | 9 | | + | |
    | |___|___|___| |___| |
    | | 4 | 5 | 6 | | - | |
    | |___|___|___| |___| |
    | | 1 | 2 | 3 | | * | |
    | |___|___|___| |___| |
    | | 0 | . | = | | / | |
    | |___|___|___| |___| |
    |_____________________|
    """)

    Should_acuumulated = True
    print()
    num1 = int(input("Please  enter the number.\n"))
    while Should_acuumulated:

      for symbols in operations:
          print(symbols)
      opr = input("Please select the Opreator : + , - , * ,/ ")
      num2 = int(input("Please enter the second number.\n"))

      Result =(operations[opr](num1,num2))
      print(f"{num1}   {opr}   {num2} = {Result}")
      user_ans =print(input("Wants to continue working with the previous result. If yes type y  Or n : "))
      if user_ans == "y":
          num1 = Result
      else :
          Should_acuumulated = False,
          print("\n * 20")
          calculator()

calculator()