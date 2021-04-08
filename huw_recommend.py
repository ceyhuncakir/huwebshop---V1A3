from flask import Flask, request, session, render_template, redirect, url_for, g
from flask_restful import Api, Resource, reqparse
import os
from pymongo import MongoClient
from dotenv import load_dotenv
import mysql.connector

app = Flask(__name__)
api = Api(app)

# We define these variables to (optionally) connect to an external MongoDB
# instance.
envvals = ["MONGODBUSER","MONGODBPASSWORD","MONGODBSERVER"]
dbstring = 'mongodb://admin:admin123@127.0.0.1/huwebshop?retryWrites=true&w=majority'

# Since we are asked to pass a class rather than an instance of the class to the
# add_resource method, we open the connection to the database outside of the
# Recom class.
load_dotenv()
if os.getenv(envvals[0]) is not None:
    envvals = list(map(lambda x: str(os.getenv(x)), envvals))
    client = MongoClient(dbstring)
else:
    client = MongoClient()
database = client.huwebshop

class Recom(Resource):
    """ This class represents the REST API that provides the recommendations for
    the webshop. At the moment, the API simply returns a random set of products
    to recommend."""
    #  shopping_card,
    def get(self, profileid, direction, count):

        # gender recommendation
        prodids = self.get_recommendation(profileid, direction)
        return prodids, 200


    def get_recommendation(self, current_id, direction):
        db = mysql.connector.connect(host="localhost", user="root", password="", database="test")
        cursor = db.cursor()
        # Varible list with all the table's
        if direction == 1:
            content = ["gender_recommendation", "recommendation_profile_orders"]
        elif direction == 2:
            content = ["main_category_rec", "gender_recommendation", "recommendation_profile_orders"]
        elif direction == 3:
            content = ["sub_category_recommendation", "main_category_rec", "gender_recommendation", "recommendation_profile_orders"]

        response = []
        # for each item in content try
        for item in content:
            print(item)
            current_id_quotes = "'" + str(current_id) + "'"
            response = self.get_products(cursor, item, current_id_quotes)
            if response:
                break
        cursor.close()
        db.commit()
        db.close()
        return list(response[0])

    def get_products(self, cursor, content, current_id):
        """
        For the given table and profile id retrieve the products. if there is no corresponding id return a empty list
        """
        # Try mysql querry
        try:
            query = "SELECT product_1, product_2, product_3, product_4 FROM %s WHERE id = %s" % (
            content, current_id)
            cursor.execute(query)
            data = cursor.fetchall()
        except:
            data = []
        return data


# This method binds the Recom class to the REST API, to parse specifically
# requests in the format described below.
api.add_resource(Recom, "/<string:profileid>/<int:direction>/<int:count>")
