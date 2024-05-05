import unittest
from stack import Stack
from valid_stack import ValidStack


class TestStack(unittest.TestCase):
    def test_push_and_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(len(stack), 0)

    def test_push_and_pop_diff_objects(self):
        stack = Stack()
        stack.push([1, 2, 3])
        stack.push((1, 2, 3))
        stack.push({"a": 2, 3: [1, 2, 3]})
        stack.push(1)
        stack.push("hello")
        self.assertEqual(stack.pop(), "hello")
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), {"a": 2, 3: [1, 2, 3]})
        self.assertEqual(stack.pop(), (1, 2, 3))
        self.assertEqual(stack.pop(), [1, 2, 3])

    def test_pop_from_empty_stack(self):
        stack = Stack()
        self.assertRaises(IndexError, stack.pop)

    def test_two_empty_stacks(self):
        stack_1 = Stack()
        stack_2 = Stack()
        stack_1.push(1)
        self.assertGreater(len(stack_1), len(stack_2))
        
    def test_two_stacks_with_list(self):
        l = [1, 2, 3]
        stack_1 = Stack(l)
        l.append(4)
        stack_2 = Stack(l)
        self.assertLess(len(stack_1), len(stack_2))

    def test_two_stacks_with_tuple(self):
        l = (1, 2, 3)
        stack_1 = Stack(l)
        l += (4, )
        stack_2 = Stack(l)
        self.assertLess(len(stack_1), len(stack_2))


class TestValidStack(unittest.TestCase):
    def test_push_and_pop(self):
        stack = ValidStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(len(stack), 0)

    def test_push_and_pop_diff_objects(self):
        stack = ValidStack()
        stack.push([1, 2, 3])
        stack.push((1, 2, 3))
        stack.push({"a": 2, 3: [1, 2, 3]})
        stack.push(1)
        stack.push("hello")
        self.assertEqual(stack.pop(), "hello")
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), {"a": 2, 3: [1, 2, 3]})
        self.assertEqual(stack.pop(), (1, 2, 3))
        self.assertEqual(stack.pop(), [1, 2, 3])

    def test_pop_from_empty_stack(self):
        stack = ValidStack()
        self.assertRaises(IndexError, stack.pop)

    def test_two_empty_stacks(self):
        stack_1 = ValidStack()
        stack_2 = ValidStack()
        stack_1.push(1)
        self.assertGreater(len(stack_1), len(stack_2))
        
    def test_two_stacks_with_list(self):
        l = [1, 2, 3]
        stack_1 = ValidStack(l)
        l.append(4)
        stack_2 = ValidStack(l)
        self.assertLess(len(stack_1), len(stack_2))

    def test_two_stacks_with_tuple(self):
        l = (1, 2, 3)
        stack_1 = ValidStack(l)
        l += (4, )
        stack_2 = ValidStack(l)
        self.assertLess(len(stack_1), len(stack_2))


if __name__ == "__main__":
    unittest.main(verbosity=3)
