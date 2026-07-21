# To-Do List Manager

DecodeLabs – Python Programming Industrial Training Kit
**Project 1: The To-Do List**

A command-line to-do list manager built with Python. Demonstrates working with lists, loops, and basic file I/O for data persistence.

## Features
- Add tasks to your list
- View all tasks with their completion status
- Remove tasks by number
- Mark tasks as complete
- Tasks automatically saved to `tasks.json` and reloaded on startup, so your list survives closing the program

## How to Run
```bash
python todo.py
```

Then follow the on-screen menu (options 1–5) to manage your tasks.

## Key Concepts Used
- Lists and dictionaries (`append`, `pop`, `enumerate`)
- Functions and separation of concerns (menu, add, view, remove, complete)
- File I/O with the `json` module for saving/loading data
- Basic input validation and error handling (`try`/`except`, empty-input checks)

## Files
- `todo.py` — main program
- `tasks.json` — auto-generated file storing your saved tasks (created on first run)
