from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]
    new_question = Question(question_text,question_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("\nYou completed the Quiz")
print(f"Your Final Score was : {quiz.score}/{len(quiz.question_list)}")