import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def test_default_stack(self):
        stack1 = Stack()
        stack1.push(1)
        self.assertEqual(len(stack1), 1)

    def test_push_and_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(len(stack), 0)

    def test_two_stacks(self):
        stack1 = Stack()
        stack2 = Stack()
        stack1.push(1)
        self.assertEqual(len(stack1), 1)
        self.assertEqual(len(stack2), 0)

    def test_pop_empty_stack(self):
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()


if __name__ == "__main__":
    unittest.main()
