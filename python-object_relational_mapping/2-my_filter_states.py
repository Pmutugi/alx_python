import MySQLdb
from sys import argv
if __name__=='__main__':
    mysql_username = argv[1]
    mysql_pass = argv[2]
    my_db = argv[3]
    conn= MySQLdb.connect(host='localhost',port=3306,user=mysql_username,passwd= mysql_pass,db = my_db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4]))
    rows =cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()