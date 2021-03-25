# Huwebshop
Git voor het huwebshop project - Groep V1A-3.

# Leden

Ceyhun Cakir : student nummer 1784480 : Email: ceyhun.cakir@student.hu.nl<br/>
Kenny van de Berg : student nummer: 1777503 : Email: kenny.vandenberg@student.hu.nl<br/>
Izabelle Auriaux : student nummer : 1762808 : Email: izabelle.auriaux@student.hu.nl<br/>
Wytze A. Ketel : student nummer : 1797080 : Email : watze.ketel@student.hu.nl<br/>

# Instructies
In de onderstaande kopjes (opstarten) (huw.py) (huw_recommend.py) staan de instructies waar je aan moet voldoen om de huwebshop werken te krijgen

# Huw.py
Verander de volgende regels binnen de huw.py bestand


```
Regel 22 | dbstring = 'mongodb://admin:admin123@127.0.0.1/huwebshop?retryWrites=true&w=majorit' NAAR dbstring = 'mongodb://EIGEN MONGODB USERNAME:EIGEN MONGODB PASSWORD@127.0.0.1/EIGEN MONGODB DATABASE?retryWrites=true&w=majorit'
Regel 61 | self.database = self.client.huwebshop NAAR self.database = self.client.EIGEN MONGODB DATABASE
```

# Huw_recommend.py
Verander de volgende regels binnen de huw_recommend.py bestand

```
Regel 15 | dbstring = 'mongodb://admin:admin123@127.0.0.1/huwebshop?retryWrites=true&w=majority' NAAR dbstring = 'mongodb://EIGEN MONGODB USERNAME:EIGEN MONGODB PASSWORD@127.0.0.1/EIGEN MONGODB DATABASE?retryWrites=true&w=majority'
Regel 26 | database = client.huwebshop NAAR database = client.EIGEN MONGODB DATABASE
```

# Opstarten
Door op de gegeven bestand (startup instructions.txt) te klikken zie je de startup commands. Met deze startup commands kan je de huwebshop werkent krijgen door het in een command prompt in te vullen. Zie onderstaande afbeeldingen ↓

![](Gitimg/Afbeelding1.png)

![](Gitimg/Afbeelding2.png)


# Versie

Versie 1.0.0 | 25-3-2021
