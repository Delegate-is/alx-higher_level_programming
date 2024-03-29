#!/usr/bin/python3
"""
Listing every state name starting with N (upper N)
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    query = "SELECT * FROM states\
             WHERE states.name LIKE BINARY 'N%'\
             ORDER BY states.id ASC"
    cursor = db.cursor()
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
