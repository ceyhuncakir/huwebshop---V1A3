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
