import unittest
from _collections_abc import Iterable

from app import DevOps

newDevops = DevOps()

class Tester(unittest.TestCase):

    def test(self): 
        self.assertIsInstance(newDevops.display_names(), Iterable) #testing whether listNames is Iterable
        self.assertEqual(newDevops.counter(), len(newDevops.display_names()))