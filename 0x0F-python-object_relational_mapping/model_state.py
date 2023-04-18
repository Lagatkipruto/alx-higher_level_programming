#!/usr/bin/python3
""" It defines a State model.
 Inherits from SQLAlchemy Base and links to the MySQL table states.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """It represents a class of state for a MySQL database.
    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy."Integer"): The state's id.
    name (sqlalchemy."String"): The state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
