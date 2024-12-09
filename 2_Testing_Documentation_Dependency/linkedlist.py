"""
Exercise 4 - Buggy linked List
In this exercise, a Node and a Doubly Linked List class is provided. You must find the bug in one method of Doubly Linked List class and fix it. The Node class is fixed and you must not edit it.

Instructions: The fixed class must have every method that the buggy class has, but with the bug fixed.

Constraints: No library can be imported.

Hints:
You may ask an LLM to explain the classes for you.
You may also ask an LLM to make some example cases for you.
"""

# I have a Doubly Linked List class implementation that has a bug in one mothod. Can you help me fix it? Check the instructions, Constraints and Hints for more details.


## Do NOT modify this class.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return new_node

    def link_nodes(self, node1, node2):
        if node1 is not None and node2 is not None:
            node1.next = node2
            node2.prev = node1

    def traverse(self):
        visited = []
        current = self.head
        seen_nodes = set()
        while current:
            if current in seen_nodes:
                break
            visited.append(current)
            seen_nodes.add(current)
            current = current.next
        return visited
