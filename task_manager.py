from task import Task
from storage import load_tasks, save_tasks


class TaskManager:

    # Constructor
    # Loads existing tasks from JSON file
    def __init__(self):

        self.tasks = [
            Task.from_dict(task)
            for task in load_tasks()
        ]

    # Save all tasks into JSON file
    def save(self):

        save_tasks(
            [task.to_dict() for task in self.tasks]
        )

    # Add a new task
    def add_task(self, title):

        # Generate next task id
        task_id = (
            max(
                [task.task_id for task in self.tasks],
                default=0
            )
            + 1
        )

        # Create Task object
        new_task = Task(task_id, title)

        # Add task to list
        self.tasks.append(new_task)

        # Save changes
        self.save()

    # Mark task as completed
    def complete_task(self, task_id):

        for task in self.tasks:

            if task.task_id == task_id:

                task.completed = True

                self.save()

                return

    # Delete task
    def delete_task(self, task_id):

        self.tasks = [
            task
            for task in self.tasks
            if task.task_id != task_id
        ]

        self.save()