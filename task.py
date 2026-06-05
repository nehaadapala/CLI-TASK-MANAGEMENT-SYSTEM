class Task:

    # Constructor to initialize a task
    def __init__(self, task_id, title, completed=False):
        self.task_id = task_id
        self.title = title
        self.completed = completed

    # Convert Task object into dictionary
    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "completed": self.completed
        }

    # Create Task object from dictionary
    @staticmethod
    def from_dict(data):
        return Task(
            data["task_id"],
            data["title"],
            data["completed"]
        )