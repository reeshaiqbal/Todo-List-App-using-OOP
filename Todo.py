class TodoList:  # I created a class and enclosed "data" and "methods" in it implementing encapsulation
    def __init__(self):
        self.tasks = []

    def add_task(self):
        add = input("Write your task here: ")
        self.tasks.append([add, False])
        print("Task Added Successfully!")

    def view_task(self):
        if len(self.tasks) == 0:
            print("No Task available yet")
        else:
            for i in range(len(self.tasks)):
                if self.tasks[i][1] == True:
                    status = "Done"
                else:
                    status = "Pending"
                print(i+1, self.tasks[i][0], status)

    def mark_as_done(self):
        number = int(input("Enter the Task number: "))
        if 1 <= number <= len(self.tasks):
            self.tasks[number - 1][1] = True
            print("Task marked as done")
        else:
            print("Invalid task number")

    def delete_task(self):
        number = int(input("Enter the Task you want to delete: "))
        if 1 <= number <= len(self.tasks):
            self.tasks.pop(number-1)
            print("Task Deleted Successfully")
        else:
            print("Invalid task number")

    def search_task(self):
        word = input("Enter the word you want to search: ")
        found = False
        for i in range(len(self.tasks)):
            if word.lower() in self.tasks[i][0].lower():
                if self.tasks[i][1] == True:
                    status = "Done"
                else:
                    status = "Pending"
                print(i+1, self.tasks[i][0], status)
                found = True
        if found == False:
            print("Desired Task not found")

    def update_task(self):
        number = int(input("Enter the task you want to update: "))
        if 1 <= number <= len(self.tasks):
            new_text = input("Enter the new text here: ")
            self.tasks[number-1][0] = new_text
            print("Task Updated Successfully!")


todo = TodoList()  # Object of the class is created

while True:  # Loop will be repeated and menu will be shown again and again until the loop breaks
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Update Task")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
        todo.add_task()

    elif choice == "2":
        todo.view_task()

    elif choice == "3":
        todo.mark_as_done()

    elif choice == "4":
        todo.delete_task()

    elif choice == "5":
        todo.search_task()

    elif choice == "6":
        todo.update_task()

    elif choice == "7":
        print("Program Ended")
        break

    else:
        print("Invalid choice")
