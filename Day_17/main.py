from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


bank = question_data

q = []
for i in range(len(bank)):
    q_mine = bank[i]
    text = q_mine["text"]
    answer = q_mine["answer"]
    new_q = Question(text, answer)
    q.append(new_q)

quiz = QuizBrain(q)
New_question = QuizBrain.new_question(quiz)






