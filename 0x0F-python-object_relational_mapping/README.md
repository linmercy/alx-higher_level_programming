# Python Object-Relational Mapping Project

## Background Context
This project bridges two incredible worlds: Databases and Python! In the first part, you'll utilize the MySQLdb module to establish a connection with a MySQL database and execute SQL queries. In the second part, you'll leverage the SQLAlchemy module, an Object Relational Mapper (ORM).

The primary distinction here is the shift from writing SQL queries to interacting with objects in Python. With an ORM, you abstract away the storage concerns, focusing more on working with objects rather than worrying about the underlying database structure. Moreover, your code becomes independent of the storage type, allowing for easy transitions between different storage systems without rewriting the entire project.

Here's a quick comparison:

Without ORM:
```python
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()

