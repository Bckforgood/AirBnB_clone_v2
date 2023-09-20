#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """SQL database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Create engine and connect to database"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        envi = getenv("HBNB_ENV", "none")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database), pool_pre_ping=True)

        if envi == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for element in query:
                key = "{}.{}".format(type(element).__name__, element.id)
                dic[key] = element
        else:
            liste = [State, City, User, Place, Review, Amenity]
            for clase in liste:
                query = self.__session.query(clase)
                for el in query:
                    key = "{}.{}".format(type(el).__name__, element.id)
                    dic[key] = element
        return (dic)

    def new(self, obj):
        """add the object to thedatabase"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the database """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from current database obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create current database session from the engine"""
        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        """Remove """
        self.__session.close()
