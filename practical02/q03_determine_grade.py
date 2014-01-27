#3 Determining a grade from a score:

score = float(input("Please enter your score(0-100 inclusive) here: "))

if 70 <= score <= 100:
    print("Your grade is an A.")
elif 60 <= score <= 69:
    print("Your grade is a B.")
elif 55 <= score <= 59:
    print("Your grade is a C.")
elif 50 <= score <= 54:
    print("Your grade is a D.")
elif 45 <= score <= 49:
    print("Your grade is an E.")
elif 35 <= score <= 44:
    print("Your grade is an S.")
elif 0 <= score <= 34:
    print("Your grade is a U.")
else:
    print("You did not enter a valid score. Your score must be between 0-100 inclusive.")
