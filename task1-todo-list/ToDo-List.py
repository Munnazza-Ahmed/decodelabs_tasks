"""
Project 1: The To-Do List
DecodeLabs - Python Programming Industrial Training Kit
Goal: Build a program where users can add tasks to a list and view them.
Key Skill: Lists (append & print loops)
"""

def display_menu():
    """Displays the main menu options to the user."""
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove a Task")
    print("4. Mark Task as Complete")
    print("5. Exit")
    print("===============================")


def add_task(my_tasks):
    """Adds a new task to the list."""
    task = input("Enter the task you want to add: ").strip()
    if task == "":
        print("⚠ Task cannot be empty. Please try again.")
        return
    my_tasks.append({"task": task, "done": False})
    print(f"✅ Task added: '{task}'")


def view_tasks(my_tasks):
    """Displays all tasks currently stored in the list."""
    print("\n----- YOUR TASKS -----")
    if not my_tasks:
        print("No tasks yet. Add one from the menu!")
    else:
        # enumerate() gives us both the index (ID) and the value (task)
        for index, item in enumerate(my_tasks, start=1):
            status = "✔" if item["done"] else " "
            print(f"[{status}] {index}. {item['task']}")
    print("-----------------------")


def remove_task(my_tasks):
    """Removes a task from the list by its displayed number."""
    if not my_tasks:
        print("⚠ No tasks to remove.")
        return
    view_tasks(my_tasks)
    try:
        choice = int(input("Enter the task number to remove: "))
        if 1 <= choice <= len(my_tasks):
            removed = my_tasks.pop(choice - 1)
            print(f"🗑 Removed: '{removed['task']}'")
        else:
            print("⚠ Invalid task number.")
    except ValueError:
        print("⚠ Please enter a valid number.")


def mark_complete(my_tasks):
    """Marks a task as completed."""
    if not my_tasks:
        print("⚠ No tasks to update.")
        return
    view_tasks(my_tasks)
    try:
        choice = int(input("Enter the task number to mark as complete: "))
        if 1 <= choice <= len(my_tasks):
            my_tasks[choice - 1]["done"] = True
            print(f"✔ Marked as complete: '{my_tasks[choice - 1]['task']}'")
        else:
            print("⚠ Invalid task number.")
    except ValueError:
        print("⚠ Please enter a valid number.")


def main():
    """Main program loop — the entry point of the application."""
    my_tasks = []  # This list is our in-memory storage (the 'database')
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_task(my_tasks)
        elif choice == "2":
            view_tasks(my_tasks)
        elif choice == "3":
            remove_task(my_tasks)
        elif choice == "4":
            mark_complete(my_tasks)
        elif choice == "5":
            print("👋 Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
