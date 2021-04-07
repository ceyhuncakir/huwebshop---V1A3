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

