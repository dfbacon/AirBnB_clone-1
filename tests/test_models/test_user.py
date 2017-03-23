#!/usr/bin/python3
'''
This is the 'test_user' module.
'''
import unittest
from datetime import datetime
from models import *
from models.user import User


class Test_UserModel(unittest.TestCase):
    """
    Test the user model class
    """

    def setUp(self):
        '''set up objects for testing
        '''
        self.test_model1 = User()
        self.test_model2 = User()

    def test_var_initialization(self):
        '''test for proper initialization
        '''
        self.assertTrue(hasattr(self.test_model1, "email"))
        self.assertTrue(hasattr(self.test_model1, "password"))
        self.assertTrue(hasattr(self.test_model1, "first_name"))
        self.assertTrue(hasattr(self.test_model1, "last_name"))
        self.assertEqual(self.test_model1.email, "")
        self.assertEqual(self.test_model1.password, "")
        self.assertEqual(self.test_model1.first_name, "")
        self.assertEqual(self.test_model1.last_name, "")
        self.assertTrue(self.test_model1.id != self.test_model2.id)
        m1c = self.test_model1.created_at
        m2c = self.test_model2.created_at
        self.assertTrue(m1c != m2c)

    def test_types(self):
        """checking proper types for user class attributes
        """
        self.assertTrue(type(self.test_model1.last_name) is str)
        self.assertTrue(type(self.test_model1.first_name) is str)
        self.assertTrue(type(self.test_model1.email) is str)
        self.assertTrue(type(self.test_model1.password) is str)

    def test_save(self):
        """testing save attribute
        """
        m1c = self.test_model1.created_at
        self.test_model1.save()
        m1c_saved = self.test_model1.created_at
        self.assertTrue(m1c == m1c_saved)

if __name__ == "__main__":
    unittest.main()
