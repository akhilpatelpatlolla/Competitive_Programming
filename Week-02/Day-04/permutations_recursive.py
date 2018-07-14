import unittest

def get_permutations(string):
    # Base case
    if len(string) <= 1:
        return set([string])

    except_last_char = string[:-1]
    last_char = string[-1]

    # Recursive call: get all possible permutations for all chars except last
    permutations_of_except_last_char = get_permutations(except_last_char)

    # Put the last char in all possible positions for each of
    # the above permutations
    permutations = set()
    for permutation_of_except_last_char in permutations_of_except_last_char:
        for position in range(len(except_last_char) + 1):
            permutation = (
                permutation_of_except_last_char[:position]
                + last_char
                + permutation_of_except_last_char[position:]
            )
            permutations.add(permutation)

    return permutations















# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)