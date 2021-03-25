# Huwebshop
Git voor het huwebshop project - Groep V1A-3.

# Leden

Ceyhun Cakir : student nummer 1784480 : Email: ceyhun.cakir@student.hu.nl<br/>
Kenny van de Berg : student nummer: 1777503 : Email: kenny.vandenberg@student.hu.nl<br/>
Izabelle Auriaux : student nummer : 1762808 : Email: izabelle.auriaux@student.hu.nl<br/>
Wytze A. Ketel : student nummer : 1797080 : Email : watze.ketel@student.hu.nl<br/>

# Instructies

# Huw.py
Verander de volgende regels binnen de huw.py bestand

```
Regel 22 | dbstring = 'mongodb://admin:admin123@127.0.0.1/huwebshop?retryWrites=true&w=majorit' NAAR dbstring = 'mongodb://admin:admin123@127.0.0.1/EIGEN MONGODB DATABASE?retryWrites=true&w=majorit'
Regel 61 | self.database = self.client.huwebshop NAAR self.database = self.client.EIGEN MONGODB DATABASE
```

# Huw_recommend.py
Verander de volgende regels binnen de huw_recommend.py bestand


```
Regel 16 | dbstring = 'mongodb://admin:admin123@127.0.0.1/huwebshop?retryWrites=true&w=majority' NAAR dbstring = 'mongodb://admin:admin123@127.0.0.1/EIGEN MONGODB DATABASE?retryWrites=true&w=majority'
Regel 27 | database = client.huwebshop NAAR database = client.EIGEN MONGODB DATABASE
```

# Versie

Versie 1.0.0 | 25-3-2021
