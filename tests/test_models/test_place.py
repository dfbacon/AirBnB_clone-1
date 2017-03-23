#!/usr/bin/python3
'''
This is the 'test_place' module.
'''
import unittest
from datetime import datetime
from models import *


class Test_PlaceModel(unittest.TestCase):
    """
    Test the place model class
    """

    def setUp(self):
        '''set up objects for testing
        '''
        self.model = Place()
        self.model.save()

    def test_var_initialization(self):
        '''test for proper initialization
        '''
        self.assertTrue(hasattr(self.model, "city_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "description"))
        self.assertTrue(hasattr(self.model, "number_rooms"))
        self.assertTrue(hasattr(self.model, "number_bathrooms"))
        self.assertTrue(hasattr(self.model, "max_guest"))
        self.assertTrue(hasattr(self.model, "price_by_night"))
        self.assertTrue(hasattr(self.model, "latitude"))
        self.assertTrue(hasattr(self.model, "longitude"))
        self.assertTrue(hasattr(self.model, "amenities"))
        self.assertEqual(self.model.city_id, "")
        self.assertEqual(self.model.user_id, "")
        self.assertEqual(self.model.name, "")
        self.assertEqual(self.model.description, "")
        self.assertEqual(self.model.number_rooms, 0)
        self.assertEqual(self.model.number_bathrooms, 0)
        self.assertEqual(self.model.max_guest, 0)
        self.assertEqual(self.model.price_by_night, 0)
        self.assertEqual(self.model.latitude, 0.0)
        self.assertEqual(self.model.longitude, 0.0)
        self.assertEqual(self.model.amenities, [''])

    def test_types(self):
        """tests whether isntance attribute types are correct
        """
        self.assertFalse(type(self.model.amenities) is str)
        self.assertTrue(type(self.model.name) is str)
        self.assertTrue(type(self.model.city_id) is str)
        self.assertTrue(type(self.model.user_id) is str)
        self.assertTrue(type(self.model.description) is str)
        self.assertTrue(type(self.model.number_rooms) is int)
        self.assertTrue(type(self.model.number_bathrooms) is int)
        self.assertTrue(type(self.model.max_guest) is int)
        self.assertTrue(type(self.model.price_by_night) is int)
        self.assertTrue(type(self.model.longitude) is float)
        self.assertTrue(type(self.model.latitude) is float)

    def test_save(self):
        """tests the save attribute
        """
        mc = self.model.created_at
        self.model.save()
        mc_saved = self.model.created_at
        self.assertTrue(mc == mc_saved)

if __name__ == "__main__":
    unittest.main()
