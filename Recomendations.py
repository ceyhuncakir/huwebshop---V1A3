from db_query import *
import random

# def getRecomendation(cursor, profileid,):

""""
Profile functies
"""
def retrieve_order_profiles(cursor):
    query = selectTable(["sessions.profiles_id_key"], ["orders", "sessions"], ["sessions.id", "orders.sessions_id_key"])
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def get_profiles_content(cursor, profileid):
    """
    functie voor het krijgen van profiel_data
    :return profiel_data
    """
    new_item = "'" + str(profileid) + "'"
    query = selectTable(["products.id", "orders.aantal", "gender.gender", "orders.sessions_id_key", "sessions.profiles_id_key"],
                        ["products", "gender", "orders", "sessions"], ["products.gender_id_key", "gender.id", "orders.products_id_key", "products.id",
                                                           "orders.sessions_id_key", "sessions.id", "profiles_id_key", new_item])
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def get_profiles_content2(cursor, profileid,a,b,c):
    new_item = "'" + str(profileid) + "'"
    query = selectTable(a,b,c)
    cursor.execute(query)
    data = cursor.fetchall()
    return data
""""
Gender recomendations
"""
def get_gender_recommendation(cursor, profileid):
    """
    functie voor het maken van content recommendation gebasseerd op producten die lijken op wat er laats is gekocht
    :param cursor
    :param profielid
    :return profileid, random 4 recommendated products
    """

    prodids = []
    # sim_prod_list = []
    product_gender = {}
    none_list = []

    # functie voor het ophalen van data voor de huidige profiel waar de recommendation moet gebeuren
    profile_data = get_profiles_content(cursor, profileid)

    # for loop voor vergelijkbaren producten
    for i in profile_data:
        if i[2] not in product_gender:
            product_gender[i[2]] = 1
        elif i[2] in product_gender:
            product_gender[i[2]] += 1

    products = sorted(product_gender, key=product_gender.get, reverse=True)[:1]

    new_item = '"' + str(products[0]) + '"'
    query = selectTable(["products.id", "products.gender_id_key"], ["products", "gender"], ["products.gender_id_key", "gender.id", "gender.gender", new_item])

    cursor.execute(query)
    sim_prod = cursor.fetchall()

    #for loop voor het inzetten van vergelijkbaren producten
    for k, v in enumerate(sim_prod):
        prodids.append(v[0])

    if len(prodids) < 4:
        for i in range(0, 4, 1):
            none_list.append("None")

    try:
        return profileid, random.sample(prodids, 4), products
    except ValueError:
        return profileid, random.sample(none_list, 4), products

def recommendation_gender(db, cursor):
    # db, cursor = mysqlConnectie(login_data)
    profiles = retrieve_order_profiles(cursor)

    for i in profiles:
        profile_content, recommendation_content, gender = get_gender_recommendation(cursor, i[0])
        query = insert_Querry("gender_recommendation", "id", "product_one", "product_two", "product_three", "product_four")
        profile_list = [profile_content]
        for item in recommendation_content:
            profile_list.append(item)
        # print(query, profile_list)
        cursor.execute(query, profile_list)

        query = insert_Querry("gender_profiles", "id", "gender")
        gender_list = [profile_content, gender[0]]

        cursor.execute(query, gender_list)
        db.commit()

