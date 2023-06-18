#!/usr/bin/python3
#Script listing every state from the database hbtn_0e_0_usa:
import MySQLdb
import sys

if __name__ == '__main__':
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connecting to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Cursor object creation to interact with database
    cursor = db.cursor()

    # Execute the query to retrieve all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
