import mysql.connector
import json

def createTable(tabelnaam, *b):
    """"
    creeerd de query voor het aanmaken van een tabel.
    """
    values = " VARCHAR(255)"
    query = "CREATE TABLE IF NOT EXISTS " + tabelnaam + "(" + b[0] + values + " PRIMARY KEY UNIQUE"
    i = 1
    while i < len(b):
        query += ", " + b[i] + values + " NULL"

        i += 1
    query += ")"
    return query

def drop_table(table_name):
    """
    Creates quary for dropping the table. If it exists.
    """
    query = "DROP TABLE IF EXISTS " + table_name
    return query

def autoLogin():
    """
    interface functie waar de gebruiker input kan hebben
    :return
    """
    login_dict = {}
    # banner()
    try:
        open('login.txt')
    except FileNotFoundError:
        login_dict['host'] = input("\n\t" + "Geef je host op: ", "yellow")
        login_dict['gebruiker'] = input("\n\t" + "Geef je mysql username op: ", "yellow")
        login_dict['wachtwoord'] = input("\n\t" + "Geef je mysql password op: ", "yellow")
        login_dict["dbNaam"] = input("\n\t" + "Geef je mysql database op: ", "yellow")
        with open('login.txt', 'w') as file:
            file.write(json.dumps(login_dict))
            file.close()

    with open('login.txt') as file:
        login_dict = json.load(file)
    return login_dict

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

def mysqlSluit(db, cursor):
    cursor.close()
    db.commit()
    db.close()
