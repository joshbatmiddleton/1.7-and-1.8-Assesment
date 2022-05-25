# 00 Base Component

# NOTE: This is NOT the final version of the base component,
# nor is it a completely finished and polished piece of code.

# Function for game:
def game():
    # Code to do functions:

    import random
    score = 0

    # Function goes here:

    def yes_no(question_text):
        while True:
            answer_1 = input(question_text).lower()

            # If they say yes, output "Program continues"

            if answer_1 == "yes" or answer_1 == "Yes" or answer_1 == "Y" or answer_1 == "y":
                answer_1 = "Yes"
                return answer_1

            # If they say no, output "display instructions"

            elif answer_1 == "no" or answer_1 == "No" or answer_1 == "N" or answer_1 == "n":
                answer_1 = "No"
                return answer_1

            # Otherwise, show error message
            else:
                print("ERROR 1: Please answer 'yes' or 'no'(In any format of yes or no).")

    # Function to display instructions

    def instructions():
        print("********************************* How To Play *********************************")
        print()
        print()
        print("This is a quiz.")
        print("In this quiz, you will need to answer questions.")
        print("To pass the quiz, you will need to answer a specific amount of questions right.")
        print("If you get it wrong, that's ok!")
        print()
        print("NOTE: Prior knowledge is allowed, replaying the quiz is also allowed.")
        print("Also, the answers will not be shown, that will be for you to discover!")
        print()

    # Main Routine goes here.

    # Ask the user if they have played before:

    print("Welcome to this Māori quiz!")
    print()
    played_before = yes_no("Have you played this quiz before? ")
    print()
    print(f"You entered '{played_before}'")
    print()

    if played_before == "No":
        instructions()
    else:
        print("That's great! Get ready to play")
    print()
    start_game = yes_no("Do you want to start? ")
    print(f"You entered '{start_game}'")

    # Import code

    print()
    print("Get ready to answer 5 questions!!!")

    # 1st list

    numbers_in_words = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

    # 2nd list

    maori_numbers = ["Tāhi", "Rua", "Toru", "Wha", "Rima", "Ono", "Whētu", "Waru", "Iwa", "Tekāu"]
    for i in maori_numbers:
        question = random.choice(numbers_in_words)
        print()
        attempt = input(f"What is the Māori number for {question}: ")

        # Using the index position of the question in one list to find the corresponding
        # index position of the answer

        answer_index = numbers_in_words.index(question)
        answer = maori_numbers[answer_index]

        # Compare the attempt to see if it matches the correct answer

        if attempt == answer:
            print("Correct! Well done!")
            score += 1

        else:
            print("Incorrect!")

        print(score)

# Main routine (Will be down here eventually)
