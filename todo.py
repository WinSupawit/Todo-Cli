import sys

def help():
    help = """
        Usage :
            todo help             # Show help
            todo add "todo item"  # Add new todo
            todo ls               # Show remaining tasks
            todo remove NUMBER    # Remove todo
            todo done NUMBER      # Mark task as done
        """
    print(help)

def format():
    try:
        task = open('tasks.txt', 'r')
        order = 1

        for line in task:
            line = line.strip('\n')
            tasks.update({ order: line })
            order = order + 1
    except Exception as e:
        print(e)
        print("There is no tasks!")


def add(todo):
    task = open('tasks.txt', 'a')
    task.write(todo)
    task.write('\n')
    task.close()

    print(f"Task added: {todo}.")

def ls():
    format()

    if len(tasks) == 0:
        print("There is no task!")
    else:
        for i in tasks:
            print(f"[{i}] {tasks[i]}")
            i = i + 1

def remove(n):
    format()
    no = int(n)

    task = open('tasks.txt', 'r+')
    lines = task.readlines()
    task.seek(0)
    for i in lines:
        if i.strip('\n') != tasks[no]:
            task.write(i)
    task.truncate()

    print(f"Removed task #{no}.")

def done(n):
    format()
    no = int(n)

    task = open('tasks.txt', 'r+')
    lines = task.readlines()
    task.seek(0)
    for i in lines:
        if i.strip('\n') != tasks[no]:
            task.write(i)
    task.truncate()

    print(f"Marked task #{no} as done.")

if __name__ == '__main__':
    try:
        tasks = {}
        args = sys.argv

        if (args[1] == 'add' and len(args[2:]) == 0):
            print("Error: Missing task string.")
        elif (args[1] == 'done' and len(args[2:]) == 0):
            print("Error: Missing task number.")
        elif (args[1] == 'remove' and len(args[2:]) == 0):
            print("Error: Missing task number.")
        else:
            globals()[args[1]](*args[2:])
    except Exception as e:
        help()
