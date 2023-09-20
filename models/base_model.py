#!/usr/bin/python3
"""This is the base model class for AirBnB"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import uuid
from models import storage

Base = declarative_base()

class BaseModel:
    """Base class for all models"""
    __abstract__ = True

    def __init__(self, *args, **kwargs):
        """Initializes a new model instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            time_format = '%Y-%m-%dT%H:%M:%S.%f'
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], time_format)
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], time_format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def save(self):
        """Updates updated_at with the current time and saves to storage"""
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def delete(self):
        """Deletes the current instance from storage"""
        storage.delete(self)

    def to_dict(self):
        """Converts the instance to a dictionary"""
        dictionary = dict(self.__dict__)
        dictionary.pop('_sa_instance_state', None)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

