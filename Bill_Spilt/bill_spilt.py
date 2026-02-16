print("Welcome to the Bill Splitter!")
bill = float(input("What is your Total Bill? INR "))
tip = int(input("What percentage of tips would you like to provide  ? 10 ,20 ,30 ?"))
people  = int(input("how many people bill would be spilt ?"))
bill_with_tips =tip / 100 *bill + bill
bill_with_per_person = bill_with_tips / people
final_amout =round(bill_with_per_person,2)
print(f"Each person share is :INR {final_amout}")