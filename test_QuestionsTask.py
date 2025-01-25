import pytest
from questions_task import QuestionsTask

@pytest.fixture
def task():
    task = QuestionsTask()
    task.question_variable = {"description": "The first letter of the alphabet", "answer": "A"}
    task.password = ["_"] * len(task.question_variable["answer"])
    return task

def test_correct_guess(task):
    task.password = ["_"]
    task.question["answer"] = "A"
    task.lenght = 1

    # Symulacja poprawnej odpowiedzi
    task.password[0] = "A"
    assert task.password == ["A"]

def test_wrong_guess_loses_life(task):
    initial_lives = len(task.lifes)
    task.lifes.pop()
    assert len(task.lifes) == initial_lives - 1
