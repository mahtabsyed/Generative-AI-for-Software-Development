"""
Exercise 3 - Debugging a Stack Implementation
In this exercise, you are provided with a stack implementation that harbors an inconsistency. Your task is to pinpoint and rectify this inconsistency. It's crucial that this stack functions similarly to a Python list. Therefore, if there is a method common to both the stack and a Python list, they should operate identically. This information is key to identifying the inconsistency.

Instructions: Ensure that the corrected class includes all the methods found in the original, buggy class, with the inconsistency addressed.

Constraints: You are not allowed to import any libraries.

Hints: Consider asking an LLM for a detailed explanation of how this stack functions and the intended purpose of its methods.You might also request example cases from an LLM to better understand and test the functionality of the stack.
"""

# I have a stack implementation that has an inconsistency. Can you help me fix it? Check the instructions, Constraints and Hints for more details.

# As a Senior Test Engineer can you write Test Cases using Python unittest module to check all edge cases of this Stack implementataion which has an inconsistency.


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
