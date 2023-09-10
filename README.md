# Daily Task Manager

The Daily Task Manager is a simple Python program that allows you to manage your daily tasks. You can add tasks, mark them as completed, view all tasks, check the completion percentage, and delete tasks. This README file provides instructions on how to use the program and an overview of its functions.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Contributing](#contributing)
- [License](#license)

## Installation

Before using the Daily Task Manager, make sure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

1. Clone this repository or download the `daily_task_manager.py` file to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the `daily_task_manager.py` file is located.

3. Run the program by executing the following command:

   ```
   python daily_task_manager.py
   ```

## Usage

Once you have the program running, you can interact with it using the following options:

1. **Add Task:** Enter '1' to add a new task. You will be prompted to enter the task's description.

2. **Mark Task as Completed:** Enter '2' to mark a task as completed. You will need to provide the task's ID.

3. **View All Tasks:** Enter '3' to view all tasks, including their status (completed or not).

4. **View Completion Percentage:** Enter '4' to see the completion percentage of your tasks.

5. **Delete Task:** Enter '5' to delete a task by specifying its ID.

6. **Quit:** Enter '6' to exit the program.

## Functions

Here is an overview of the functions in the `daily_task_manager.py` file:

- `initialize_database()`: Initializes the SQLite database for storing tasks.

- `add_task(task_text)`: Adds a new task to the database with the provided task description.

- `complete_task(task_id)`: Marks a task as completed by updating its status in the database.

- `view_all_tasks()`: Retrieves and displays all tasks from the database.

- `get_completion_percentage()`: Calculates and returns the percentage of completed tasks.

- `delete_task(task_id)`: Deletes a task from the database based on its ID.

The main program loop allows you to interact with these functions through a text-based menu.

## Contributing

If you want to contribute to the Daily Task Manager, feel free to fork this repository, make your changes, and submit a pull request. We welcome any improvements or feature additions that can enhance the program's functionality.
