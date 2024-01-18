import MySQLdb
from sys import argv
# if __name__=='__main__':
mysql_username = argv[1]
mysql_pass = argv[2]
my_db = argv[3]
states_name =argv[4]
conn= MySQLdb.connect(host='localhost',port=3306,user=mysql_username,passwd= mysql_pass,db = my_db)
cursor = conn.cursor()
query = "SELECT cities.name FROM cities INNER JOIN states ON cities.state_id=states.id WHERE  states.name= %s ORDER BY cities.id ASC"
cursor.execute(query, (states_name,))
rows =cursor.fetchall()
cities = [row[0] for row in rows]
print(", ".join(cities))
# for i, row in enumerate(rows):
      
#     print(row[0], end='')
#       if i < len(rows)-1:
#           print(', ', end='')
#  
# print("")
# cursor.close()
# conn.close()