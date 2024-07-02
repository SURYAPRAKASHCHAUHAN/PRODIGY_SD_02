import random 
mynum = random.randrange(1,100)

usernum= int(input("Enter your Guess:"))

while mynum!=usernum:

    if usernum < mynum:
        print("Your number is low")
        usernum= int(input("Enter your Guess:"))

    elif usernum > mynum:
        print("Your number is high")
        usernum= int(input("Enter your Guess:"))

    else:
        break

print("Your Guess is right!")
