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
        if direction == 1:
            prodids = self.get_gender(profileid)
            return prodids, 200
        elif direction == 2:
            prodids = self.get_main(profileid)
            return prodids, 200
        elif direction == 3:
            prodids = self.get_sub(profileid)
            return prodids, 200

        # random recommendation voor basket
            #randcursor = database.products.aggregate([{ '$sample': { 'size': count } }])
            #prodids = list(map(lambda x: x['_id'], list(randcursor)))
            #return prodids, 200

    def get_gender(self, current_id):
        """
        Loop through the recommendation tables and find the corresponding profile id. The tables are sorted from content
        to collaborative filters. if the profile is not in the content filter it will look through the collaborative filers
        """
        # Create sql connection
        db = mysql.connector.connect(host="localhost", user="root", password="", database="test")
        cursor = db.cursor()
        # Varible list with all the table's
        content = ["gender_recommendation"]
        response = []
        # for each item in content try
        for item in content:
            current_id_quotes = "'" + str(current_id) + "'"
            response = self.get_products(cursor, item, current_id_quotes)
            if response:
                break
        cursor.close()
        db.commit()
        db.close()
        return list(response[0])

    def get_main(self, current_id):
        """
        Loop through the recommendation tables and find the corresponding profile id. The tables are sorted from content
        to collaborative filters. if the profile is not in the content filter it will look through the collaborative filers
        """
        # Create sql connection
        db = mysql.connector.connect(host="localhost", user="root", password="", database="test")
        cursor = db.cursor()
        # Varible list with all the table's
        content = ["main_category_recommendation"]
        response = []
        # for each item in content try
        for item in content:
            current_id_quotes = "'" + str(current_id) + "'"
            response = self.get_products(cursor, item, current_id_quotes)
            if response:
                break
        cursor.close()
        db.commit()
        db.close()
        return list(response[0])

    def get_sub(self, current_id):
        """
        Loop through the recommendation tables and find the corresponding profile id. The tables are sorted from content
        to collaborative filters. if the profile is not in the content filter it will look through the collaborative filers
        """
        # Create sql connection
        db = mysql.connector.connect(host="localhost", user="root", password="", database="test")
        cursor = db.cursor()
        # Varible list with all the table's
        content = ["sub_category_recommendation"]
        response = []
        # for each item in content try
        for item in content:
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
            query = "SELECT product_one, product_two, product_three, product_four FROM %s WHERE id = %s" % (
            content, current_id)
            cursor.execute(query)
            data = cursor.fetchall()
        except:
            data = []
        return data


# This method binds the Recom class to the REST API, to parse specifically
# requests in the format described below.
api.add_resource(Recom, "/<string:profileid>/<int:direction>/<int:count>")
