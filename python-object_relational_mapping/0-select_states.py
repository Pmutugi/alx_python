import MySQLdb
from sys import argv
mysql_username = argv[1]
mysql_pass = argv[2]
my_db = argv[3]
my_conn= MySQLdb.connector(host='localhost',port='3306',user=mysql_username,passwd= mysql_pass,database = my_db)
cursor = my_conn.cursor()
query= 'SELECT * FROM states ORDER BY id ASC'
cursor.execute(query)
for row in cursor:
    print (row)
cursor.close()
my_conn.close()
