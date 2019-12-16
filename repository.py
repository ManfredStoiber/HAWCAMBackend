import mysql.connector
from repository_interface import RepositoryInterface


class Repository(RepositoryInterface):

    def __init__(self, model, uc):
        super().__init__(model, uc)


    def fire_sql(self, connection, query, prepared, tupel):
        result = False
        if (prepared == True):
            try:
                cursor = connection.cursor(prepared=True)
                cursor.execute(query, tupel)
                connection.commit()
                result = True
            except mysql.connector.Error as error:
                print("parameterized query failed {}".format(error))
            finally:
                if(result == True):
                    temp = cursor.lastrowid
                    cursor.close()
                    return temp
                else:
                    return False
        else:
            try:
                cursor = connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
            except mysql.connector.Error as error:
                print("select statement failed {}".format(error))
            finally:
                cursor.close()
                return result


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
        result = None
        sql_insert_cat_query = "INSERT INTO Categories (Category_name, deleted) VALUES (%s, %s)"
        sql_insert_tupel = model.getTupel()
        cat_key = self.fire_sql(connection, sql_insert_cat_query, sql_insert_tupel)
        sql_insert_attr_query = "INSERT INTO Attribues (Name, Datatype, deleted) VALUES (%s, %s, %s)"
        sql_insert_relation_query = "INSERT INTO Categorie_to_Attributes (idCategorie, idAttribute, mandatory) VALUES (%s, %s, %s)"
        for detail in model.details.detail_list:
            temp_tupel = (detail.getTupel()[0], detail.getTupel()[1], detail.getTupel()[3])  # ohne mandatory
            sql_insert_tupel = temp_tupel
            result = attr_key = self.fire_sql(connection, sql_insert_attr_query, True, sql_insert_tupel)
            sql_insert_tupel = (cat_key, attr_key, detail.getTupel()[2])
            result = self.fire_sql(connection, sql_insert_relation_query, True, sql_insert_tupel)
        return result


    def list_categories(self, connection):
        sql_select_cat_query = "Select Category_name as Name, Count(idObject) as Anzahl From Categories C " \
                               "Inner Join  Object_to_category OC on C.idCategories = OC.idCategorie " \
                               "Group By C.idCategories Order by Category_name ASC"
        result = self.fire_sql(connection, sql_select_cat_query, False, tupel=None)
        return result


    def connect_with_db(self):
        try:
            connection = mysql.connector.connect(host="remotemysql.com", user="xbKMa0eIqY", passwd="wqGNkrfAkK",
                                                 db="xbKMa0eIqY")
            result = False
            if self.uc == "createCategory":
                self.delete_table_data(connection)
                result = self.create_category(self.model, connection)
                self.check_insert_with_select(connection)
            elif self.uc == "listCategories":
                result = self.list_categories(connection)
            else:
                print("Nichts weiter")
            connection.close()
            return result
        except:
            return False
