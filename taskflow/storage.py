import json
from pathlib import Path


def load_tasks(path):
    path = Path(path)
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding='utf-8'))


def save_tasks(path, tasks):
    Path(path).write_text(json.dumps(tasks, indent=2), encoding='utf-8')


def add_task(tasks, title):
    if not title.strip():
        raise ValueError('Task title cannot be empty')
    task = {'id': max((t['id'] for t in tasks), default=0) + 1, 'title': title, 'done': False}
    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            return
    raise ValueError(f'Task {task_id} not found')


def delete_task(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return
    raise ValueError(f'Task {task_id} not found')
