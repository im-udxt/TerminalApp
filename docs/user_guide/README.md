# User Guide

This guide will help you get started with Terminal Task Manager (TTM) and show you how to use its features effectively.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installing from Source

1. Clone the repository:
```bash
git clone https://github.com/im-udxt/terminalapp.git
cd terminalapp
```

2. Install the package:
```bash
pip install -e .
```

## Basic Usage

### Starting TTM

After installation, you can start TTM by running:

```bash
ttm
```

### Task Management

#### Adding Tasks

```bash
# Basic task
ttm add "Buy groceries"

# Task with priority
ttm add "Prepare presentation" --priority high

# Task with due date
ttm add "Submit report" --due "2024-03-20"

# Task with both priority and due date
ttm add "Team meeting" --priority medium --due "2024-03-19 14:00"
```

#### Listing Tasks

```bash
# List all tasks
ttm list

# List only pending tasks
ttm list --show-completed false
```

#### Completing Tasks

```bash
# Mark a task as completed
ttm complete <task-id>
```

#### Deleting Tasks

```bash
# Delete a task
ttm delete <task-id>
```

#### Searching Tasks

```bash
# Search tasks containing keyword
ttm search "meeting"
```

## Task Properties

### Priority Levels

- `low`: Low priority tasks
- `medium`: Medium priority tasks (default)
- `high`: High priority tasks

### Task Status

- `pending`: Tasks that are not completed
- `completed`: Tasks that have been marked as done

### Due Dates

- Format: "YYYY-MM-DD" or "YYYY-MM-DD HH:MM"
- Examples:
  - `2024-03-20`
  - `2024-03-20 15:30`

## Storage

Tasks are automatically saved to:
- Unix/MacOS: `~/.terminal_task_manager/tasks.json`
- Windows: `%USERPROFILE%\.terminal_task_manager\tasks.json`

## Tips and Best Practices

1. **Regular Updates**: Keep your task list current by marking completed tasks
2. **Priority Usage**: Use priorities wisely to focus on important tasks
3. **Due Dates**: Set realistic due dates to better manage your time
4. **Search**: Use the search function to quickly find related tasks
5. **Backup**: The tasks file can be backed up from the storage location

## Troubleshooting

### Common Issues

1. **Command Not Found**
   - Ensure TTM is installed correctly
   - Check if Python is in your PATH
   - Try reinstalling the package

2. **Task Not Saving**
   - Check write permissions in the storage directory
   - Ensure sufficient disk space

3. **Date Format Errors**
   - Use the correct date format (YYYY-MM-DD)
   - Check for typos in the date string

### Getting Help

If you encounter issues:

1. Check this documentation
2. Visit our [GitHub Issues](https://github.com/im-udxt/terminalapp/issues)
3. Create a new issue with:
   - Command used
   - Error message
   - Your system information 