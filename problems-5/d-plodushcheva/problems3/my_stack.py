import unittest


class Stack:
    def __init__(self, elements=None):
        if elements is None:
            self.elements = []
        else:
            self.elements = elements

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        if not self.is_empty():
            return self.elements.pop()
        else:
            raise IndexError("Cannot pop from an empty stack")

    def is_empty(self):
        return len(self.elements) == 0

    def peek(self):
        if not self.is_empty():
            return self.elements[-1]
        else:
            raise IndexError("Cannot peek on an empty stack")

    def __len__(self):
        return len(self.elements)


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

    def test_peek(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.peek(), 3)
        self.assertEqual(len(stack), 3)

    def test_peek_empty_stack(self):
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

        stack.push(1)
        self.assertFalse(stack.is_empty())


if __name__ == "__main__":
    unittest.main()
