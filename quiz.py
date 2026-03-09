from question import Question
from quiz_data import get_questions


class Quiz:
    def __init__(self):
        self.questions = get_questions()
        self.score = 0

    def start(self):
        for question in self.questions:
            answers_count = len(question.answers)

            question.print_question()
            your_choice = self._get_answer(answers_count)
            self._show_question_result(question, your_choice)

        self._show_final_result()

    def _show_final_result(self):
        print(f"Результат {self.score}/{len(self.questions)}")

    def _show_question_result(self, question: Question, your_choice: int):
        if question.check_answer(your_choice):
            print("Правильно!\n")
            self._add_score()
        else:
            print("Неправильно\n")

    def _add_score(self):
        self.score += 1

    def _get_answer(self, answers_count: int) -> int:
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
