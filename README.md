# Terminal Task Manager (TTM)

A cross-platform terminal application for managing your daily tasks efficiently. Built with Python and modern terminal UI libraries, TTM provides a clean interface for organizing your tasks right from the command line.

## Features

- 📝 Add, remove, and list tasks
- ⭐ Set task priorities and due dates
- ✅ Mark tasks as completed
- 🔍 Search and filter tasks
- 💾 Persistent storage using JSON
- 🎨 Beautiful terminal UI

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Install from source

1. Clone the repository:
```bash
git clone https://github.com/im-udxt/terminalapp.git
cd terminal-task-manager
```

2. Install the package in editable mode:
```bash
pip install -e .
```

## Usage

After installation, you can run the task manager using:

```bash
ttm
```

### Common Commands

- Add a task: `ttm add "Task description" --priority high --due "2024-03-20"`
- List tasks: `ttm list`
- Complete a task: `ttm complete <task-id>`
- Delete a task: `ttm delete <task-id>`
- Search tasks: `ttm search "keyword"`

## Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install development dependencies:
```bash
pip install -e ".[dev]"
```

3. Run tests:
```bash
pytest tests/
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 