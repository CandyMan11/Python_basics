import os

#function to get filename
def get_filename(file_name, extension=".txt"):
    if file_name.endswith(".txt") or file_name.endswith(".json"):
        return file_name
    else:
        return file_name + extension

#function to add a task
def add_task(task, file_name):
    with open(file_name, 'a') as file:
        file.write(task + "\n")

    print("Task added.")

#function to view tasks
def view_task(file_name):
    try:
        with open(file_name, "r") as file:
            tasks = file.readlines()

            if not tasks:
                print("No tasks found.")
                return

            print(f"Tasks in {file_name}:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")

    except FileNotFoundError:
        print("Error: File does not exist.")

#function to remove a task
def delete_task(filename, index):
    try:
        with open(filename, "r") as file:
            tasks = file.readlines()

        if (index < 1) or (index > len(tasks)):
            print("Invalid task number.")
            return
        
        removed_task = tasks.pop(index - 1)
        with open(filename, "w") as file:
            file.writelines(tasks)

        print(f"Deleted task: {removed_task.strip()}")
    
    except FileNotFoundError:
        print("Error: File does not exist.")

def main():
    file = input("Enter file name: ")
    file = get_filename(file)

    while True:
        print("\nChoose an action:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            task = input("Enter task -\n")
            add_task(task, file)

        elif choice == "2":
            view_task(file)

        elif choice == "3":
            index = int(input("Enter the index to be deleted: "))
            delete_task(file, index)

        elif choice == "4":
            print("Exiting the To-do manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()