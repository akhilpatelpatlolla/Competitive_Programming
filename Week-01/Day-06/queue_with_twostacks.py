import unittest


class QueueTwoStacks(object):

    def __init__(self):
        self.inStack=[]
        self.outStack=[]

    def enqueue(self, item):
        while(self.inStack!=[]):
            self.outStack.append(self.inStack.pop())
        self.inStack.append(item)
        while(self.outStack!=[]):
            self.inStack.append(self.outStack.pop())

    def dequeue(self):
        if(self.inStack==[]):
            raise Exception
        else:
            return self.inStack.pop()


















# Tests

class Test(unittest.TestCase):

    def test_queue_usage(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)