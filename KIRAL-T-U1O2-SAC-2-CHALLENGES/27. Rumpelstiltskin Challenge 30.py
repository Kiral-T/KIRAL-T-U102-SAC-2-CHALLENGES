#this program tells the user to guess the name of him.
name = ""
while name != "Rumpelstiltskin":
    name = input("Guess my name: ")
    if name != "Rumpelstiltskin":
        print("That's wrong! Try again.")
print("Wow you guessed it! Welcome, " + name)