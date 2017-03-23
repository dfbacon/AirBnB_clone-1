#!/usr/bin/python3
'''
This is the 'test_city' module.
'''
import unittest
from datetime import datetime
from models import *
from models.city import City


class Test_CityModel(unittest.TestCase):
    """
    Test the city model class
    """

    def setUp(self):
        """sets up objects for testing later
        """
        self.test_model1 = City()
        self.test_model2 = City()

    def test_basic_setup(self):
        """test for init of class attributes
        """
        self.assertTrue(hasattr(self.test_model1, "state_id"))
        self.assertTrue(hasattr(self.test_model1, "name"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)

    def test_types(self):
        """testing for proper typing of city attributes
        """
        self.assertTrue(type(self.test_model1.state_id) is str)
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
