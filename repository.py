import mysql.connector
from repository_interface import RepositoryInterface


class Repository(RepositoryInterface):

    def __init__(self, model, uc):
        super().__init__(model, uc)

    def fire_sql(self, connection, query, prepared, tupel):
        if (prepared == True):
            try:
                cursor = connection.cursor(prepared=True)
                cursor.execute(query, tupel)
                connection.commit()
                return cursor.lastrowid
            except mysql.connector.Error as error:
                #print("parameterized query failed {}".format(error))
                raise
            finally:
                cursor.close()
        else:
            try:
                cursor = connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                return result
            except mysql.connector.Error as error:
                print("select statement failed {}".format(error))
                raise
            finally:
                cursor.close()

    def check_insert_with_select(self, connection):
        mycursor = connection.cursor()
        mycursor.execute("Select * From category")
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Category " + str(x))
        mycursor.execute("Select * From attribute")
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Attribute " + str(x))
        mycursor.execute("Select * From category_to_attribute")
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Attribute_to_Category: " + str(x))

    def delete_table_data(self, connection):
        mycursor = connection.cursor()
        mycursor.execute("Delete From category_to_attribute")
        mycursor.execute("Delete From category")
        mycursor.execute("Delete From attribute")

    def create_category(self, model, connection):
        sql_insert_cat_query = "INSERT INTO category (Category_name, deleted) VALUES (%s, %s)"
        sql_insert_tupel = model.getTupel()
        cat_key = sql_insert_tupel[0]
        self.fire_sql(connection, sql_insert_cat_query, True, sql_insert_tupel)  # idCategories hier irrelevant
        sql_insert_attr_query = "INSERT INTO attribute (attribute_name, attribute_datatype, deleted) VALUES (%s, %s, " \
                                "%s) "
        sql_insert_relation_query = "INSERT INTO category_to_attribute (category_name, id_attribute, mandatory) " \
                                    "VALUES (%s, %s, %s) "
        for detail in model.details.detail_list:
            try:
                temp_tupel = (detail.getTupel()[0], detail.getTupel()[1], detail.getTupel()[3])  # ohne mandatory
                sql_insert_tupel = temp_tupel
                attr_id = self.fire_sql(connection, sql_insert_attr_query, True, sql_insert_tupel)
            except:
                attr_id_query = "SELECT id_attribute FROM attribute WHERE attribute_name = '" + detail.getTupel()[0] + \
                                "' "    # dirty Workaround, da prep. Statement mit einem Param nicht ging
                attr_id = self.fire_sql(connection, attr_id_query, False, tupel=None)
                attr_id = attr_id[0][0]
            sql_insert_tupel = (cat_key, attr_id, detail.getTupel()[2])
            self.fire_sql(connection, sql_insert_relation_query, True, sql_insert_tupel)

    def list_categories(self, connection):
        sql_select_cat_query = "SELECT C.Category_name AS Name, Count(OC.id_object) AS Anzahl FROM category C " \
                               "LEFT JOIN object_to_category OC ON C.Category_name = OC.categorie_name " \
                               "GROUP BY C.Category_name ORDER BY C.Category_name ASC"
        result = self.fire_sql(connection, sql_select_cat_query, False, tupel=None)
        return result

    def connect_with_db(self):
        connection = mysql.connector.connect(host="remotemysql.com", user="xbKMa0eIqY", passwd="wqGNkrfAkK",
                                             db="xbKMa0eIqY", connect_timeout=1000)
        if self.uc == "createCategory":
            # self.delete_table_data(connection)
            self.create_category(self.model, connection)
            self.check_insert_with_select(connection)
        elif self.uc == "listCategories":
            result = self.list_categories(connection)
            return result
        else:
            print("Nichts weiter")
        connection.close()
