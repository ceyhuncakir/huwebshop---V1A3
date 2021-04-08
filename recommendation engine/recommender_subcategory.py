import time
import random
from termcolor import colored
from mySQL_framework import *

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


