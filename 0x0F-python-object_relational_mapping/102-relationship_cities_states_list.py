#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa.
 Usage: ./102-relationship_cities_states_list.py <mysql username> /
                                                 <mysql password> /
                                                 <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Creating an engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Creating session object
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querrying the database for city objects
    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
