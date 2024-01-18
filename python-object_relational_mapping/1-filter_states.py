import MySQLdb
from sys import argv
if __name__=='__main__':
    mysql_username = argv[1]
    mysql_pass = argv[2]
    my_db = argv[3]
    my_conn= MySQLdb.connect(host='localhost',port=3306,user=mysql_username,passwd= mysql_pass,db = my_db)
    cursor = my_conn.cursor()
    cursor.execute('SELECT * FROM states WHERE BINARY LEFT (name, 1) = "N" ORDER BY id ASC')
    rows = cursor.fetchall()
    for row in rows:
        print (row)
    cursor.close()
    my_conn.close()