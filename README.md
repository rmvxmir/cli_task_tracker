## CLI Task Tracker

A simple command-line tool to help you manage your tasks, created with Python and Click. The CLI Task Tracker allows you to add, update, delete, list, and manage the progress status of your tasks. Tasks are saved in a JSON file (`data.json`) for persistent storage, making it easy to keep track of tasks between sessions.

## Features

- **Add a Task**: Add a new task with a description.
- **Update a Task**: Update an existing task's description.
- **Delete a Task**: Delete a task by its ID.
- **Mark In Progress**: Mark a task as in-progress.
- **Mark Done**: Mark a task as done.
- **List Tasks**: List all tasks or filter by status (`todo`, `in-progress`, `done`).

## Setup

### Prerequisites

- Python 3.6+
- [Click](https://palletsprojects.com/p/click/) package (can be installed with pip)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/cli-task-tracker.git
   cd cli-task-tracker
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To use the CLI Task Tracker, open a terminal in the project directory and use the following commands:

### Add a Task

Add a task to your task list:
```
python task_tracker.py add "Your task description here"
```

### Update a Task

Update an existing task’s description by its ID:
```
python task_tracker.py update <task_id> "New task description"
```

### Delete a Task

Delete a task by its ID:
```
python task_tracker.py delete <task_id>
```

### Mark as In Progress

Change the status of a task to "in-progress":
```
python task_tracker.py mark-in-progress <task_id>
```

### Mark as Done

Change the status of a task to "done":
```
python task_tracker.py mark-done <task_id>
```

### List Tasks

List all tasks or filter tasks by their status:
```
python task_tracker.py list               # Lists all tasks
python task_tracker.py list todo          # Lists only tasks with status 'todo'
python task_tracker.py list in-progress   # Lists only tasks in progress
python task_tracker.py list done          # Lists only tasks that are done
```

## Example

```
$ python task_tracker.py add "Finish CLI project"
Task added successfully! (ID: 1)

$ python task_tracker.py list
Tasks:
ID:  1 | Task: Finish CLI project     | Status: todo         | Created At: 2023-01-01, 12-00-00 | Last Update: -

$ python task_tracker.py mark-in-progress 1
Task 1 marked as in progress.

$ python task_tracker.py list in-progress
Tasks:
ID:  1 | Task: Finish CLI project     | Status: in-progress  | Created At: 2023-01-01, 12-00-00 | Last Update: 2023-01-01, 12-10-00
```

## Project Structure

- `task_tracker.py`: Main CLI script.
- `data.json`: JSON file used to store tasks and their details (created automatically if not present).

## Contributing

1. Fork this repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and test thoroughly.
4. Submit a pull request.
