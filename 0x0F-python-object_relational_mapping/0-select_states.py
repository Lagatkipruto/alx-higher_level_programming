#!/usr/bin/python3
# It lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#        <mysql password> \
#        <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306)
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host='localhost', port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
