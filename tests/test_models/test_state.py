#!/usr/bin/python3
'''
This is the 'test_state' module.
'''
import unittest
from datetime import datetime
from models import *


class Test_StateModel(unittest.TestCase):
    """
    Test the state model class
    """

    def setUp(self):
        '''set up objects for testing
        '''
        self.test_model1 = State()
        self.test_model2 = State()

    def test_var_initialization(self):
        '''test for proper initialization
        '''
        self.assertTrue(hasattr(self.test_model1, "name"))
        self.assertFalse(hasattr(self.test_model1, "first_name"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)
        self.assertEqual(self.test_model1.name, "")
        m1c = self.test_model1.created_at
        m2c = self.test_model2.created_at
        self.assertTrue(m1c != m2c)
        self.assertTrue(type(m1c) is datetime)

    def test_types(self):
        """testing types of class attributes
        """
        self.assertTrue(type(self.test_model1.name) is str)

    def test_save(self):
        """testing save attribute
        """
        m1c = self.test_model1.created_at
        self.test_model1.save()
        m1c_saved = self.test_model1.created_at
        self.assertTrue(m1c == m1c_saved)

if __name__ == "__main__":
    unittest.main()
