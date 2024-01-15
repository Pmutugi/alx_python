import MySQLdb
from sys import argv
mysql_username = argv[1]
mysql_pass = argv[2]
my_db =argv[3]
my_conn= MySQLdb.connector(host='localhost',port='3306',user=mysql_username,passwd= mysql_pass,db =my_db)

