password = "somethingsomethingpassword123"
guess = input("Enter the secret password: ")
if guess == password:
    print("Access granted!")
else:
    print("Wrong password!")
