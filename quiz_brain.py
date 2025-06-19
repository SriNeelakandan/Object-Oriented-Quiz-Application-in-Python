# Task 1: 

# Create a QuizBrain class with __init__() method. 
# Initialize question_number =0
# Initialize question_list to an input
class QuizBrain:

    def __init__(self,q_list):
        self.question_number=0
        self.question_list = q_list
        self.score = 0

# Task 2:

# Create a next_question() method
# Retrieve the item at the current question_number from the question_list.
# Use the input() function to show the user question text and ask for text answer

    def next_question(self):
        current_question =self.question_list[self.question_number]
        self.question_number+=1
        user_answer =input(f"\nQ.{self.question_number} : {current_question.question} True/False : ")
        self.check_answer(user_answer,current_question.answer)

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self,u_ans,c_ans):
        if u_ans.lower() == c_ans.lower():
            self.score+=1
            print("You got it right!")
        else:
            print("That's Wrong!")
        print(f"The correct answer is : {c_ans}.")
        print(f"Your current score is {self.score}/{self.question_number}")






# TODO: Asking the questions

# TODO: Checking if the answer was correct

# TODO: checking if we were at the end of the quiz

# QuizBrain class has 

# Attributes

# question_no = 0 (default value)
# questions_list

# Methods

# next_question() 