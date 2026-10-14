import argparse
from pathlib import Path
from .storage import load_tasks, save_tasks, add_task, complete_task, delete_task


def main():
    parser = argparse.ArgumentParser(description='Simple task manager')
    parser.add_argument('--file', type=Path, default=Path('tasks.json'))
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('list')
    add = commands.add_parser('add')
    add.add_argument('title')
    done = commands.add_parser('done')
    done.add_argument('id', type=int)
    delete = commands.add_parser('delete')
    delete.add_argument('id', type=int)
    args = parser.parse_args()
    tasks = load_tasks(args.file)
    try:
        if args.command == 'add':
            task = add_task(tasks, args.title)
            print(f"Added task {task['id']}")
        elif args.command == 'done':
            complete_task(tasks, args.id)
            print(f'Completed task {args.id}')
        elif args.command == 'delete':
            delete_task(tasks, args.id)
            print(f'Deleted task {args.id}')
        else:
            for task in tasks:
                print(f"{task['id']}. [{'x' if task['done'] else ' '}] {task['title']}")
            return
    except ValueError as error:
        parser.error(str(error))
    save_tasks(args.file, tasks)


if __name__ == '__main__':
    main()
