#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    # Create a cursor object using cursor() method
    cur = conn.cursor()

    # Prepare SQL query to retrieve cities of the given state
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    # Execute SQL query
    cur.execute(query, (sys.argv[4],))

    # Fetch all the rows in a list of tuples
    rows = cur.fetchall()

    # Print the results
    print(", ".join([row[0] for row in rows]))

    # Close the cursor and connection
    cur.close()
    conn.close()

