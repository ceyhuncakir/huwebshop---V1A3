""""
Test bestand voor het aanmaken van alle verbindingen.
(Nog) geen diepe UI integratie.
"""
from data_out import *
from Recomendations import *
import time

def main():
    loginInfo = autoLogin()
    db, cursor = mysqlConnectie(loginInfo)
    start = time.time()

    """"
    Gender onderdeel
    """
    drop = drop_table("gender_recommendation")
    cursor.execute(drop)
    drop = drop_table("gender_profiles")
    cursor.execute(drop)

    create_table = createTable("gender_recommendation", "id", "product_one", "product_two", "product_three",
                               "product_four")
    create_table_two = createTable("gender_profiles", "id", "gender")

    cursor.execute(create_table)
    cursor.execute(create_table_two)
    recommendation_gender(db, cursor)
    """"
    sub_category onderdeel
    """
    cursor.execute(drop_table("sub_category_recommendation"))
    cursor.execute(drop_table("sub_category_profiles"))

    recommendationTable = createTable("sub_category_recommendation","id", "product_one", "product_two", "product_three",
                                "product_four")
    profileTable = createTable("sub_category_profiles", "id", "sub_category")
    cursor.execute(recommendationTable)
    cursor.execute(profileTable)
    recomendation_sub_category(db, cursor)
    """"
    Main category
    """
    cursor.execute(drop_table("main_category_recommendation"))
    cursor.execute(drop_table("main_category_profiles"))

    recommendationTable = createTable("main_category_recommendation","id", "product_one", "product_two", "product_three",
                                 "product_four")
    profileTable = createTable("main_category_profiles", "id", "main_category")
    cursor.execute(recommendationTable)
    cursor.execute(profileTable)
    recomendationMainCategory(db,cursor)

    end = time.time()
    print(f"Done: {end - start}")
    mysqlSluit(db, cursor)

main()