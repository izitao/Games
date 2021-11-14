from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    #question_text = question["text"]
    #question_answer = question["answer"]
    #print(new_question.text)
    #new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions() == True: #if quiz still has questions remaining
    quiz.next_question()
print(f"You've completed the quiz!")
print(f"your final score was:{quiz.score}/{quiz.question_number}")
