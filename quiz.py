from quiz_data import get_questions


class Quiz:
    def __init__(self):
        self.questions = get_questions(shuffle=True)
        self.score = 0

    def start(self):
        for question in self.questions:
            options_count = len(question.answers)

            question.show()
            answer = self._get_player_choice(options_count)

            if question.is_correct_answer(answer):
                print("Правильно!\n")
                self.score += 1
            else:
                print("Неправильно\n")

        self._print_final_score()

    def _get_player_choice(self, answers_count: int) -> int:
        while True:
            player_input = input(f"Введи число от 1 до {answers_count}: ")

            try:
                selected_option = int(player_input)
                if 1 <= selected_option <= answers_count:
                    return selected_option
            except ValueError:
                pass

    def _print_final_score(self):
        print(f"Результат {self.score}/{len(self.questions)}")
