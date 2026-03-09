from answer import Answer
from question import Question

data = [
    Question(
        "Столица России?",
        [
            Answer("Москва", True),
            Answer("Екатеринбург", False),
            Answer("Пенза", False),
            Answer("Санкт-Петербург", False)
        ]
    ),
    Question(
        "Какого цвета трава?",
        [
            Answer("Красный", False),
            Answer("Зеленый", True),
            Answer("Синий", False)
        ]
    )
]


def get_questions() -> list[Question]:
    return data
