import pytest


def test_question_show(question_data, capsys):
    question_data.show()
    captured = capsys.readouterr()
    assert "Вопрос\n1. Ответ 1\n2. Ответ 2" in captured.out


@pytest.mark.parametrize("answer, expected_result", [
    (1, True),
    (2, False),
    (0, False),
    (-1, True),
])
def test_question_is_correct(answer, expected_result, question_data):
    assert question_data.is_correct_answer(answer) == expected_result


@pytest.mark.parametrize("answer", [-2, 3])
def test_question_is_correct_raise_index_error(answer, question_data):
    with pytest.raises(IndexError):
        question_data.is_correct_answer(answer)
