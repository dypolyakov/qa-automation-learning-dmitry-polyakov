from question import Question
from quiz_data import get_questions


class Quiz:
    questions = get_questions()
    score = 0

    def start(self):
        for question in self.questions:
            answers_count = len(question.answers)

            question.print_question()
            your_choice = self.get_answer(answers_count)
            self.show_question_result(question, your_choice)

        self.show_final_result()

    def show_final_result(self):
        print(f"Результат {self.score}/{len(self.questions)}")

    def show_question_result(self, question: Question, your_choice: int):
        if question.check_answer(your_choice):
            print("Правильно!\n")
            self.add_score()
        else:
            print("Неправильно\n")

    def add_score(self):
        self.score += 1

    def get_answer(self, answers_count: int) -> int:
        your_choice = input(f"Введи число от 1 до {answers_count}: ")
        while True:
            try:
                your_choice = int(your_choice)
                if 1 <= your_choice <= answers_count:
                    break
                else:
                    your_choice = input(f"Нужно ввести число от 1 до {answers_count}: ")

            except ValueError:
                your_choice = input(f"Нужно ввести число от 1 до {answers_count}: ")
                continue
        return your_choice
