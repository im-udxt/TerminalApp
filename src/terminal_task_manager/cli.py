from datetime import datetime
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from .models import Priority, Task, TaskStatus
from .storage import StorageManager

app = typer.Typer()
console = Console()
storage = StorageManager()

def _create_task_table(tasks: list[Task], show_completed: bool = True) -> Table:
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim")
    table.add_column("Title")
    table.add_column("Priority", justify="center")
    table.add_column("Due Date", justify="center")
    table.add_column("Status", justify="center")

    for task in tasks:
        if not show_completed and task.status == TaskStatus.COMPLETED:
            continue

        status_color = "green" if task.status == TaskStatus.COMPLETED else "yellow"
        if task.is_overdue():
            status_color = "red"

        due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else "-"
        table.add_row(
            str(task.id),
            task.title,
            task.priority.value,
            due_date,
            f"[{status_color}]{task.status.value}[/{status_color}]"
        )
    return table

@app.command()
def add(
    title: str,
    description: Optional[str] = None,
    priority: Priority = Priority.MEDIUM,
    due: Optional[datetime] = None,
):
    """Add a new task."""
    task = Task(
        title=title,
        description=description,
        priority=priority,
        due_date=due,
    )
    storage.add_task(task)
    console.print(f"✅ Added task: {title}")

@app.command()
def list(show_completed: bool = True):
    """List all tasks."""
    tasks = storage.load_tasks()
    if not tasks:
        console.print("No tasks found!")
        return

    table = _create_task_table(tasks, show_completed)
    console.print(table)

@app.command()
def complete(task_id: int):
    """Mark a task as completed."""
    task = storage.get_task(task_id)
    if not task:
        console.print(f"❌ Task {task_id} not found!")
        return

    task.complete()
    storage.update_task(task)
    console.print(f"✅ Marked task {task_id} as completed!")

@app.command()
def delete(task_id: int):
    """Delete a task."""
    if storage.delete_task(task_id):
        console.print(f"🗑️ Deleted task {task_id}")
    else:
        console.print(f"❌ Task {task_id} not found!")

@app.command()
def search(keyword: str):
    """Search tasks by keyword."""
    tasks = storage.load_tasks()
    matching_tasks = [
        task for task in tasks
        if keyword.lower() in task.title.lower()
        or (task.description and keyword.lower() in task.description.lower())
    ]

    if not matching_tasks:
        console.print(f"No tasks found matching '{keyword}'")
        return

    table = _create_task_table(matching_tasks)
    console.print(table)

if __name__ == "__main__":
    app() 