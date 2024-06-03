import unittest
from stack import Stack
from my_stack import MyStack


class TestStack(unittest.TestCase):

    def test_push(self):
        stack = Stack([])
        stack.push(1)
        self.assertEqual(len(stack), 1)
        stack.push(2)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.elements, [1, 2])

    def test_pop(self):
        stack = Stack([])
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(len(stack), 0)

    def test_pop_empty(self):
        stack = Stack([])
        with self.assertRaises(IndexError):
            stack.pop()

    def test_len(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)
        stack.push(1)
        self.assertEqual(len(stack), 1)
        stack.pop()
        self.assertEqual(len(stack), 0)

    def test_multiple_instances(self):
        stack1 = Stack()
        stack2 = Stack()
        stack1.push(1)
        self.assertEqual(len(stack1), 1)
        self.assertNotEqual(len(stack2), 0)
        stack2.push(2)
        self.assertEqual(len(stack1), 2)
        self.assertEqual(len(stack2), 2)


class TestMyStack(unittest.TestCase):

    def test_push(self):
        stack = MyStack()
        stack.push(1)
        self.assertEqual(len(stack), 1)
        stack.push(2)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.elements, [1, 2])

    def test_pop(self):
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(len(stack), 0)

    def test_pop_empty(self):
        stack = MyStack()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_len(self):
        stack = MyStack()
        self.assertEqual(len(stack), 0)
        stack.push(1)
        self.assertEqual(len(stack), 1)
        stack.pop()
        self.assertEqual(len(stack), 0)

    def test_multiple_instances(self):
        stack1 = MyStack()
        stack2 = MyStack()
        stack1.push(1)
        self.assertEqual(len(stack1), 1)
        self.assertEqual(len(stack2), 0)
        stack2.push(2)
        self.assertEqual(len(stack1), 1)
        self.assertEqual(len(stack2), 1)


if __name__ == '__main__':
    unittest.main()
