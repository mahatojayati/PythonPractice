#to_do list lets  you add, remove, and manage tasks
def add_task(task, task_list):
    """Add a task to the task list."""
    task_list.append(task)
    return task_list
def remove_task(task, task_list):
    """Remove a task from the task list."""
    if task in task_list:
        task_list.remove(task)
    else:
        print(f"Task '{task}' not found in the list.")
    return task_list
def view_tasks(task_list):
    """View all tasks in the task list."""
    if not task_list:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task}")
    return task_list
def clear_tasks(task_list):
    """Clear all tasks from the task list."""
    task_list.clear()
    print("All tasks cleared.")
    return task_list
def main():
    """Main function to run the task manager."""
    task_list = []
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Clear Tasks")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task, task_list)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task, task_list)
        elif choice == '3':
            view_tasks(task_list)
        elif choice == '4':
            clear_tasks(task_list)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
# This code provides a simple command-line interface for managing a to-do list.
# You can add, remove, view, and clear tasks.
# The tasks are stored in a list, and the user can interact with the program through a