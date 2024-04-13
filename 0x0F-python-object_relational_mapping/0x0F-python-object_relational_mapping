#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    # Create a cursor object using cursor() method
    cur = conn.cursor()

    # Execute SQL query to retrieve states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows in a list of tuples
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()

