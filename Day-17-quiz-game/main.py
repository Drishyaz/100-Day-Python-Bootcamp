# LIVE DEMO: https://replit.com/@guardianblossom/Day-17-quiz-gamepy#main.py

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

category_chosen = input("Which category do you want to try?\n1.Anime and Manga.\n2.Fun Facts.\n3.Science and "
                        "Nature.\n4.Computer Science.\n(1/2/3/4)? ")
# first look for the category, if found, store its questions
for item in question_data:
    # if item["category"].lower() == category_chosen.lower():
    #     category = item["questions"]
    if item["id"] == int(category_chosen):
        category = item["questions"]

# contains a list of all the questions
question_bank = []
# iterating through each item in the question_data
for question in category:
    # since each item in the list is a dictionary: ques retrieves the question, ans retrieves the answer
    ques = question["text"]
    ans = question["answer"]
    new_question = Question(q_text=ques, q_answer=ans)
    # append each question to the question_bank
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
# if quiz still has questions remaining
while quiz.still_has_questions():
    quiz.next_question()

print("\nThe Game has ended..")
