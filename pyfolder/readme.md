# Todo CLI App (Python)

A simple command-line todo list manager written in Python. Tasks are saved in a local JSON file and can be added, listed, and marked as done.

---

## Features

- Add tasks from the command line
- List all current tasks with status (✓/✗)
- Mark tasks as done
- Stores data in `todos.json`

---

## Usage

### List tasks
```bash
python3 main.py
```

### Add a task
```bash
python3 main.py add "Buy coffee"
```

### Mark task as done
```bash
python3 main.py done 1
```

---

## Data Format

Tasks are stored in `todos.json` as:
```json