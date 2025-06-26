pictures_per_month = int(input("How many pictures do you often send per month? "))
texts = int(input("How many texts per month? "))
data = int(input("How many MB of data do you use per month? "))
total = pictures * 0.35 + texts * 0.10 + data * 0.05
print("You total bill is $", round(total, 2))
if total > 10:
    print("Your better off on a contract.")

