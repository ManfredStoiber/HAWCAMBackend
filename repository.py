import mysql.connector
from repository_interface import RepositoryInterface


class Repository(RepositoryInterface):

    def __init__(self, model, uc):
        super().__init__(model, uc)

    def fire_sql(self, connection, query, tupel):
        try:
            cursor = connection.cursor(prepared=True)
            cursor.execute(query, tupel)
            connection.commit()
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
        finally:
            temp = cursor.lastrowid
            cursor.close()
            return temp

    def check_insert_with_select(self, connection):
        mycursor = connection.cursor()
        mycursor.execute("Select * From Categories")
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Category " + str(x))
        mycursor.execute("Select * From Attribues")
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Attribute " + str(x))
        mycursor.execute("Select * From Categorie_to_Attributes")
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Attribute_to_Category: " + str(x))

    def delete_table_data(self, connection):
        mycursor = connection.cursor()
        mycursor.execute("Delete From Categorie_to_Attributes")
        mycursor.execute("Delete From Categories")
        mycursor.execute("Delete From Attribues")

    def create_category(self, model, connection):
        sql_insert_cat_query = "INSERT INTO Categories (Category_name, deleted) VALUES (%s, %s)"
        sql_insert_tupel = model.getTupel()
        cat_key = self.fire_sql(connection, sql_insert_cat_query, sql_insert_tupel)
        sql_insert_attr_query = "INSERT INTO Attribues (Name, Datatype, deleted) VALUES (%s, %s, %s)"
        sql_insert_relation_query = "INSERT INTO Categorie_to_Attributes (idCategorie, idAttribute, mandatory) VALUES (%s, %s, %s)"
        for detail in model.details.detail_list:
            temp_tupel = (detail.getTupel()[0], detail.getTupel()[1], detail.getTupel()[3])  # ohne mandatory
            sql_insert_tupel = temp_tupel
            attr_key = self.fire_sql(connection, sql_insert_attr_query, sql_insert_tupel)
            sql_insert_tupel = (cat_key, attr_key, detail.getTupel()[2])
            self.fire_sql(connection, sql_insert_relation_query, sql_insert_tupel)

    def transmit_model_to_repository(self):
        try:
            connection = mysql.connector.connect(host="remotemysql.com", user="xbKMa0eIqY", passwd="wqGNkrfAkK",
                                                 db="xbKMa0eIqY")
            if self.uc == "createCategory":
                self.delete_table_data(connection)
                self.create_category(self.model, connection)
                self.check_insert_with_select(connection)
            elif self.uc == "...":
                print("lala")
                # ...(interface.model)
            else:
                print("Nichts weiter")
            connection.close()
            return True
        except:
            return False
