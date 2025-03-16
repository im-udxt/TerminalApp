from datetime import datetime, timedelta

from terminal_task_manager.models import Priority, Task, TaskStatus

def test_task_creation():
    task = Task(title="Test task")
    assert task.title == "Test task"
    assert task.priority == Priority.MEDIUM
    assert task.status == TaskStatus.PENDING
    assert task.due_date is None

def test_task_completion():
    task = Task(title="Test task")
    task.complete()
    assert task.status == TaskStatus.COMPLETED
    assert task.completed_at is not None

def test_task_overdue():
    # Create a task due yesterday
    past_date = datetime.now() - timedelta(days=1)
    task = Task(title="Test task", due_date=past_date)
    assert task.is_overdue() is True

    # Create a task due tomorrow
    future_date = datetime.now() + timedelta(days=1)
    task = Task(title="Test task", due_date=future_date)
    assert task.is_overdue() is False

    # Completed tasks should not be overdue
    task.complete()
    assert task.is_overdue() is False 