import random

count = 0
answer = 0
answer_count = 0
question_number = int(input("How muany questions do you want to have?\n"))

while count < question_number:
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    print(number_1, "+", number_2, "=")
    right_answer = number_1 + number_2
    input(answer)
    if answer == right_answer:
        answer_count = + 1
    count = + 1
print("Right answers are", answer_count, "of",question_number)




