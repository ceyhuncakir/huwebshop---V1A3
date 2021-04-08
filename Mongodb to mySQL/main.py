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
