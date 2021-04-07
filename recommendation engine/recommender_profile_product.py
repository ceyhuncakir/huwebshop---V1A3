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


def retrieve_similar_profile_products(cursor, product):
    """
    Retrieve for each product all sessions that bought the same item. for each session return all items bought.
    :param cursor: sql cursor
    :param product: current product
    :return: list of all similar products to the profile
    """
    # Create a new_string for query ' are needed.
    new_item = "'" + str(product) + "'"
    # Retrieve all sessions with the same item bought
    cursor.execute("SELECT orders.sessions_id_key FROM orders WHERE orders.products_id_key = %s" % new_item)
    profiles = cursor.fetchall()


    profile_products_list = []
    # for each profile
    for item in profiles:
        # Create a new_string for query ' are needed.
        new_item = "'" + str(item[0]) + "'"
        # for each sessions return all items bought

        cursor.execute("SELECT orders.products_id_key FROM orders WHERE orders.sessions_id_key = %s" % new_item)
        profile_items = cursor.fetchall()
        # add the list to profile_products_list
        profile_products_list += list(profile_items)
    return profile_products_list


def product_profile(cursor, profile_products_list):
    """
    For each profile return random sample of 4 of the most frequency bought items. if there are more than 2 products
    skip the product (Beter recomondations can be made). for each product retrieve all orders with that product.
    determine the frequency of ever product. Sort the list on the highest frequency and return 4 items out of the 10
    most bought items.
    :param cursor: sql cursor
    :param profile_products_list: profile with all the products
    :return: return a list of 4 products with profile id
    """
    profile_recomondation = []
    # for each profile
    for profile in profile_products_list:
        recomondation_product = {}
        # if profile contaions more than 2 products skip the profile
        if len(profile[1]) >= 2:
            continue
        # for each product in profile
        for product in profile[1]:
            # Retrieve similar profile items.
            similar_profile_products = retrieve_similar_profile_products(cursor, product)
            # Reduce duplicates
            recomondation_product = frequency_category(profile[1], recomondation_product, similar_profile_products, 0.01)
        # Sort the dictionary and return the first 4 items
        products = sorted(recomondation_product, key=recomondation_product.get, reverse=True)[:10]
        # if length of recommended products is lower than 4 skip profile
        if len(products) < 4:
            continue
        profile_recomondation.append([profile[0], random.sample(products, 4)])
    return profile_recomondation


def retrieve_correct(data):
    """
    Return de all products from different sessions in one list
    :param data:
    :return: list
    """
    # Create a list
    product_list = []
    # Loop trough a list of lists.
    for products in data:
        # loop trough all items
        for product in products:
            # append item in product_list
            product_list.append(product)
    return product_list


def recommendation_profile_orders_process(login_dict):
    """
    Rule: People similar to you bought.
    This process creates 4 recommendations based on the orders. For each profile with orders return all
    products. For each product in profiles retrieve all sessions with similar products and determine the frequency
    and add a value for each product to determine highest recommended. Return 4 random product items of the 10 most
    common product.
    :param login_dict: Username and passwoord
    :return: Start and End time.
    """
    # Create connection with to mysql database.  # localhost
    db, cursor = mysqlConnectie(login_dict)
    start = time.time()

    delete_table(cursor, "recommendation_profile_orders")
    create_rule_table(cursor, "recommendation_profile_orders", "", 1)

    # Retrieve all profiles that have orders.
    profiles_orders = retrieve_order_profiles(cursor)
    # Retrieve all products id's for each profile.
    profile_products_list = retrieve_order_products(cursor, profiles_orders)
    # Retrieve a list of profiles with four items.
    products = product_profile(cursor, profile_products_list)

    # Insert all data into table
    for profile_products in products:
        insert_values(0, profile_products[0], profile_products[1], db, cursor, "recommendation_profile_orders", "id", "product_1",
                      "product_2", "product_3", "product_4")

    # Commit and close database connection
    sql_closer(db, cursor)
    end = time.time()
    return start, end