# Takes Version 1 code and makes it more efficient and reliable.

# Saying hello to the user

print("Hello! Welcome to this Māori quiz!")
question = input("Have you played before? ").lower()

# If the user says yes, the program will continue

if question == "yes" or question == "Yes" or question == "Y" or question == "y":
    print("Program will continue")

# If the user says no, then the instructions will show.

elif question == "no" or question == "No" or question == "n" or question == "N":
    print("Show instructions")

# In all other cases, show an error message

else:
    print("ERROR 1: Please answer yes or no.")

print(f"You entered '{question}'")
