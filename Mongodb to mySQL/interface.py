from termcolor import colored
from main import *

colors = ["green", "blue", "yellow", "red", "cyan"]


# Voornamelijk gemaakt door: Ceyhun Cakir, Studentnummer: 1784480,
def banner():
    print(colored('''
    @============================================================================================@

     /$$   /$$ /$$   /$$                         /$$                 /$$
    | $$  | $$| $$  | $$                        | $$                | $$
    | $$  | $$| $$  | $$ /$$  /$$  /$$  /$$$$$$ | $$$$$$$   /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$
    | $$$$$$$$| $$  | $$| $$ | $$ | $$ /$$__  $$| $$__  $$ /$$_____/| $$__  $$ /$$__  $$ /$$__  $$
    | $$__  $$| $$  | $$| $$ | $$ | $$| $$$$$$$$| $$  \ $$|  $$$$$$ | $$  \ $$| $$  \ $$| $$  \ $$
    | $$  | $$| $$  | $$| $$ | $$ | $$| $$_____/| $$  | $$ \____  $$| $$  | $$| $$  | $$| $$  | $$
    | $$  | $$|  $$$$$$/|  $$$$$/$$$$/|  $$$$$$$| $$$$$$$/ /$$$$$$$/| $$  | $$|  $$$$$$/| $$$$$$$/
    |__/  |__/ \______/  \_____/\___/  \_______/|_______/ |_______/ |__/  |__/ \______/ | $$____/
                                                                                        | $$
                                                                                        | $$
                                                                                        |__/

    @============================================================================================@

    ''', colors[randrange(5)]))

# Voornamelijk gemaakt door: Ceyhun Cakir, Studentnummer: 1784480,
def mysql_rules():
    print(colored('''
    @=============================== MySQL database regels (voorbeeld) ==========================@\n
    1: products (table) | (Columns): ()
    2: profiles (table) | (Columns): ()
    3: sessions (table) | (Columns): ()\n
    @============================================================================================@\n
    ''', colors[randrange(2)]))

# Voornamelijk gemaakt door: izabelle Auriaux, Studentnummer: 1762808,
def opties():
    print(colored('''
    @====================================== Menu opties =========================================@\n
    1: Automatisch aanmaken van het predifined mySQL tables
    2: Overzetten van big data vanuit (mongoDB) naar (mySQL)
    3: Verwijderen van mySQL database table
    4: Error menu
    5: Quit program\n
    @============================================================================================@\n
    ''', colors[randrange(2)]))

# Voornamelijk gemaakt door: Ceyhun Cakir, Studentnummer: 1784480,
def table_remove_options():

    print(colored('''
    @====================================== Delete Table Options ================================@\n
    1: Verwijder alle tables
    2: Verwijder geselecteerde table\n
    @============================================================================================@\n
    ''', colors[randrange(3)]))
