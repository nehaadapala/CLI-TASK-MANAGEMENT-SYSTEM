import json
import os

# JSON file used to store tasks
FILE_NAME = "tasks.json"


# Load tasks from JSON file
def load_tasks():

    # If file does not exist, return empty list
    if not os.path.exists(FILE_NAME):
        return []

    # Read data from JSON file
    with open(FILE_NAME, "r") as file:
        return json.load(file)


# Save tasks into JSON file
def save_tasks(tasks):

    # Write data into JSON file
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)