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
```

# Startup
By clicking on the given file (startup instructions.txt) you will see the startup commands. With these startup commands you can get the huwebshop working by entering it in a command prompt. See images below ↓

![](Gitimg/Afbeelding1.png)

![](Gitimg/Afbeelding2.png)


# Version

Versie 1.0.1 | 27-3-2021
