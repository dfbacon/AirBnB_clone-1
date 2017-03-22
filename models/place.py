#!/usr/bin/python3
'''
This is the 'place' module.
'''
from models import *
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import *
from sqlalchemy.orm import relationship


class PlaceAmenity(Base):
        '''This is the 'PlaceAmenity' class'''
        __tablename__ = "place_amenity"
        place_id = Column(String(60), ForeignKey('places.id'),
                          primary_key=True, nullable=False)
        amenity_id = Column(String(60), ForeignKey('amenities.id'),
                            primary_key=True, nullable=False)


class Place(BaseModel, Base):
        '''This is the 'Place' class'''
        if Base is not object:
                __tablename__ = "places"
                city_id = Column(String(60), ForeignKey("cities.id"),
                                 nullable=False)
                user_id = Column(String(60), ForeignKey("users.id"),
                                 nullable=False)
                name = Column(String(128), nullable=False)
                description = Column(String(1024), nullable=False)
                number_rooms = Column(Integer, nullable=False, default=0)
                number_bathrooms = Column(Integer, nullable=False, default=0)
                max_guest = Column(Integer, nullable=False, default=0)
                price_by_night = Column(Integer, nullable=False, default=0)
                latitude = Column(Float, nullable=False)
                longitude = Column(Float, nullable=False)
                amenities = relationship("Amenity", secondary='place_amenity',
                                         viewonly=True)

        else:
                city_id = ""
                user_id = ""
                name = ""
                description = ""
                number_rooms = 0
                number_bathrooms = 0
                max_guest = 0
                price_by_night = 0
                latitude = 0.0
                longitude = 0.0
                amenities = [""]

        def __init__(self, *args, **kwargs):
                '''This is the initialization method'''
                super().__init__(*args, **kwargs)
