import sys, os, json

data_file = "todos.json"

def load_todos():
    if not os.path.isfile(data_file):
        return []
    try:
        return json.load(open(data_file))
    except json.JSONDecodeError:
        return []

def save_todos(todos):
    json.dump(todos, open(data_file, "w"), indent=2)

def add_task(task):
    todos = load_todos()
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print(f"Added: {task}")

def list_tasks():
    todos = load_todos()
    if not todos:
        print("No tasks found.")
        return
    for i, todo in enumerate(todos, 1):
        print(f"{i}. {'✓' if todo['done'] else '✗'} {todo['task']}")

def mark_done(index):
    todos = load_todos()
    if 0 < index <= len(todos):
        todos[index - 1]["done"] = True
        save_todos(todos)
        print(f"Marked task {index} as done.")
    else:
        print(f"No task found at position {index}.")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        list_tasks()
    else:
        cmd, *args = sys.argv[1:]
        if cmd == "add":
            add_task(" ".join(args))
        elif cmd == "done":
            mark_done(int(args[0]))
        else:
            print("Usage:")
            print("  python3 main.py           # list tasks")
            print("  python3 main.py add TASK  # add task")
            print("  python3 main.py done N    # mark task N done")