import unittest

from src.repository.module import Module


class ModuleTest(unittest.TestCase):
    """
    A class that handles the testing of the Module class
    """
    def test_class(self):
        module = Module()
        module[1] = 1
        self.assertEqual(module, {1: 1})

        module[2] = 1
        self.assertEqual(module, {1: 1, 2: 1})

        module[0] = 0
        self.assertEqual(module, {1: 1, 2: 1, 0: 0})

        module[1] = 2
        self.assertEqual(module, {1: 2, 2: 1, 0: 0})

        del module[1]
        self.assertEqual(module, {2: 1, 0: 0})

        self.assertEqual(module(), {2: 1, 0: 0})

        with self.assertRaises(KeyError):
            x = module[1]

        self.assertEqual(len(module), 2)
        iterator = iter(module)

        self.assertEqual(next(iterator), 1)
        self.assertEqual(next(iterator), 0)
        with self.assertRaises(StopIteration):
            x = next(iterator)

        list = [5, 3, 1, 4, 2, 0]

        sortedList = Module.sort(list, lambda x, y: x >= y)
        self.assertEqual(sortedList, [0, 1, 2, 3, 4, 5])

        sortedList = Module.sort(list, lambda x, y: x < y)
        self.assertEqual(sortedList, [5, 4, 3, 2, 1, 0])

        filteredList = Module.filter(list, lambda x: x % 2 == 0)
        self.assertEqual(filteredList, [4, 2, 0])

        filteredList = Module.filter(list, lambda x: x > 3)
        self.assertEqual(filteredList, [5, 4])
