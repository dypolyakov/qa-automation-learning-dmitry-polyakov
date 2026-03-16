import pytest

from answer import Answer
from question import Question


@pytest.fixture
def question_data():
    return Question("Вопрос",
                    [Answer("Ответ 1", True), Answer("Ответ 2", False)])
