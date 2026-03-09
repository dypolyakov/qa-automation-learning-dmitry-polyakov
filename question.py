from answer import Answer


class Question:
    def __init__(self, text: str, answers: list[Answer]):
        self.text = text
        self.answers = answers

    def print_question(self):
        print(self.text)
        for i, answer in enumerate(self.answers, start=1):
            print(f"{i}. {answer.text}")
        print()


    def check_answer(self, choice: int) -> bool:
        return self.answers[choice - 1].is_correct