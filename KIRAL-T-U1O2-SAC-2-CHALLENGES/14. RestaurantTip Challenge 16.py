total_amount = 100
tip = total_amount * 0.15
total_with_tip = total_amount + tip
each_person = total_with_tip / 2
print("Each person should pay", each_person)

bill = float(input("How much was the total bill? "))
people = int(input("How many people are there? "))
tip_percentage = float(input("What percentage tip would you want to leave? "))
tip_amount = bill * (tip_percentage / 100)
total = bill + tip_amount
each_person = total / people
print("Each person should pay:", round(each_person, 2))


