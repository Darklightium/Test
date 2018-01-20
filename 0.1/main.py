import random

count = 0

answer_count = 0
question_number = int(input("How muany questions do you want to have?\n"))

while count < question_number:
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    print(number_1, "+", number_2)
    right_answer = number_1 + number_2
    answer = int(input())
    if answer == right_answer:
        answer_count = answer_count + 1
    count = count + 1
print("Right answers are", answer_count, "of",question_number)




