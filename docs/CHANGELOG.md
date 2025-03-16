# Changelog

All notable changes to Terminal Task Manager will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-03-15

### Added
- Initial release
- Basic task management functionality
  - Add, list, complete, and delete tasks
  - Task priorities (low, medium, high)
  - Due dates for tasks
  - Task completion status
- JSON-based persistent storage
- Rich terminal UI
- Search functionality
- Cross-platform support (Windows, MacOS, Linux)

### Dependencies
- Python >=3.8
- textual>=0.47.1
- rich>=13.7.0
- typer>=0.9.0
- pydantic>=2.5.0 