""""
sub_category recomendaitons
"""
def getRecomendationSubCatgory(cursor, profileID):
    # print("hoi")
    productIDS = []
    productSubCategory = []
    products = {}
    # print(f'profileID {profileID}')
    new_item = '"' + str(profileID) + '"'
    profielInfo = get_profiles_content2(cursor, profileID, ["products.id", "orders.aantal", "sub_category.sub_category", "orders.sessions_id_key", "sessions.profiles_id_key"],
                                        ["products", "sub_category", "orders", "sessions"], ["products.sub_category_id_key", "sub_category.id", "orders.products_id_key", "products.id",
                                                           "orders.sessions_id_key", "sessions.id", "profiles_id_key", new_item])
    # print(f'profielInfo {profielInfo}')
    for set in profielInfo:
        if set[2] not in products:
            products[set[2]] = 1
        elif set[2] in products:
            products[set[2]] += 1

    products = sorted(products,key=products.get, reverse=True)[:1]
    new_item = "'" + str(products[0]) + "'"
    query = selectTable(["products.id", "products.sub_category_id_key"], ["products", "sub_category"],
                        ["products.sub_category_id_key", "sub_category.id", "sub_category.sub_category", new_item])
    try:
        cursor.execute(query)
        sim_prod = cursor.fetchall()
    except:
        return profileID, ['0','0','0','0'],products

    for k, v in enumerate(sim_prod):
        productIDS.append(v[0])

    none_list = []
    if len(productIDS) < 4:
        for i in range(0, 4, 1):
            none_list.append("")
    try:
        return profileID, random.sample(productIDS, 4), products
    except ValueError:
        return profileID, random.sample(none_list, 4), products

def recomendation_sub_category(db, cursor):
    profiles = retrieve_order_profiles(cursor)
    
    for profile in profiles:
        # print(f'profile: {profile[0]}')
        profielInhoud, voorstelInhoud, subCategory = getRecomendationSubCatgory(cursor, profile[0])
        query = insert_Querry("sub_category_recommendation","id", "product_one", "product_two", "product_three",
                                "product_four")
        profielLijst = [profielInhoud]
        for item in voorstelInhoud:
            profielLijst.append(item)
            
        cursor.execute(query,profielLijst)
        
        query = insert_Querry("sub_category_profiles","id","sub_category")
        subCategoryLijst = [profielInhoud,subCategory[0]]

        cursor.execute(query, subCategoryLijst)
        db.commit()

"""
main_category recomendations.
"""
def getRecomendationMainCategory(cursor, profileID):
    productIDS = []
    new_item = "'" + str(profileID) + "'"
    profielInfo = get_profiles_content2(cursor, profileID, ["products.id", "orders.aantal", "main_category.main_category",
                                                            "orders.sessions_id_key", "sessions.profiles_id_key"],
                                        ["products", "main_category", "orders", "sessions"],
                                        ["products.main_category_id_key", "main_category.id", "orders.products_id_key",
                                         "products.id","orders.sessions_id_key", "sessions.id", "profiles_id_key", new_item])
    products = {}
    for set in profielInfo:
        if set[2] not in products:
            products[set[2]] = 1
        elif set[2] in products:
            products[set[2]] += 1

    products = sorted(products, key=products.get, reverse=True)[:1]

    new_item = '"' + str(products[0]) + '"'
    query = selectTable(["products.id", "products.main_category_id_key"], ["products", "main_category"],
                        ["products.main_category_id_key", "main_category.id", "main_category.main_category", new_item])
    cursor.execute(query)
    sim_prod = cursor.fetchall()

    for k, v in enumerate(sim_prod):
        productIDS.append(v[0])

    none_list = []
    if len(productIDS) < 4:
        for i in range(0, 4, 1):
            none_list.append("")

    try:
        return profileID, random.sample(productIDS, 4), products
    except ValueError:
        return profileID, random.sample(none_list, 4), products

def recomendationMainCategory(db,cursor):
    profiles = retrieve_order_profiles(cursor)
    for profile in profiles:
        profielInhoud, voorstelInhoud, mainCategory = getRecomendationMainCategory(cursor, profile[0])
        query = insert_Querry("main_category_recommendation" , "id", "product_one", "product_two", "product_three",
                                "product_four")
        profielLijst = [profielInhoud]
        for item in voorstelInhoud:
            profielLijst.append(item)

        cursor.execute(query,profielLijst)

        query = insert_Querry("main_category_profiles","id","main_category")
        mainCategoryLijst = [profielInhoud,mainCategory[0]]
        # print(query, mainCategoryLijst)
        cursor.execute(query, mainCategoryLijst)
        db.commit()