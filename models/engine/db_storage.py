#!/usr/bin/python3

from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    """This class handles database storage for the application"""

    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine and links it to the database"""
        user = environ.get('HBNB_MYSQL_USER')
        password = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST', 'localhost')
        database = environ.get('HBNB_MYSQL_DB')
        dialect = 'mysql'
        driver = 'mysqldb'
        pool_pre_ping = True if environ.get('HBNB_ENV') == 'test' else False

        self.__engine = create_engine(f'{dialect}+{driver}://{user}:{password}@{host}/{database}',
                                      pool_pre_ping=pool_pre_ping)

        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects in the database"""
        from models import classes

        objects = {}

        if cls:
            if isinstance(cls, str) and cls in classes:
                cls = classes[cls]
            else:
                return objects

            for obj in self.__session.query(cls).all():
                key = f"{type(obj).__name__}.{obj.id}"
                objects[key] = obj
        else:
            for cls in classes.values():
                for obj in self.__session.query(cls).all():
                    key = f"{type(obj).__name__}.{obj.id}"
                    objects[key] = obj

        return objects

    def new(self, obj):
        """Add an object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)


