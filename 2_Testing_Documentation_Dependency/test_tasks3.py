import pytest
from tasks3 import add_task, remove_task, list_tasks, clear_tasks

def setup_function():
    clear_tasks()

def test_add_task():
    add_task('Buy groceries')
    assert 'Buy groceries' in list_tasks()

def test_add_empty_task():
    with pytest.raises(ValueError):
        add_task('')

def test_list_tasks():
    add_task('Buy groceries')
    add_task('Read a book')
    assert list_tasks() == ['Buy groceries', 'Read a book']

def test_remove_task():
    add_task('Buy groceries')
    add_task('Read a book')
    remove_task('Buy groceries')
    assert 'Buy groceries' not in list_tasks()
    assert 'Read a book' in list_tasks()

def test_remove_nonexistent_task():
    add_task('Buy groceries')
    result = remove_task('Read a book')
    assert result == "Task not found."
    assert 'Buy groceries' in list_tasks()

def test_clear_tasks():
    add_task('Buy groceries')
    add_task('Read a book')
    result = clear_tasks()
    assert list_tasks() == []
    assert result == "Tasks cleared."