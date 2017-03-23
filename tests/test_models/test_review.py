#!/usr/bin/python3
'''
This is the 'test_review' module.
'''
import unittest
from datetime import datetime
from models import *
from models.review import Review

class Test_ReviewModel(unittest.TestCase):
    """
    Test the review model class
    """

    def setUp(self):
        '''set up objects for testing
        '''
        self.test_model1 = Review()
        self.test_model2 = Review()

    def test_var_initialization(self):
        '''test for proper initiailization
        '''
        self.assertTrue(hasattr(self.test_model1, "place_id"))
        self.assertTrue(hasattr(self.test_model1, "user_id"))
        self.assertTrue(hasattr(self.test_model1, "text"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)
        self.assertEqual(self.test_model1.place_id, "")
        self.assertEqual(self.test_model1.user_id, "")
        self.assertEqual(self.test_model1.text, "")
        m1c = self.test_model1.place_id
        m2c = self.test_model2.place_id
        self.assertTrue(m1c == m2c)
        self.assertTrue(type(m1c) is str)

    def test_types(self):
        """test for proper types of instance attributes
        """
        self.assertTrue(type(self.test_model1.place_id) is str)
        self.assertTrue(type(self.test_model1.user_id) is str)
        self.assertTrue(type(self.test_model1.text) is str)

    def test_save(self):
        """tests the save attribute
        """
        m1c = self.test_model1.created_at
        self.test_model1.save()
        m1c_saved = self.test_model1.created_at
        self.assertTrue(m1c == m1c_saved)

if __name__ == "__main__":
    unittest.main()
