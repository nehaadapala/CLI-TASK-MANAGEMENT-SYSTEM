# Task Management System

## Project Overview

The Task Management System is a Python-based command-line application that helps users manage their daily tasks efficiently. The application allows users to add, view, complete, and delete tasks. Task data is stored permanently in a JSON file, ensuring that tasks remain available even after the application is closed.

## Features

* Add new tasks
* View all tasks with their current status
* Mark tasks as completed
* Delete tasks
* Automatic saving of tasks to a JSON file
* Automatic loading of tasks when the application starts

## Project Structure

```text
TaskManagementSystem/
│
├── main.py
├── task.py
├── task_manager.py
├── storage.py
└── tasks.json
```

### File Description

#### main.py

Contains the command-line interface and handles user interactions.

#### task.py

Defines the Task class, which represents a task with:

* Task ID
* Task Title
* Completion Status

#### task_manager.py

Contains the business logic for:

* Adding tasks
* Completing tasks
* Deleting tasks
* Saving task updates

#### storage.py

Handles reading and writing task data to the JSON file.

#### tasks.json

Stores task information persistently.

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* JSON
* File Handling

## Concepts Implemented

* Classes and Objects
* Constructors (`__init__`)
* Instance Methods
* Static Methods
* Encapsulation
* List Comprehensions
* JSON Serialization and Deserialization
* Modular Programming
* Exception Handling
* File Handling

## How to Run the Project

1. Open the terminal.
2. Navigate to the project folder.

```bash
cd TaskManagementSystem
```

3. Run the application.

```bash
python main.py
```

## Sample Menu

```text
===== TASK MANAGEMENT SYSTEM =====
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit
```

## Future Enhancements

* Graphical User Interface (GUI) using Tkinter or CustomTkinter
* Task priorities
* Due dates and reminders
* Search and filter functionality
* Task categories


## Conclusion

This project demonstrates the use of Python fundamentals, object-oriented programming, JSON data storage, file handling, and modular application design through a real-world Task Management System.
