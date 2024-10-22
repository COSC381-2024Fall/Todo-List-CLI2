# todo.py

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Adds a new task to the list."""
        self.tasks.append(task)
        print(f'Task added: {task}')

    def edit_task(self, task_number, new_task):
        """Edits an existing task"""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            self.tasks[task_number - 1] = new_task
            print(f'Task updated: {new_task}')

    def list_tasks(self):
        """Lists all tasks in the to-do list."""
        if not self.tasks:
            print("No tasks in the list!")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f'{idx}. {task}')

    def delete_task(self, task_number):
        """Deletes a task by its number in the list."""
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number!")
        else:
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task removed: {removed_task}')


def print_menu():
    print("\nTo-Do List CLI App")
    print("1. Add task")
    print("2. List tasks")
    print("3. Delete task")
    print("4. Edit task")
    print("5. Quit")


def main():
    todo_list = TodoList()

    while True:
        print_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)

        elif choice == '2':
            todo_list.list_tasks()

        elif choice == '3':
            try:
                task_number = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif choice == '4':
            task_number = int(input("Enter task number to edit: "))
            new_task = input("Enter the updated task: ")
            todo_list.edit_task(task_number, new_task)

        elif choice == '5':
            print("Exiting To-Do List CLI App. Goodbye!")
            break

        else:
            print("Invalid choice! Please choose a valid option.")


if __name__ == '__main__':
    main()
