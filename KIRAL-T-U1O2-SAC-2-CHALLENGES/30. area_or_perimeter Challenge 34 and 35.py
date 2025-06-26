def area(length, width):
    shapes_Area = length * width
    print("Area =", shapes_Area)

def perimeter(length, width):
    shapes_Perimeter = length*2 + width*2
    print("Perimeter =", shapes_Perimeter)

response = None
while response not in ("a", "p"):
    response = input("Which one would you want to calculate? Area or Perimeter? Type a/p to confirm: ").lower()

length = int(input("Enter the length: "))
width = int(input("Enter the width: "))

if response == "a":
    area(length, width)
else:
    perimeter(length, width)
