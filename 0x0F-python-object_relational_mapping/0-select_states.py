#!/usr/bin/python3

""" It lists all states from the database hbtn_0e_0_usa.
 Usage: ./0-select_states.py <mysql username> \
        <mysql password> \
        <database name>
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Connecting to the localhost and port
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")

    # Create a cursor object to excute SQL queries
    cur = conn.cursor()

    # Execute SQL querries to retrieve all states, sorted by ascending order.
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all rows returned by the query
    query_rows = cur.fetchall()

    # Print the rows in the specified format
    for row in query_rows:
        print(row)

    # Close the database connection
    cur.close()
    conn.close()
