import pytest

from taskflow.storage import (
    add_task,
    complete_task,
    delete_task,
    load_tasks,
    save_tasks,
)


def test_add_task():
    tasks = []
    assert add_task(tasks, 'Learn CI')['id'] == 1
    assert tasks[0]['done'] is False


def test_complete_task():
    tasks = [{'id': 1, 'title': 'Test', 'done': False}]
    complete_task(tasks, 1)
    assert tasks[0]['done'] is True


def test_delete_task():
    tasks = [{'id': 1, 'title': 'Test', 'done': False}]
    delete_task(tasks, 1)
    assert tasks == []


def test_missing_task():
    with pytest.raises(ValueError):
        complete_task([], 99)


def test_empty_title():
    with pytest.raises(ValueError):
        add_task([], '   ')


def test_save_and_load(tmp_path):
    path = tmp_path / 'tasks.json'
    tasks = [{'id': 1, 'title': 'Test', 'done': False}]
    save_tasks(path, tasks)
    assert load_tasks(path) == tasks
