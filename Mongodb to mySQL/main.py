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
