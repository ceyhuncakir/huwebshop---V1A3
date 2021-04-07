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


def delete_table(cursor, table_name):
    """
    Delete table with variable "table_name".
    :param cursor:
    :param table_name:
    """
    # Drop the table if it exists.
    query = "DROP TABLE IF EXISTS %s" % table_name
    cursor.execute(query)


def retrieve_order_profiles(cursor):
    """
    Return all profiles with orders.
    :param cursor:
    :return:
    """
    cursor.execute("SELECT DISTINCT sessions.profiles_id_key FROM orders, sessions WHERE sessions.id = orders.sessions_id_key")
    profiles_orders = cursor.fetchall()

    return profiles_orders


def insert_values(direction, profile, list_value, db, cursor, table, *column):
    """
    Connect aan de database en loop door de verschillende waardes in de list en voeg ze die dan toe aan de table collums.
    Execute deze command en commit het naar de sql database.
    :param direction:, :param profile, :param list_value:, :param db:, :param cursor:, :param table:, :param *column:, :return:,
    """

    if direction == 0:
        category_list_sql = "INSERT IGNORE INTO " + table + " (" + column[0] + ", " + column[1] + ", " + column[2] + ", " + column[3] + ", " + column[4] +") VALUES (%s, %s, %s, %s, %s)"
        category_list_sql_value = (str(profile), str(list_value[0]), str(list_value[1]), str(list_value[2]), str(list_value[3]))
        cursor.execute(category_list_sql, category_list_sql_value)

    elif direction == 1:
        category_list_sql = "INSERT IGNORE INTO " + table + " (" + column[0] + ", " + column[1] + ") VALUES (%s, %s)"
        category_list_sql_value = (str(profile), str(list_value[0]))
        cursor.execute(category_list_sql, category_list_sql_value)

    db.commit()