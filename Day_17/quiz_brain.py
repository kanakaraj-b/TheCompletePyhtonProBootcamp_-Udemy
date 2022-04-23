class QuizBrain:
    def __init__(self, q_list):
        self.question_numer = 0
        self.question_list = q_list

    def new_question(self):
        score = 0
        while self.question_numer < len(self.question_list):
        # while self.question_numer < 3:
            current_question = self.question_list[self.question_numer]
            choice = input(f"Q.{self.question_numer + 1}: {current_question.text} (True/False): ")
            self.question_numer += 1
            if choice != current_question.answer:
                print(f"Wrong Answer. \nThe correct answer is: {current_question.answer}")
            else:
                score += 1
                print("Correct Answer")
            print(f"Your Score is {score}/{len(self.question_list)}")
        print("\n\n")
        if score > (len(self.question_list)/2):
            print("Congratulations, Great Game ")
        else:
            print("Good attempt, do more practice")
        print(f"Your total score is {score} out of {len(self.question_list)}")


