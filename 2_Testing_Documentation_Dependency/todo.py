# todo.py
# As an Experienced Software Engineer can you write Python code for a TODO list implementation with functions add, list and delete TODOs. You can use a list to implement the TODO. And make the code threadsafe.

import threading
import unittest

class TodoList:
    def __init__(self):
        self.todos = []
        self.lock = threading.Lock()

    def add(self, todo):
        with self.lock:
            if (todo != ""):
                self.todos.append(todo)
                print(f'TODO added: {todo}')
            
    def list_todos(self):
        with self.lock:
            print('Current TODOs:')
            for idx, todo in enumerate(self.todos, 1):
                print(f'{idx}. {todo}')
            return list(self.todos)  # Return a copy of the list

    def delete(self, index):
        with self.lock:
            if 0 <= index < len(self.todos):
                removed_todo = self.todos.pop(index)
                print(f'TODO removed: {removed_todo}')
            else:
                print('Invalid index. No TODO removed.')

# Example usage
if __name__ == '__main__':
    todo_list = TodoList()

    print("Beginning of the program")
    # Adding TODOs
    todo_list.add('Buy groceries')
    todo_list.add("") # Empty TODO
    todo_list.add('Read a book')
    todo_list.add('Book movie tickets')

    # Listing TODOs
    todo_list.list_todos()

    # Deleting a TODO
    todo_list.delete(0)

    # Listing TODOs again
    todo_list.list_todos()
    print("End of the program")
    print("***\n")

# Prompt: As an expert software tester, write code that converts the output of the exploratory testing above into functional testing using the unittest module in Python


