tasks = []

def add_task(task):
    if not task:
      raise ValueError("Task cannot be empty.")
    else:
      tasks.append(task)
    return tasks

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        return tasks
    else:
        return "Task not found."

def list_tasks():
    return tasks

def clear_tasks():
    tasks.clear()
    print(tasks)
    return "Tasks cleared."

# Prompt: You are an expert in pytest for automated testing of Python code. Please amend this code with a comprehensive set of tests in pytest to find bugs or other issues in the code.

# How to use pytest?
# 1. Install pytest
# 2. Create the main python code and then create a test file with the same name but with the prefix test_.
# Navigate to the directory containing your test file and run pytest from the command line. pytest will automatically discover and run your test functions, providing a summary of the test results.
# Or run for a specific test file: pytest test_tasks3.py



