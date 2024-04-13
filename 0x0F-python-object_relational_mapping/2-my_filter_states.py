#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    # Create a cursor object using cursor() method
    cur = conn.cursor()

    # Prepare SQL query to retrieve states matching the user input
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute SQL query with user input as parameter
    cur.execute(query, (sys.argv[4],))

    # Fetch all the rows in a list of tuples
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()

