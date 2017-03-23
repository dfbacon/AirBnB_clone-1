#!/usr/bin/python3
'''
This is the 'test_amenity' module.
'''
import unittest
from datetime import datetime
from models import *


class Test_AmenityModel(unittest.TestCase):
    """
    Test the amenity model class
    """

    def setUp(self):
        """sets up objects for testing later
        """
        self.test_model1 = Amenity()
        self.test_model2 = Amenity()

    def test_basic_setup(self):
        """test for amenity class attributes
        """
        self.assertTrue(hasattr(self.test_model1, "name"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)
        m1c = self.test_model1.created_at
        m2c = self.test_model2.created_at
        self.assertTrue(m1c != m2c)
        self.assertTrue(type(m1c) is datetime)

    def test_types(self):
        """testing for proper typing of attributes
        """
        self.assertTrue(type(self.test_model1.name) is str)

    def test_save(self):
        """tests the save attribute
        """
        m1c = self.test_model1.created_at
        self.test_model1.save()
        m1c_saved = self.test_model1.created_at
        self.assertFalse(m1c != m1c_saved)


if __name__ == "__main__":
    unittest.main()
