# Took the code from 02_Welcome_Screen_Function_v1 and made it the base for instructions.

# functions go here:

def yes_no(question_text):
    while True:

        # Ask the user if they have played before:
        answer = input(question_text).lower()

        # If they say yes, output "Program continues"

        if answer == "yes" or answer == "Yes" or answer == "Y" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output "display instructions"

        elif answer == "no" or answer == "No" or answer == "N" or answer == "n":
            answer = "No"
            return answer

        # Otherwise, show error message
        else:
            print("ERROR 1: Please answer 'yes' or 'no'(In any format of yes or no).")

# Function to display instructions


def instructions():
    print("******************** How To Play ********************")
    print()
    print()
    print("This is a quiz.")
    print("In this quiz, you will need to answer questions.")
    print("To pass the quiz, you will need to answer a specific amount of questions right.")
    print("If you get it wrong, that's ok!")
    print()
    print("NOTE: Prior knowledge is allowed, replaying the quiz is also allowed,")
    print("Although the answers will not be shown, that will be for you to discover!")
    print()

# Main Routine goes here.


print("Welcome to this Māori quiz!")
played_before = yes_no("Have you played this quiz before? ")
print(f"You entered '{played_before}'")
print()

if played_before == "No":
    instructions()
else:
    print("That's great! Get ready to play")
