import random

print("Get ready to answer 10 questions!!!")

# 1st list
numbers_in_words = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

# 2nd list
maori_numbers = ["Tahi", "Rua", "Toru", "Wha", "Rima", "Ono", "Whētu", "Waru", "Iwa", "Tekāu"]

question = random.choice(numbers_in_words)
attempt = input(f"What is the Māori number for {question}: ")
# Using the index position of the question in one list to find the corresponding
# index position of the answer

answer_index = numbers_in_words.index(question)
answer = maori_numbers[answer_index]

# Compare the attempt to see if it matches the correct answer
if attempt == answer:
    print("Correct! Well done!")

else:
    print("Incorrect!\n")
