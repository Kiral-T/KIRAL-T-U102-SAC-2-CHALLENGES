
myFile = open("numbers.txt", "wt")
for i in range(6):
    num = input("Enter a number: ")
    myFile.write(num + "\n")
myFile.close()

myFile = open("numbers.txt", "rt")
numbers = []

for line in myFile:
    numbers.append(int(line.strip()))

print("Numbers:", numbers)
print("Total:", sum(numbers))
print("Average:", sum(numbers)/len(numbers))
myFile.close()

myFile = open("numbers.txt", "at")
for i in range(4):
    newNo = input("Enter a new number: ")
    myFile.write(str(newNo) + "\n")
myFile.close()
