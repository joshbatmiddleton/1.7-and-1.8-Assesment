# Version 1 of the Welcome screen.

# Saying hello to the user

question = input("Hello! Welcome to this Māori quiz! Have you played before? ")

# If the user says yes, the program will continue

if question == "yes":
    print("Program will continue")

# If the user says no, then the instructions will show.

elif question == "no":
    print("Show instructions")

# In all other cases, show an error message

else:
    print("ERROR 1: Please answer yes or no.")
