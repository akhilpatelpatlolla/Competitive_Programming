import unittest


def find_duplicate(int_list):

    # Find a number that appears more than once ... in O(n) time
    size=len(int_list)
    for i in range(0, size):
         
        if int_list[abs(int_list[i])] >= 0:
            int_list[abs(int_list[i])] = -int_list[abs(int_list[i])]
        else:
            k=abs(int_list[i])

    return k


















# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_duplicate([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_duplicate([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_duplicate([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_duplicate([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)