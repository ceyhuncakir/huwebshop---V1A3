from mySQL_framework import *
import time
import random


def retrieve_order_products(cursor, profile_list):
    """
    Retrieve all products for each profile.
    :param cursor: sql cursor
    :param profile_list: All profile id's
    :return: list of profile products
    """
    profile_product_list = []

    for item in profile_list:
        # Create a new_string for query ' are needed.
        new_item = "'" + str(item[0]) + "'"
        # retrieve all order products id
        cursor.execute("SELECT orders.products_id_key FROM orders, sessions WHERE orders.sessions_id_key = sessions.id AND sessions.profiles_id_key = %s" % new_item)
        data = cursor.fetchall()
        profile_product_list.append([item[0], retrieve_correct(data)])

    return profile_product_list


def frequency_category(product, freq_dict, product_category, num):
    """
    Determine the frequency of every product in a list and add them to a dictionary
    :param product: original list of products
    :param freq_dict: frequency dictionary
    :param product_category: Products need to be counted
    :param num: counter or weight
    :return:
    """
    # for item in product_category
    for item in product_category:
        # if the item is already in products
        if item[0] not in freq_dict and item[0] not in product:
            # add item in dict and add given value
            freq_dict[item[0]] = num
        elif item[0] in freq_dict and item[0] not in product:
            freq_dict[item[0]] += num
    return freq_dict