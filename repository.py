import mysql.connector
from repository_interface import RepositoryInterface


class Repository(RepositoryInterface):

    def __init__(self, model, uc):
        super().__init__(model, uc)

    def fire_sql(self, connection, query, prepared, tupel):
        if (prepared is True):
            try:
                cursor = connection.cursor(prepared=True)
                cursor.execute(query, tupel)
                connection.commit()
                return cursor.lastrowid
            except mysql.connector.Error as error:
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

    def create_category(self, connection):
        sql_insert_cat_query = "INSERT INTO category (Category_name, deleted) VALUES (%s, %s)"
        sql_insert_tuple = self.model.get_tuple()
        cat_key = sql_insert_tuple[0]
        self.fire_sql(connection, sql_insert_cat_query, True, sql_insert_tuple)  # idCategories hier irrelevant
        sql_insert_attr_query = "INSERT INTO attribute (attribute_name, attribute_datatype, deleted) VALUES (%s, %s, " \
                                "%s) "
        sql_insert_relation_query = "INSERT INTO category_to_attribute (category_name, id_attribute, mandatory) " \
                                    "VALUES (%s, %s, %s) "
        for detail in self.model.details.detail_list:
            try:
                temp_tuple = (detail.get_tuple()[0], detail.get_tuple()[1], detail.get_tuple()[3])  # ohne mandatory
                sql_insert_tuple = temp_tuple
                attr_id = self.fire_sql(connection, sql_insert_attr_query, True, sql_insert_tuple)
            except:
                attr_id_query = "SELECT id_attribute FROM attribute WHERE attribute_name = '" + detail.get_tuple()[0] + \
                                "' "    # dirty Workaround, da prep. Statement mit einem Param nicht ging
                attr_id = self.fire_sql(connection, attr_id_query, False, tupel=None)
                attr_id = attr_id[0][0]
            sql_insert_tuple = (cat_key, attr_id, detail.get_tuple()[2])
            self.fire_sql(connection, sql_insert_relation_query, True, sql_insert_tuple)

    def list_categories(self, connection):
        sql_select_cat_query = "SELECT C.Category_name AS Name, Count(OC.id_object) AS Anzahl FROM category C " \
                               "LEFT JOIN object_to_category OC ON C.Category_name = OC.categorie_name " \
                               "GROUP BY C.Category_name ORDER BY C.Category_name ASC"
        result = self.fire_sql(connection, sql_select_cat_query, False, tupel=None)
        return result

    def list_attributes(self, connection, category):
        sql_select_cat_query = "SELECT a.attribute_name, a.attribute_datatype, ca.mandatory " \
                               "FROM category_to_attribute ca " \
                               "INNER JOIN attribute a ON ca.id_attribute = a.id_attribute " \
                               "WHERE ca.Category_name = " + str(category) + ";"
        result = self.fire_sql(connection, sql_select_cat_query, False, tupel=None)
        return result

    def create_object(self, connection):
        sql_insert_obj_query = "INSERT INTO object (object_name, object_deleted) VALUES (%s, %s)"
        sql_insert_obj_tuple = self.model.get_tuple()
        obj_key = self.fire_sql(connection, sql_insert_obj_query, True, sql_insert_obj_tuple)
        sql_insert_relation_query = "INSERT INTO object_to_category (id_object, categorie_name) VALUES (%s, %s) "
        sql_insert_relation_tuple = (obj_key, self.model.cat_name)
        self.fire_sql(connection, sql_insert_relation_query, True, sql_insert_relation_tuple)
        # i = 1
        for detail in self.model.details.detail_list:
            sql_insert_obj_attr_query = "INSERT INTO attribute_to_object (value, id_object) VALUES (%s, %s)"
            sql_insert_obj_attr_tuple = (detail, obj_key)
            self.fire_sql(connection, sql_insert_obj_attr_query, True, sql_insert_obj_attr_tuple)

    def search(self, connection, search):
        sql_search_cat_query = "SELECT Category_name FROM category WHERE Category_name LIKE '%" + str(search[1:-1]) + "%'"
        result_cat = self.fire_sql(connection, sql_search_cat_query, False, tupel=None)
        sql_search_obj_query = "SELECT O.object_name, OC.categorie_name FROM object O " \
                               "INNER JOIN object_to_category OC ON O.id_object = OC.id_object " \
                               "WHERE O.object_name LIKE '%" + str(search[1:-1]) + "%'"
        result_obj = self.fire_sql(connection, sql_search_obj_query, False, tupel=None)
        print("result_cat = " + str(result_cat))
        print("result_obj = " + str(result_obj))
        result = result_cat + result_obj
        print("result = " + str(result))
        return result

    def delete(self, table, condition):
        try:
            connection = mysql.connector.connect(host="remotemysql.com", user="xbKMa0eIqY", passwd="wqGNkrfAkK",
                                                 db="xbKMa0eIqY", connect_timeout=1000)
            query = "Delete From " + table + " Where " + condition + ";"
            cursor = connection.cursor()
            cursor.execute(query)
            cursor.close()
            connection.commit()
            connection.close()
        except:
            raise

    def connect_with_db(self, *argv):
        connection = mysql.connector.connect(host="remotemysql.com", user="xbKMa0eIqY", passwd="wqGNkrfAkK",
                                             db="xbKMa0eIqY", connect_timeout=1000)
        if self.uc == "createCategory":
            self.create_category(connection)
        elif self.uc == "listCategories":
            result = self.list_categories(connection)
            return result
        elif self.uc == "listAttributes":
            result = self.list_attributes(connection, argv[0])
            return result
        elif self.uc == "createObject":
            self.create_object(connection)
        elif self.uc == "search":
            result = self.search(connection, argv[0])
            return result
        connection.close()
