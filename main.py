#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is, ", now)
while True:
    # Get user input and strip space chars from it
    user_action = input("Type add or show, edit, complete or exit: ")
    user_action = user_action.strip()

    #match user_action:

        #case 'add' in user_action:
    #if 'add' in user_action or 'new' in user_action:
    if user_action.startswith("add"):

        # todo = input("Enter a todo: ") + "\n"
       # file = open('todos.txt', 'r')
       # todos = file.readlines()
       # file.close()
        todo = user_action[4:]
       # with open('todos.txt', 'r') as file:
       #     todos = file.readlines()
        #todos = get_todos("todos.txt")
        todos = functions.get_todos()
        todos.append(todo + '\n')

        #file = open('todos.txt', 'w')
        #file.writelines(todos)
        #file.close()

        #with open('todos.txt', 'w') as file:
         #   file.writelines(todos)
        #write_todos("todos.txt", todos)
        functions.write_todos(todos)

   # case 'show':
        #file = open('todos.txt', 'r')
        #todos = file.readlines()
        #file.close()
    #elif 'show' in user_action:
    elif user_action.startswith("show"):
        #todos = get_todos("todos.txt")
        todos = functions.get_todos()
        #with open('todos.txt', 'r') as file:
            #todos = file.readlines()

        # new_todos = [item.strip('\n' for item in todos]

        for index, item in enumerate(todos):
            item = item.title()
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
   # case 'edit':
    #elif 'edit' in user_action:
    elif user_action.startswith("edit"):
        #number = int(input("Number of the todo to edit: "))
        try:

            number = int(user_action[5:])
            number = number - 1

            #with open('todos.txt', 'r') as file:
             #   todos = file.readlines()
            #todos = get_todos("todos.txt")
            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            #with open('todos.txt', 'w') as file:
            #    file.writelines(todos)
            #write_todos("todos.txt", todos)
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    #case 'complete':
    #elif 'complete' in user_action:
    elif user_action.startswith("complete"):
        try:
            #number = int(input("Number of the todo to complete: "))
            number = int(user_action[9:])
            #todos = get_todos("todos.txt")
            todos = functions.get_todos()

            #with open('todos.txt', 'r') as file:
               # todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            #with open('todos.txt', 'w') as file:
            #    file.writelines(todos)
            #write_todos("todos.txt", todos)
            functions.write_todos(todos)

            message = f"Todo {todo_to_remove.strip('\n')} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    #case 'exit':
    #elif 'exit' in user_action:
    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")

print("Bye!")

