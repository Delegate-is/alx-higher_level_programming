#!/usr/bin/python3
"""
Listing every cities in database using foreing key
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    query = "SELECT cities.id, cities.name FROM cities JOIN states ON cities.state_id = states.id"
    cursor = db.cursor()
    cursor.execute(query)
    for city in cursor.fetchall():
        print(city)
    cursor.close()
    db.close()
