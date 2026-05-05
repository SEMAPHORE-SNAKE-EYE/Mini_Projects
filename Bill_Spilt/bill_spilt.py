print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_amount = tip/ 100 * bill + bill
spilt_amount = tip_amount/ people
print(f"Your Individual Bill is : {round(spilt_amount,2)}")