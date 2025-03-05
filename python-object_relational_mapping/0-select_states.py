#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)
    cursor = db.cursor()
    
    # Execute the SQL query to get all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    
    # Fetch all results and print them
    for row in cursor.fetchall():
        print(row)
    
    # Close cursor and database connection
    cursor.close()
    db.close()
