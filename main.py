from task_manager import TaskManager


def display_tasks(manager):
    """
    Display all tasks with their status.
    """

    if not manager.tasks:
        print("\nNo tasks available.\n")
        return

    print("\n------ TASK LIST ------")

    for task in manager.tasks:

        status = "Completed" if task.completed else "Pending"

        print(
            f"ID: {task.task_id} | "
            f"Task: {task.title} | "
            f"Status: {status}"
        )

    print("-----------------------\n")


def main():

    # Create TaskManager object
    manager = TaskManager()

    while True:

        print("\n===== TASK MANAGEMENT SYSTEM =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        # Add Task
        if choice == "1":

            title = input("Enter task title: ")

            if title.strip() == "":
                print("Task title cannot be empty.")
                continue

            manager.add_task(title)

            print("Task added successfully!")

        # View Tasks
        elif choice == "2":

            display_tasks(manager)

        # Complete Task
        elif choice == "3":

            try:
                task_id = int(
                    input("Enter task ID to complete: ")
                )

                manager.complete_task(task_id)

                print("Task marked as completed!")

            except ValueError:

                print("Please enter a valid number.")

        # Delete Task
        elif choice == "4":

            try:
                task_id = int(
                    input("Enter task ID to delete: ")
                )

                manager.delete_task(task_id)

                print("Task deleted successfully!")

            except ValueError:

                print("Please enter a valid number.")

        # Exit
        elif choice == "5":

            print("Thank you for using Task Manager!")
            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()