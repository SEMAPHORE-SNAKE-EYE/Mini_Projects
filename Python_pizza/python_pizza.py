print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "S" :
    bill += 15
elif size == "M":
    bill += 20
elif size == "L" :
    bill += 25
else:
    print("Invalid output")
if pepperoni == "Y":
    if size == "S" :
        bill += 2
    elif size == "M" or "L":
        bill +=3
    else :
        print(f"your bill is : ${bill}")
if extra_cheese == "Y" :
    if size == "S" or "M" or "L" :
        bill = bill + 1
        print(f"Your bills is : ${bill}")
    else :
        print(f"your bill is :${bill}")
else:
    print(f"your bill is : ${bill}")






