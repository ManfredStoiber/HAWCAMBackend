import mysql.connector
from repository import *

connection = mysql.connector.connect(host="remotemysql.com", user="xbKMa0eIqY", passwd="wqGNkrfAkK", db="xbKMa0eIqY")
query = "Select C.Category_name as Name, Count(idObject) as Anzahl From Categories C " \
                               "Left Join  Object_to_category OC on C.Category_name = OC.Category_name " \
                               "Group By C.Category_name Order by C.Category_name ASC"
query1 = "Select * From category"
query2 = "Insert Ignore into Objects (Name, deleted, description) Values ('PS5', 0, 'Spielekonsole');"
query3 = "Insert into Object_to_category values (16, 'Raum')"
query4 = "Select * from Objects"
query5 = "Select * from Object_to_category"
query6 = "Select * from attribute"
query7 = "Select * from category_to_attribute"
query8 = "Delete from category"
query9 = "Delete from category_to_attribute"
query0 = "Delete from attribute"

cursor = connection.cursor()
cursor.execute(query1)
#cursor.execute(query9)
#cursor.execute(query0)
#cursor.execute(query8)
#cursor.execute(query1)

result = cursor.fetchall()
for x in result:
    print(x)

cursor.close()
connection.commit()
connection.close()