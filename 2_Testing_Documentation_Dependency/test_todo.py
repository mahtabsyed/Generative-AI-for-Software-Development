import unittest
from todo import TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = TodoList()

    def test_add_todo(self):
        self.todo_list.add('Buy groceries')
        self.assertIn('Buy groceries', self.todo_list.list_todos())

    def test_add_empty_todo(self):
        self.todo_list.add('')
        self.assertNotIn('', self.todo_list.list_todos())

    def test_list_todos(self):
        self.todo_list.add('Buy groceries')
        self.todo_list.add('Read a book')
        todos = self.todo_list.list_todos()
        self.assertEqual(todos, ['Buy groceries', 'Read a book'])

    def test_delete_todo_valid_index(self):
        self.todo_list.add('Buy groceries')
        self.todo_list.add('Read a book')
        self.todo_list.delete(0)
        self.assertNotIn('Buy groceries', self.todo_list.list_todos())
        self.assertIn('Read a book', self.todo_list.list_todos())

    def test_delete_todo_invalid_index(self):
        self.todo_list.add('Buy groceries')
        self.todo_list.delete(5)
        self.assertIn('Buy groceries', self.todo_list.list_todos())

if __name__ == '__main__':
    unittest.main()