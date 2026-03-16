# Викторина
Вопросы и варианты ответов выводятся в случайном порядке

## Запуск программы:
```commandline
python main.py
```

## Запуск тестов:
### Установка зависимостей

1. Создать виртуальное окружение
```commandline
python -m venv .venv
```

2. Активировать виртуальное окружение
```commandline
source .venv/bin/activate
```

3. Установить все зависимости
```commandline
pip install -r requirements.txt
```

### Запуск тестов с помощью pytest
Запустить все тесты
```commandline
python -m pytest
```

Запустить позитивные тесты
```commandline
python -m pytest -k positive
```

Запустить негативные тесты
```commandline
python -m pytest -k negative
```


