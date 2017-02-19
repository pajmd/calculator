import unittest


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = ['9', '24', '7', '3', '-', '/', '+']
        self.expected_stack = ['9', '24', '7', '3', '-', '/', '+']

    def test_pop_all_items(self):
        first = True
        while len(self.stack) != 0:
            popped = self.stack.pop()
            if first is True:
                first_popped = popped
                first = False
        self.assertEqual('+', first_popped)
        self.assertEqual('9', popped)
        self.assertEqual(0, len(self.stack))