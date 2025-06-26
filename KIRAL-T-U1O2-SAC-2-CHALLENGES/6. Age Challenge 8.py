name = input("Enter your name: ")
age = int(input("Enter your age: "))

days = age * 365
hours = days * 24
minutes = hours * 60
seconds  = minutes* 60

print(name + ", you have been alive for:")
print(days, "days")
print(hours, "hours")
print(minutes, "minutes")
print(seconds, "seconds")