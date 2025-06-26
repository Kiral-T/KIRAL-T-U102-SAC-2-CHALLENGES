import time
name = input("Enter your name ")
print(name + "'s calorie counter")
time.sleep(3)
calories = int(input("How many calories have you eaten today? "))
caloriecounter = 2000 - calories
print("You can eat", caloriecounter, "more calories today.")