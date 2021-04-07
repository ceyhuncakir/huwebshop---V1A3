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
