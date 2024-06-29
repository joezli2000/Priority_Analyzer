import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('mySQLLite.db')

# Create a cursor object
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE pareto_data (
            id INTEGER PRIMARY KEY,
            prod_name TEXT NOT NULL,
            frequency INTEGER,
            percentage REAL,
            cumu_percentage REAL,
            img BLOB,
            is_present NULL)''')

# List of tuples containing the data to insert
data = [
    (1, 'Prod_A', 333, 0.425, 0.425, None, 1),
    (2, 'Prod_B', 222, 0.282, 0.707, None, 1),
    (3, 'Prod_C', 111, 0.141, 0.848, None, 1),
    (4, 'Prod_D', 78, 0.099, 0.947, None, 1),
    (5, 'Prod_E', 37, 0.047, 0.994, None, 1),
    (6, 'Prod_F', 5, 0.006, 1.000, None, 1),
]

# Insert a row of data
# c.execute("INSERT INTO pareto_data VALUES (1,'Prod_A',333)")

# Insert multiple rows of data
c.executemany('INSERT INTO pareto_data VALUES (?,?,?,?,?,?,?)', data)

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()