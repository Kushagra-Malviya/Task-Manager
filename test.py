import sqlite3

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect("daily_tasks.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            task_text TEXT,
            completed BOOLEAN
        )
    """)
    conn.commit()
    conn.close()

# Function to add a task
def add_task(task_text):
    conn = sqlite3.connect("daily_tasks.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task_text, completed) VALUES (?, 0)", (task_text,))
    conn.commit()
    conn.close()

# Function to mark a task as completed
def complete_task(task_id):
    conn = sqlite3.connect("daily_tasks.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# Function to view all tasks
def view_all_tasks():
    conn = sqlite3.connect("daily_tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# Function to calculate the percentage of completed tasks
def get_completion_percentage():
    conn = sqlite3.connect("daily_tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM tasks")
    total_tasks = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM tasks WHERE completed = 1")
    completed_tasks = cursor.fetchone()[0]
    conn.close()

    if total_tasks == 0:
        return 0.0
    else:
        return (completed_tasks / total_tasks) * 100.0

# Function to delete a task
def delete_task(task_id):
    conn = sqlite3.connect("daily_tasks.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# Main program loop
if __name__ == "__main__":
    initialize_database()

    while True:
        print("\nDaily Task Manager")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View All Tasks")
        print("4. View Completion Percentage")
        print("5. Delete Task")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_text = input("Enter the task: ")
            add_task(task_text)
            print("Task added successfully!")

        elif choice == "2":
            task_id = int(input("Enter the task ID to mark as completed: "))
            complete_task(task_id)
            print("Task marked as completed!")

        elif choice == "3":
            tasks = view_all_tasks()
            for task in tasks:
                print(f"{task[0]}. {task[1]} {'(Completed)' if task[2] else ''}")

        elif choice == "4":
            percentage = get_completion_percentage()
            print(f"Completion Percentage: {percentage:.2f}%")

        elif choice == "5":
            task_id = int(input("Enter the task ID to delete: "))
            delete_task(task_id)
            print("Task deleted successfully!")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
