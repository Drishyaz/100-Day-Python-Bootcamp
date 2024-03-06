
class Question:
    # this class contains the question and its answer in separate variables
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
        self.q_num = 0

    def __str__(self):
        self.q_num += 1
        return f"Q.{self.q_num}: {self.text} (True/False)?: "
