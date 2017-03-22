#!/usr/bin/python3
from models import *
from sqlalchemy import Table, Column, Integer, Float, String, DateTime
import os

class PlaceAmenity(BaseModel):
        """  """
    if os.environ['HBNB_TYPE_STORAGE'] == "db":
        __tablename__ = "place_amenity"
    place_id = Column(String(60), nullable=False,
                      ForeignKey("places.id"), primary_key=True)
    amenity_id = Column(String(60), nullable=False,
                        ForeignKey("amenities.id"), primary_key=True)

class Place(BaseModel):
    '''This is the 'Place' class'''
    if os.environ['HBNB_TYPE_STORAGE'] == "db":
        __tablename__ = "places"
    city_id = Column(String(60), nullable=False, ForeignKey("cities.id"))
    user_id = Column(String(60), nullable=False, ForeignKey("user.id"))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer(), nullable=False, default=0)
    number_bathrooms = Column(Integer(), nullable=False, default=0)
    max_guest = Column(Integer(), nullable=False, default=0)
    price_by_night = Column(Integer(), nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenities = relationship("Amenity", viewonly=True, secondary=place_amenity)

    def __init__(self, *args, **kwargs):
        super().__init__()
