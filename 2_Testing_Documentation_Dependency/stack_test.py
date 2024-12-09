import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.items, [1])

    def test_pop(self):
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), None)

    def test_peek(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), None)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 0)


if __name__ == "__main__":
    unittest.main()
