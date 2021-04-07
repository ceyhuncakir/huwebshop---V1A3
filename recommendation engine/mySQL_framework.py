import mysql.connector

def mysqlConnectie(loginInfo):
    """"
    Verbinding met de gekozen mysql database.
    Voor eenvoud wordt de loginInfo in 1 lijst; [], meegegeven via loginInfo
    :arg gebruiker ; Gebruikersnaam
    :arg wachtwoord ; wachtwoord behorend bij gebruikersnaam
    :arg dbNaam ; de naam van de database waarin gezoekt moet worden.
    :arg host ; de link naar de server. Voor localhost gebruik ("localhost")
    """
    db = mysql.connector.connect(host=loginInfo["host"], user=loginInfo["gebruiker"], password=loginInfo["wachtwoord"], database=loginInfo["dbNaam"])
    cursor = db.cursor()

    return db, cursor


def sql_closer(db, cursor):
    """
    Sluit de cursor en commit de veranderingen van de database daarna sluit de database.
    :param cursor:, :param db:
    """

    cursor.close()
    db.commit()
    db.close()


def create_rule_table(cursor, table_name, column, direction):
    """
    Create table with name variable "table_name" for to hold the recommendations.
    :param cursor:
    :param table_name:
    """
    # Create a table if it not already exists
    if direction == 1:
        query = "CREATE TABLE IF NOT EXISTS %s (id VARCHAR(255) PRIMARY KEY UNIQUE, product_1 VARCHAR(255)" \
               ", product_2 VARCHAR(255), product_3 VARCHAR(255), product_4 VARCHAR(255))""" % table_name
    elif direction == 2:
        query = "CREATE TABLE IF NOT EXISTS %s (id VARCHAR(255) PRIMARY KEY UNIQUE, %s VARCHAR(255))" % (table_name, column)

    cursor.execute(query)