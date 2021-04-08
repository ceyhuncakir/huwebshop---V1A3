import pymongo
from random import *
import sys
import mysql.connector
import time

#  Voornamelijk gemaakt door Kenny van den berg Studentnummer: 1777503 en Ceyhun Cakir, Studentnummer: 1784480
def mongo_database_names():
    """Set up connection with local mongodb and retrieve a list of all databases names
    :param mongo_client, :param db_names
    """
    # Set connection with mongo db
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Retrieve the names of all databases
    db_names = mongo_client.list_database_names()

    # Close connection
    mongo_client.close()
    return db_names

# Voornamelijk gemaakt door: izabelle Auriaux, Studentnummer: 1762808
def mysql_connector(user, password, db_name):
    """
    Hier verbind je met de database aan de hand van een host, username, wachtwoord en database naam. Die aanmeldings informatie sla je op onder een
    variable. Ook maak je een cursor die de vorige variable gebruikt om aan te melden.
    Je returned de variabele met de aanmeldingsgegevens en de cursor.
    :param user:, :param password:, :param db_name:
    """
    # Variable with a connection with mysql with the user, password and db_name
    db = mysql.connector.connect(host="localhost", user=user, password=password, database=db_name)

    # Variable for mysql cursor
    cursor = db.cursor()
    return db, cursor


# Voornamelijk gemaakt door: izabelle Auriaux, Studentnummer: 1762808 en Wytze A. Ketel, Studentnummer: 1797080
def sql_closer(db, cursor):
    """
    Sluit de cursor en commit de veranderingen van de database daarna sluit de database.
    :param cursor:, :param db:
    """
    # Close the cursor, commit de change made in the database and close the database
    cursor.close()
    db.commit()
    db.close()

def get_mysql_database_names(user, passwd):
    """
    Maakt verbinding met de DB en haalt alle database namen op.
    Voegt de namen aan een lijst toe en geeft deze terug.
    :param user:
    :param passwd:
    :return: lijst van database namen
    """
    # list variable for the databases
    db, cursor = mysql_connector(user, passwd, " ")
    database_name_list = []

    # Execute sql query to retrieve all database names
    cursor.execute("SHOW DATABASES")

    # varible with all items found
    database_names = cursor.fetchall()
    sql_closer(db, cursor)

    # retrieve the database names from with in a list with in a list
    for item in database_names:
        for db_name in item:
            database_name_list.append(db_name)
    return database_name_list

# voornamelijk gemaakt door: Ceyhun Cakir, Studentnummer: 1784480 en Wytze A. Ketel, Studentnummer: 1797080
def retrieve_mysql_table_names(cursor):
    """"
    Execute een query voor het opvragen van alle tabelen in de database. Return een lijst aan table namen.
    :param cursor:
    """
    # list for all tables
    list_tables = []

    # retrieve all tables
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    # append each table to list_tables
    for index in tables:
        for table in index:
            list_tables.append(table)
    return list_tables



# voornamelijk gemaakt door: izabelle Auriaux, Studentnummer: 1762808 en Wytze A. Ketel, Studentnummer: 1797080
def delete_database(database_name, cursor):
    """
    Je maakt een variable die een "drop database" quarry en een database inhoud
    en een variable die een "create database" quarry en een database inhoud.
    Vervolgens excecute je deze variable via de cursor.
    Daarna print je dat de tables zijn verwijdert. Als er een exception tussen zit word de mysql_error_print opgeroepen.
    :param cursor:
    :param database_name:
    :return:
    """
    # 2 varibles with my sql queries
    drop_query = "DROP DATABASE " + database_name
    create_query = "CREATE DATABASE " + database_name

    # Execute sql query drop and create
    cursor.execute(drop_query)
    cursor.execute(create_query)

