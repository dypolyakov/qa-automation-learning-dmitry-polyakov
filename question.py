from answer import Answer


class Question:
    def __init__(self, text: str, answers: list[Answer]):
        self.text = text
        self.answers = answers

    def show(self):
        print(self.text)
        for i, answer in enumerate(self.answers, start=1):
            print(f"{i}. {answer.text}")
        print()

    def is_correct_answer(self, answer: int) -> bool:
        return self.answers[answer - 1].is_correct
