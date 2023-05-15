# Create an empty to-do list
todo_list = []

# Function to add a task to the to-do list
def add_task():
    task = input("Enter a task to add: ")
    todo_list.append(task)
    print("Task added successfully!")

# Function to remove a task from the to-do list
def remove_task():
    task = input("Enter the task to remove: ")
    if task in todo_list:
        todo_list.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found in the to-do list.")

# Function to display the current to-do list
def display_list():
    if todo_list:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    else:
        print("To-Do List is empty.")

# Main program loop
while True:
    print("\n----- Menu -----")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display the to-do list")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        display_list()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
