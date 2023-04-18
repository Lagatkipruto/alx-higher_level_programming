#!/usr/bin/python3
"""Itcreates the state "California" with the City "San Francisco"
fromdatabase hbtn_0e_100_usa
Ittakes these args: mysql username\
            mysql password\
            database name
Usage:./100-relationship_states_cities.py
It should connect to MySQL server running on localhost
    port3306
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    # Creating the running engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
