# Huwebshop
Git for the huwebshop project - Group V1A-3.

# Project members

Ceyhun Cakir : student nummer 1784480 : Email: ceyhun.cakir@student.hu.nl<br/>
Kenny van de Berg : student nummer: 1777503 : Email: kenny.vandenberg@student.hu.nl<br/>
Izabelle Auriaux : student nummer : 1762808 : Email: izabelle.auriaux@student.hu.nl<br/>
Wytze A. Ketel : student nummer : 1797080 : Email : watze.ketel@student.hu.nl<br/>

# Installation
Install the following programs as shown below
```
Mongodb Compass (1.26.0)
Xampp (8.0.3)
```

# Required dependencies
```
Python 3 (3.7*)
Flask (1.0.3*)
Pymongo (3.8.0*)
Flask-RESTful (0.3.7*)
Python-Dotenv (0.10.3*)
Requests (2.22.0*)
```

# Transfer data from mongodb to mySQL
When you want to use the huwebshop for comercial purposes you should begin with the data transfer from mongodb to mySQL. Run the following file (interface.py) within the folder (Mongodb to mySQL) to transfer the data from mongodb to mySQL. See the example below

![](Gitimg/Afbeelding4.png)

Select (2) if you want the automation for the data transfer. Fill in the following credentials in the tool to achieve the data transfering

# Create recommendations for the webshop
Once your done with the data transfer you should be able to create recommendation. You can do this by running the following file (interface.py) within the folder (recommendation engine). See the example below

![](Gitimg/afbeelding5.png)

Once you filled in the credentials the recommendation engine will start to create recommendations. Note it will take a while for these to finish so have patience!. 

# Instructions
In the headings below (startup) (huw.py) (huw_recommend.py) are the instructions that you must comply with to get the huwebshop working

# Huw.py
Change the following lines within the huw.py file

```
Line 22 | dbstring = 'mongodb://admin:admin123@127.0.0.1/huwebshop?retryWrites=true&w=majorit' TO dbstring = 'mongodb://OWN MONGODB USERNAME:OWN MONGODB PASSWORD@127.0.0.1/OWN MONGODB DATABASE?retryWrites=true&w=majorit'
Line 61 | self.database = self.client.huwebshop NAAR self.database = self.client.OWN MONGODB DATABASE
```

# Huw_recommend.py
Change the following lines within the huw_recommend.py file

```
Line 15 | dbstring = 'mongodb://admin:admin123@127.0.0.1/huwebshop?retryWrites=true&w=majority' TO dbstring = 'mongodb://OWN MONGODB USERNAME:OWN MONGODB PASSWORD@127.0.0.1/OWN MONGODB DATABASE?retryWrites=true&w=majorit'
Line 26 | database = client.huwebshop NAAR database = client.OWN MONGODB DATABASE
Line 40 | db = mysql.connector.connect(host="localhost", user="root", password="", database="test") TO db = mysql.connector.connect(host="localhost", user="YOUR OWN USERNAME", password="YOUR OWN PASSWORD", database="YOUW OWN DATABASE")
```

# Keuzehulp
If you want to use the keuzehulp properly you should create a table within a database with the following name 
```
keuzehulp 
```

after u created a table with the name keuzehulp you should create the following columns

```
product_id (varchar(255), Primary key, NOT NULL))
optie_1 (varchar(255), NULL))
optie_2 (varchar(255), NULL))
optie_3 (varchar(255), NULL))
```

If the columns are finished u can proceed to fill these columns with the product id's in the column product_id and the following options behind it. See the example below

![](Gitimg/Afbeelding3.png)

Once you have filled the table with data. you can proceed to startup the huwebshop!

# Startup
By clicking on the given file (startup instructions.txt) you will see the startup commands. With these startup commands you can get the huwebshop working by entering it in a command prompt. See images below ↓

![](Gitimg/Afbeelding1.png)

![](Gitimg/Afbeelding2.png)


# Version

Versie 2.0.0 | 8-4-2021
