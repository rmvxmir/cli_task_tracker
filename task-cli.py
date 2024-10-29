# Import all necessary modules
import click
import os
import json
from datetime import datetime

# JSON manipulations
DATA_FILE = 'data.json'

def create_default_json():
    default_data = {
        'tasks' : []
    }
    with open(DATA_FILE, 'w') as f:
        json.dump(default_data, f, indent=4)

def load_data():
    if not os.path.exists(DATA_FILE):
        create_default_json()

    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# 'Add' command
@click.command(name='add')
@click.argument('task')
def add(task):
    data = load_data()

    if data['tasks']:
        task_id = data['tasks'][-1]['id'] + 1
    else:
        task_id = 1
    
    new_task = {
        'id' : task_id,
        'description' : task,
        'status' : 'todo',
        'createdAt' : datetime.now().strftime("%Y-%m-%d, %H-%M-%S"),
        'updatedAt' : '-'
    }

    data['tasks'].append(new_task)
    save_data(data)

    click.echo(f'Task added successfully! (ID: {task_id})')

# 'Update' command
@click.command(name='update')
@click.argument('input_id')
@click.argument('new_task')

def update_task(input_id, new_task):
    data = load_data()

    found = False

    for task in data['tasks']:
        if task['id'] == int(input_id):
            task['description'] = new_task
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d, %H-%M-%S")
            save_data(data)

            click.echo(f'Task {input_id} updated successfully!')

            found = True
            break
    if not found:
        click.echo('Task is not found.')

# 'Delete' command
@click.command(name='delete')
@click.argument('input_id')

def delete_task(input_id):
    data = load_data()

    found = False

    for task in data['tasks']:
        if task['id'] == int(input_id):
            data['tasks'].remove(task)
            save_data(data)

            click.echo(f'Task {input_id} deleted successfully!')

            found = True
            break
    if not found:
        click.echo('Task is not found.')

# 'Mark in progress' command
@click.command(name='mark-in-progress')
@click.argument('input_id')

def mark_in_progress(input_id):
    data = load_data()

    found = False

    for task in data['tasks']:
        if task['id'] == int(input_id):
            task['status'] = 'in-progress'
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d, %H-%M-%S")
            save_data(data)

            click.echo(f'Task {input_id} marked as in progress.')

            found = True
            break
    if not found:
        click.echo('Task is not found.')

# 'Mark done' command
@click.command(name='mark-done')
@click.argument('input_id')

def mark_done(input_id):
    data = load_data()

    found = False

    for task in data['tasks']:
        if task['id'] == int(input_id):
            task['status'] = 'done'
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d, %H-%M-%S")
            save_data(data)

            click.echo(f'Task {input_id} marked as done.')

            found = True
            break
    if not found:
        click.echo('Task is not found.')

# 'List' command
@click.command(name='list')
@click.argument('status', required=False)

def list_tasks(status):
    data = load_data()

    tasks_to_display = data['tasks']
    
    # If a status is provided, filter tasks
    if status:
        tasks_to_display = [task for task in data['tasks'] if task['status'] == status]

    if tasks_to_display:
        click.echo('Tasks:')
        for task in tasks_to_display:
            click.echo(f'ID: {task["id"]:2} | Task: {task["description"]:20} | Status: {task["status"]:12} | '
                    f'Created At: {task["createdAt"]} | Last Update: {task["updatedAt"]}')
    else: click.echo('No tasks found.')

# Creating a group for multiple commands
@click.group()
def cli():
    pass

# Add commands to the group
cli.add_command(add)
cli.add_command(list_tasks)
cli.add_command(update_task)
cli.add_command(delete_task)
cli.add_command(mark_in_progress)
cli.add_command(mark_done)

if __name__ == '__main__':
    cli()