import time
import random
from termcolor import colored
from mySQL_framework import *

def get_sub_category_recommendation(cursor, profileid):
    """
    Maakt een voorstel aan per profiel op basis van de sub_category key.
    :param cursor: cursor key
    :param profielid: profielID key
    :return profileid, random 4 voorstel products
    """

    prodids = []
    sim_prod_list = []
    product_subcategory = {}
    similiar_products = {}
    none_list = []

    # functie voor het ophalen van data voor het huidige profiel waarvoor het voorstel moet gebeuren
    profile_data = get_profiles(cursor, profileid)

    # for loop voor vergelijkbaren producten
    for i in profile_data:
        if i[2] not in product_subcategory:
            product_subcategory[i[2]] = 1
        elif i[2] in product_subcategory:
            product_subcategory[i[2]] += 1

    #hier worden alle values van het dictionary opgehaald
    all_values = product_subcategory.values()
    #hier wordt de grootse frequentie opgehaalt
    max_value = max(all_values)

    #hier wordt de sub_category gesorteerd
    sub_category = sorted(product_subcategory, key=product_subcategory.get, reverse=True)[:1]


    new_item = "'" + str(sub_category[0]).replace("'", "''") + "'"
    cursor.execute("SELECT products.id, orders.aantal, products.sub_category_id_key FROM `products`,`orders`, `sub_category` WHERE products.sub_category_id_key = sub_category.id AND orders.products_id_key = products.id AND sub_category.sub_category = %s" % new_item)
    sim_prod = cursor.fetchall()

    # hier wordt de frequentie van het populairste items getelt
    for i in sim_prod:
        if i[0] not in similiar_products:
            similiar_products[i[0]] = 1
        elif i[0] in similiar_products:
            similiar_products[i[0]] += 1

    # hier word de top 10 producten op gesorteerd
    sim_prod = sorted(similiar_products, key=similiar_products.get, reverse=True)[:10]

    if len(sim_prod) < 4:
        return 0

    # hier pakken we random 4 producten uit de top 10 lijst van producten
    return profileid, random.sample(sim_prod, 4), sub_category

def get_profiles(cursor, profileid):
    """
    Haalt profielinformatie op voor elk profileid
    :param cursor: cursor key
    :param profileid: profiel ID
    :return profiel_data
    """

    # mysql sql commando om data te krijgen van de huidge profiel waar recommendation op moet gebeuren
    cursor.execute("SELECT products.id, orders.aantal, sub_category.sub_category, orders.sessions_id_key, sessions.profiles_id_key FROM `products`, `sub_category`, `orders`, `sessions` WHERE orders.products_id_key = products.id AND orders.sessions_id_key = sessions.id AND products.sub_category_id_key = sub_category.id AND profiles_id_key = '%s'" % profileid)
    profile_data = cursor.fetchall()

    return profile_data


def recommendation_subcategory(login_dict):
    """
    Zend data naar de juiste tabel in DB
    :param mysql_username
    :param mysql_password
    :param mysql_database
    :return
    """

    db, cursor = mysqlConnectie(login_dict)

    #hier word de verwijdering van de tabellen gedaan
    delete_table(cursor, "sub_category_profiles")
    delete_table(cursor, "sub_category_recommendation")

    #hier worden de tabellen aangemaakt
    create_rule_table(cursor, "sub_category_recommendation", "", 1)
    create_rule_table(cursor, "sub_category_profiles", "sub_category", 2)

    #orders worden opgehaald
    profiles = retrieve_order_profiles(cursor)

    for i in profiles:
        #hier gebeurt een try and catch door naar te kijken of er gevonden producten minder dan 4 zijn als dat zo is er een continue anders try die de insert
        try:
            profile_content, recommendation_content, sub_category = get_sub_category_recommendation(cursor, i[0])
            insert_values(0, profile_content, recommendation_content, db, cursor, "sub_category_recommendation", "id", "product_1", "product_2", "product_3", "product_4")
            insert_values(1, profile_content, sub_category, db, cursor, "sub_category_profiles", "id", "sub_category")
        except TypeError:
            continue

    start = time.time()

    end = time.time()
    sql_closer(db, cursor)
    return end, start
