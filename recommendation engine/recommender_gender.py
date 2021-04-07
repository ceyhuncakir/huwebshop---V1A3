import time
import random
from termcolor import colored
from mySQL_framework import *


def get_profiles_content(cursor, profileid):
    """
    functie voor het krijgen van profiel_data
    :return profiel_data
    """

    # mysql sql commando om data te krijgen van de huidge profiel waar recommendation op moet gebeuren
    cursor.execute("SELECT products.id, orders.aantal, gender.gender, orders.sessions_id_key, sessions.profiles_id_key FROM `products`, `gender`, `orders`, `sessions` WHERE products.gender_id_key = gender.id AND orders.products_id_key = products.id AND orders.sessions_id_key = sessions.id AND profiles_id_key = '%s'" % profileid)
    profile_data = cursor.fetchall()

    return profile_data

def get_gender_recommendation(cursor, profileid):
    """
    functie voor het maken van content recommendation gebasseerd op producten die lijken op wat er laats is gekocht
    :param cursor
    :param profielid
    :return profileid, random 4 recommendated products
    """

    prodids = []
    sim_prod_list = []
    product_gender = {}
    similiar_products = {}
    none_list = []

    # functie voor het ophalen van data voor de huidige profiel waar de recommendation moet gebeuren
    profile_data = get_profiles_content(cursor, profileid)

    # for loop voor vergelijkbaren producten
    for i in profile_data:
        if i[2] not in product_gender:
            product_gender[i[2]] = 1
        elif i[2] in product_gender:
            product_gender[i[2]] += 1

    all_values = product_gender.values()
    max_value = max(all_values)

    # hier word er gekeken of de profiel minder dan 2 orders heeft zo ja voert die geen recommendation op dat profiel zo niet maakt die wel een recommendation
    if max_value <= 2:
        return 0

    products = sorted(product_gender, key=product_gender.get, reverse=True)[:1]

    cursor.execute("SELECT products.id, orders.aantal, products.gender_id_key FROM `products`,`orders`, `gender` WHERE products.gender_id_key = gender.id AND orders.products_id_key = products.id AND gender.gender = '{0}'".format(products[0]))
    sim_prod = cursor.fetchall()

    #frequentie berekening van het product wat meest gekocht word
    for i in sim_prod:
        if i[0] not in similiar_products:
            similiar_products[i[0]] = 1
        elif i[0] in similiar_products:
            similiar_products[i[0]] += 1

    # hier pakt die het top 10 best verkochte producten met het gepaste gender
    sim_prod = sorted(similiar_products, key=similiar_products.get, reverse=True)[:10]

    #for loop voor het inzetten van vergelijkbaren producten
    if len(sim_prod) < 4:
        return 0

    #print(colored("\n\t" + "content filtering Done", "green"), colored("\t" + "profiel:" + profileid, "yellow"))
    return profileid, random.sample(sim_prod, 4), products
