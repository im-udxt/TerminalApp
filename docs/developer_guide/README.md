# Developer Guide

This guide provides information for developers who want to contribute to or modify the Terminal Task Manager (TTM).

## Project Structure

```
terminal-task-manager/
├── docs/                  # Documentation
├── src/                   # Source code
│   └── terminal_task_manager/
│       ├── __init__.py   # Package initialization
│       ├── cli.py        # Command-line interface
│       ├── models.py     # Data models
│       └── storage.py    # Storage management
├── tests/                # Test files
├── LICENSE              # MIT license
├── README.md           # Project readme
└── pyproject.toml      # Project configuration
```

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/im-udxt/terminalapp.git
cd terminalapp
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Unix/MacOS
# or
venv\Scripts\activate     # On Windows
```

3. Install development dependencies:
```bash
pip install -e ".[dev]"
```

## Core Components

### Models (`models.py`)

The `Task` model is defined using Pydantic for data validation:

```python
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: Priority
    due_date: Optional[datetime]
    status: TaskStatus
    created_at: datetime
    completed_at: Optional[datetime]
```

### Storage (`storage.py`)

The `StorageManager` class handles:
- JSON file operations
- Task serialization/deserialization
- CRUD operations for tasks

### CLI (`cli.py`)

The command-line interface uses Typer and Rich for:
- Command parsing
- Terminal UI rendering
- User interaction

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_models.py

# Run with coverage
pytest --cov=terminal_task_manager
```

### Writing Tests

1. Create test files in the `tests/` directory
2. Use descriptive test names
3. Follow the existing test structure
4. Include both positive and negative test cases

Example:
```python
def test_task_creation():
    task = Task(title="Test task")
    assert task.title == "Test task"
    assert task.priority == Priority.MEDIUM
```

## Contributing

### Guidelines

1. Fork the repository
2. Create a feature branch
3. Write clear commit messages
4. Add tests for new features
5. Update documentation
6. Submit a pull request

### Code Style

- Follow PEP 8 guidelines
- Use type hints
- Document functions and classes
- Keep functions focused and small

### Pull Request Process

1. Update the README.md if needed
2. Update the documentation
3. Ensure all tests pass
4. Request review from maintainers

## Building and Distribution

### Building the Package

```bash
python -m build
```

### Running Quality Checks

```bash
# Run linter
flake8 src/terminal_task_manager

# Run type checker
mypy src/terminal_task_manager
```

## Architecture Decisions

### Storage Format

JSON was chosen for:
- Human readability
- Easy debugging
- No external dependencies
- Cross-platform compatibility

### CLI Framework

Typer was selected for:
- Modern Python features
- Automatic help generation
- Type hint support
- Rich integration

## Future Development

Planned features:
1. Task categories/tags
2. Recurring tasks
3. Task dependencies
4. Data export/import
5. Multiple storage backends

## Security Considerations

1. File permissions
   - Storage file uses user directory
   - Appropriate file permissions

2. Data validation
   - Input sanitization
   - Type checking
   - Pydantic validation 