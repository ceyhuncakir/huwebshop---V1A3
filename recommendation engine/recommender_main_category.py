from mySQL_framework import *
import random
import time


def main_category_rec(cursor, profiel_id):
    """
    Haal voor het gegeven profiel alle producten uit de database en bepaal de meest voorkomende main category. Haal
    alle producten uit de database met de main catagory en count daar de populairste producten van. sorteer de dictionary
    en haal 10 producten uit de lijst en return 4 random producten.

    :param cursor: sql cursor
    :param profiel_id: huidige profiel
    :return: 4 producten
    """
    # Dictionary met gelijke producten.
    products = {}

    # Haal de meest voorkomende category uit de database
    main_category = meest_voorkomend(cursor, profiel_id)

    # Alle producten die all eerder all georderd zijn met de huidige main category
    cursor.execute("SELECT products.id FROM products, orders, main_category WHERE products.main_category_id_key = main_category.id AND orders.products_id_key = products.id AND main_category.id = %s" % main_category )
    prod = cursor.fetchall()

    # Voor elke product bepaal het aantal keer dat het voorkomt
    for i in prod:
        if i[0] not in products:
            products[i[0]] = 1
        elif i[0] in products:
            products[i[0]] += 1
    # Sorteer de dictionary op waardes en haal de 10 meest voor komende producten er uit
    prod = sorted(products, key=products.get, reverse=True)[:10]

    # Als de lengte van de producten kleiner is dan 4 sla het profiel over
    if len(prod) < 4:
        return 0

    return profiel_id, random.sample(prod, 4)

def meest_voorkomend(cursor, profiel_id):
    """
    Bepaal de meest voor komende main category en tell die bij elkaar op. return de meest voorkomende main category
    :param cursor: sql cursor
    :param profiel_id:
    :return:
    """

    counter = 0
    # Haal alle producten van het profiel uit de database
    data = data_ophalen_uit_database(cursor, profiel_id)
    num = data[0]

    # Bepaal de meest voorkomende main catagory
    for i in data:
        # Count de aantal keer de main category er in voorkomt
        curr_frequency = data.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
    # Als Num 0 is return 0 en sla profiel over
    if num == None:
        return 0
    else:
        return num


def tabelInformatie(tabel, cursor):
    """
    Haal alle data uit table met huidige table naam
    :param tabel:
    :param cursor: sql cursor
    :return:
    """
    # Haal alle data van table varibale op
    cursor.execute("SELECT * FROM " + tabel)
    ophaal = cursor.fetchall()

    return ophaal


def data_ophalen_uit_database(cursor, profiel_id):
    """
    Haal alle producten op uit de database die het profiel heeft georderd.
    :param cursor: sql cursor
    :param profiel_id: het huidige profiel
    :return: lijst aan main category's
    """
    # list profiel main catagory
    profiel_cat = []
    # Haal alle producten met het huidige profiel op uit de table products relaatie orders.
    cursor.execute("SELECT products.id,products.price,products.stock,main_category.id,orders.aantal,brand.brand,gender.id,orders.sessions_id_key,doelgroep.id,sessions.profiles_id_key FROM `products`,`brand`,`gender`,`orders`,`main_category`,`sessions`,`doelgroep` WHERE products.gender_id_key = gender.id AND products.main_category_id_key = main_category.id AND products.brand_id_key = brand.id AND orders.products_id_key = products.id AND products.doelgroep_id_key = doelgroep.id AND orders.sessions_id_key = sessions.id AND profiles_id_key = '%s'" % profiel_id)
    profiel_data = cursor.fetchall()
    # Voor elke product in de tuple voeg de main category toe aan de lijst
    for item in profiel_data:
        profiel_cat.append(item[3])

    return profiel_cat

