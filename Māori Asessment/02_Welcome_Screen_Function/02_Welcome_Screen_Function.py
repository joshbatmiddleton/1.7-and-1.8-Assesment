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
            print("Please answer 'yes' or 'no'.")


# Main Routine goes here.

print("Hello! Welcome to this Māori quiz!")
question = yes_no("Have you played this quiz before? ")
print(f"You entered '{question}'")
print()
start_game = yes_no("Do you want to start? ")
print(f"You entered '{start_game}'")