# Voornamelijk gemaakt door: Ceyhun Cakir, Studentnummer: 1784480 | izabelle Auriaux : Studentnummer: 1762808
def create_predefined_tables(cursor, database_name):
    """ predefined
    Je voegt de verschillende tabellen toe aan de database, hierin geef je aan of het een primairt key is,
    wat voor type en onder welke tabel je hem toevoegd. Dit doe je individueel voor elke tabel.
    Daarna print je dat de tabellen zijn aangemaakt. Als er een exception tussen zit word de mysql_error_print opgeroepen.
    :param user:, :param password:, :param database:, :return:
    """
    cursor.execute("USE " + database_name)
    cursor.execute("CREATE TABLE sub_category (id INTEGER(10) AUTO_INCREMENT PRIMARY KEY UNIQUE, sub_category VARCHAR(255) NULL)")
    cursor.execute("CREATE TABLE main_category (id INTEGER(10) AUTO_INCREMENT PRIMARY KEY UNIQUE, main_category VARCHAR(255))")

    cursor.execute("CREATE TABLE doelgroep (id INTEGER(10) AUTO_INCREMENT PRIMARY KEY UNIQUE, doelgroep VARCHAR(255))")

    cursor.execute("CREATE TABLE gender (id INTEGER(10) AUTO_INCREMENT PRIMARY KEY UNIQUE, gender VARCHAR(255))")

    cursor.execute("CREATE TABLE brand (id INTEGER(10) AUTO_INCREMENT PRIMARY KEY UNIQUE, brand VARCHAR(255))")

    cursor.execute("CREATE TABLE profiles (id VARCHAR(255) PRIMARY KEY UNIQUE, first_order_item TIMESTAMP(6) NULL, last_order_item TIMESTAMP(6) NULL)")

    cursor.execute("CREATE TABLE sessions (id VARCHAR(255) PRIMARY KEY UNIQUE, date_from TIMESTAMP(6) NULL, date_to TIMESTAMP(6) NULL, profiles_id_key VARCHAR(255), FOREIGN KEY(profiles_id_key) REFERENCES profiles(id))")

    cursor.execute("CREATE TABLE products (id VARCHAR(255) PRIMARY KEY UNIQUE, price INTEGER(10), stock INTEGER(10), flavor VARCHAR(255) NULL, kleur VARCHAR(255) NULL, recomendable BIT(10), fast_mover BIT(10), gender_id_key INTEGER(10), doelgroep_id_key INTEGER(10), brand_id_key INTEGER(10), main_category_id_key INTEGER(10), sub_category_id_key INTEGER(10), FOREIGN KEY(gender_id_key) REFERENCES gender(id), FOREIGN KEY(brand_id_key) REFERENCES brand(id), FOREIGN KEY(main_category_id_key) REFERENCES main_category(id), FOREIGN KEY(doelgroep_id_key) REFERENCES doelgroep(id), FOREIGN KEY(sub_category_id_key) REFERENCES sub_category(id))")

    cursor.execute("CREATE TABLE orders (id INTEGER(10) AUTO_INCREMENT PRIMARY KEY UNIQUE, aantal INTEGER(10) NULL, products_id_key VARCHAR(255), sessions_id_key VARCHAR(255), FOREIGN KEY(products_id_key) REFERENCES products(id), FOREIGN KEY(sessions_id_key) REFERENCES sessions(id))")

    cursor.execute("CREATE TABLE already_recommended (id INTEGER(10) AUTO_INCREMENT PRIMARY KEY UNIQUE, profiles_id_key VARCHAR(255), products_id_key VARCHAR(255), FOREIGN KEY(profiles_id_key) REFERENCES profiles(id), FOREIGN KEY(products_id_key) REFERENCES products(id))")

#  Voornamelijk gemaakt door Kenny van den berg Studentnummer: 1777503 en Ceyhun Cakir, Studentnummer: 1784480
def try_except_flex(*value):
    """
    #     Gebruik een try except over de gegeven dict values, return  de dict value anders return je none
    #     :param value:, :param value1:, :return value[value1], :except return "None"
    #
    """
    # Een extra variable mee geven voor de keuze argument[0]
    try:
        if value[0] == 0:
            return value[1][value[2]]
        else:
            return value[1][value[2]][value[3]]
    except:
        return "None"


# Voornamelijk gemaakt door: izabelle Auriaux, Studentnummer: 1762808
def setting_list(list_value):
    """
    Maakt van list_value een set list, en retured deze.
    :param list_value:
    :return:
    """
    list_category_value = list(set(list_value))
    return list_category_value


