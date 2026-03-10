import random
from copy import deepcopy

from answer import Answer
from question import Question

data = [
    Question(
        "Столица России?",
        [
            Answer("Москва", True),
            Answer("Екатеринбург", False),
            Answer("Пенза", False),
            Answer("Новосибирск", False)
        ]
    ),
    Question(
        "Сколько будет 2 + 2?",
        [
            Answer("3", False),
            Answer("4", True),
            Answer("5", False),
            Answer("6", False)
        ]
    ),
    Question(
        "Какого цвета небо в ясную погоду?",
        [
            Answer("Зеленое", False),
            Answer("Синее", True),
            Answer("Красное", False),
            Answer("Черное", False),
            Answer("Желтое", False)
        ]
    ),
    Question(
        "Сколько дней в неделе?",
        [
            Answer("5", False),
            Answer("6", False),
            Answer("7", True)
        ]
    ),
    Question(
        "На каком языке программирования пишутся авто-тесты в Smartway?",
        [
            Answer("Java", False),
            Answer("Python", True),
            Answer("C#", False),
            Answer("TypeScript", False)
        ]
    )
]


def get_questions(shuffle: bool) -> list[Question]:
    questions = deepcopy(data)
    if shuffle:
        for question in questions:
            random.shuffle(question.answers)
        random.shuffle(questions)
    return questions
