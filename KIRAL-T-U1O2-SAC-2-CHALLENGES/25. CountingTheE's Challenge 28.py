sentence = input("Type a sentence: ")
numberE = 0

for letter in sentence:
    if letter == "e":
        numberE += 1
print("The number of e's that is in the sentence is:", numberE)

vowels = "aeiou"
count = 0

for letter in sentence:
    if letter.lower() in vowels:
        count += 1
print("The number of vowels is:", count)