# API Documentation

This document describes the internal API of Terminal Task Manager (TTM).

## Models

### Task

```python
class Task(BaseModel):
    """Represents a task in the system."""
    
    id: int
    title: str
    description: Optional[str]
    priority: Priority
    due_date: Optional[datetime]
    status: TaskStatus
    created_at: datetime
    completed_at: Optional[datetime]

    def complete(self) -> None:
        """Mark the task as completed."""
        
    def is_overdue(self) -> bool:
        """Check if the task is overdue."""
```

### Priority

```python
class Priority(str, Enum):
    """Task priority levels."""
    
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
```

### TaskStatus

```python
class TaskStatus(str, Enum):
    """Task completion status."""
    
    PENDING = "pending"
    COMPLETED = "completed"
```

## Storage

### StorageManager

```python
class StorageManager:
    """Manages task persistence."""
    
    def __init__(self, storage_file: Optional[str] = None):
        """Initialize storage manager."""
        
    def add_task(self, task: Task) -> None:
        """Add a new task."""
        
    def update_task(self, task: Task) -> bool:
        """Update an existing task."""
        
    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID."""
        
    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by ID."""
        
    def load_tasks(self) -> List[Task]:
        """Load all tasks."""
        
    def save_tasks(self, tasks: List[Task]) -> None:
        """Save all tasks."""
```

## CLI Commands

### Add Task

```python
@app.command()
def add(
    title: str,
    description: Optional[str] = None,
    priority: Priority = Priority.MEDIUM,
    due: Optional[datetime] = None,
) -> None:
    """Add a new task."""
```

Parameters:
- `title`: Task title (required)
- `description`: Task description (optional)
- `priority`: Task priority (default: medium)
- `due`: Due date (optional)

### List Tasks

```python
@app.command()
def list(show_completed: bool = True) -> None:
    """List all tasks."""
```

Parameters:
- `show_completed`: Whether to show completed tasks (default: True)

### Complete Task

```python
@app.command()
def complete(task_id: int) -> None:
    """Mark a task as completed."""
```

Parameters:
- `task_id`: ID of the task to complete

### Delete Task

```python
@app.command()
def delete(task_id: int) -> None:
    """Delete a task."""
```

Parameters:
- `task_id`: ID of the task to delete

### Search Tasks

```python
@app.command()
def search(keyword: str) -> None:
    """Search tasks by keyword."""
```

Parameters:
- `keyword`: Search term to match against task titles and descriptions

## Data Storage

### File Format

Tasks are stored in JSON format:

```json
[
  {
    "id": 1234567890,
    "title": "Example Task",
    "description": "Task description",
    "priority": "high",
    "due_date": "2024-03-20T15:30:00",
    "status": "pending",
    "created_at": "2024-03-15T10:00:00",
    "completed_at": null
  }
]
```

### Storage Location

- Unix/MacOS: `~/.terminal_task_manager/tasks.json`
- Windows: `%USERPROFILE%\.terminal_task_manager\tasks.json`

## Error Handling

The application handles various error cases:

1. File Operations
   - FileNotFoundError
   - PermissionError
   - JSONDecodeError

2. Data Validation
   - Invalid date formats
   - Missing required fields
   - Invalid priority values

3. Task Operations
   - Task not found
   - Invalid task ID
   - Duplicate task ID

## Dependencies

- `typer`: CLI framework
- `rich`: Terminal formatting
- `pydantic`: Data validation
- `python-dateutil`: Date parsing 