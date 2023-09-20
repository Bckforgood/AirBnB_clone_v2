#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String

class Amenity(BaseModel):
    """Amenity class"""
    name = Column(String(128), nullable=False)