# voornamelijk gemaakt door: Ceyhun Cakir, Studentnummer: 1784480 en Kenny van den berg Studentnummer: 1777503
def get_item_from_collection(db, cursor, database):
    """
    Maak een lege list voor de verschillende categorieen producten, merken, gender, doelgroep, sub cat & sub sub cat.
    Maak hiervoor ook lists die een profiel gaan voorstellen. En lege lists die collecties voorstellen.
    Daarna connect je met de mongo database en haal je de data op uit de database, deze verdeel je via de lege list waar het toebehoorend is.
    uiteindelijk geef je het door naar insert_into_mysql.
    :param db:
    :param cursor:
    :param database:
    :return:
    """
    # Opslaan van de values van collection products
    products_value_item = []

    # Categories of products
    product_categorie_list = [[], [], [], [], []]

    # Opslaan van de values van collection profiles
    profiles_values = []
    profiles_previously_recommended = []
    profiles_sessions_list = {}

    #opslaan van de values van collection sessions
    sessions_date_to_from = []
    sessions_orders = []

    #connectie naar het mongodb database
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Retrieve a list of all collections
    collections = mongo_client[database]

    # retrieve collections products, sessions and profiles
    collection_products = collections["products"]

    collection_session = collections["sessions"]

    collection_profile = collections["profiles"]

    # for loop voor het ophalen van data vanuit MongoDB
    for item in collection_products.find({}, {"_id", "price", "properties", "flavor", "properties", "recommendable", "fast_mover", "brand", "gender", "properties", "sub_category", "sub_sub_category"}):
        product_value_one = []
        product_value_one.append(try_except_flex(0, item, "_id"))                            # Id = index 0
        product_value_one.append(try_except_flex(1, item, "price", "selling_price"))         # Price = index 1
        product_value_one.append(try_except_flex(1, item, "properties", "stock"))            # Stock = index 2
        product_value_one.append(try_except_flex(0, item, "flavor"))                         # Flavor = index 3
        product_value_one.append(try_except_flex(1, item, "properties", "kleur"))
        product_value_one.append(try_except_flex(0, item, "recommendable"))
        product_value_one.append(try_except_flex(0, item, "fast_mover"))
        product_value_one.append(try_except_flex(0, item, "gender"))
        product_value_one.append(try_except_flex(1, item, "properties", "doelgroep"))
        product_value_one.append(try_except_flex(0, item, "brand"))
        product_value_one.append(try_except_flex(0, item, "sub_category"))
        product_value_one.append(try_except_flex(0, item, "sub_sub_category"))

        products_value_item.append(product_value_one)

        # data uithalen voor brand, gender, doelgroep, main_category, sub_category
        product_categorie_list[0].append(try_except_flex(0, item, "brand"))                        # brand = index 0
        product_categorie_list[1].append(try_except_flex(0, item, "gender"))                       # gender = index 1
        product_categorie_list[2].append(try_except_flex(1, item, "properties", "doelgroep"))      # properties = index 2
        product_categorie_list[3].append(try_except_flex(0, item, "sub_category"))                 # sub_category = index 3
        product_categorie_list[4].append(try_except_flex(0, item, "sub_sub_category"))             # sub_sub_category = index 4


    for item in collection_profile.find({}, {"_id", "buids", "previously_recommended", "order"}):
        column_id = try_except_flex(0,item, "_id")
        profiles_values.append([str(try_except_flex(0, item, "_id")), str(try_except_flex(1,item, "order", "first")),
                                str(try_except_flex(1, item, "order", "latest"))])

        column_buid = try_except_flex(0, item, "buids")

        # if there are multiple build loop through the list and add each buid and profile id to a dictionary
        if type(column_buid) == list:
            for index_item in column_buid:
                profiles_sessions_list[index_item] = str(column_id)


    for item in collection_session.find({}, {"buid", "session_start", "session_end", "order"}):
        column_start = try_except_flex(0, item, "session_start")
        column_end = try_except_flex(0, item, "session_end")
        column_buid = try_except_flex(0, item, "buid")

        id = try_except_flex(0, item, "_id")
        order = try_except_flex(0, item, "order")

        item_dict = {}
        item_list = []

        # if order is a dictionary
        if type(order) == dict:

            # for each product in the order
            for item in order['products']:
                # if the item is not in the dict, create item key and value 1
                if item['id'] not in item_dict:
                    item_dict[item['id']] = 1
                # else increment the value with one
                else:
                    item_dict[item['id']] += 1

            # for each key, value in item dict append the value, key and id.
            for key, value in item_dict.items():
                item_list.append([value, key, str(id)])

        # if the length of the list is not 0 append item
        if len(item_list) != 0:
            for item in item_list:
                sessions_orders.append(item)

        # Retrieve correct id build of profile to sessions.
        try:
            id_buid = profiles_sessions_list[column_buid[0]]
        except (TypeError, KeyError):
            id_buid = "None"

        sessions_date_to_from.append([str(id), str(column_start), str(column_end), id_buid])
    mongo_client.close()

    end, start = insert_into_mysql_process(db, cursor, products_value_item, product_categorie_list, profiles_previously_recommended, profiles_values, sessions_date_to_from, sessions_orders)
    return end, start
