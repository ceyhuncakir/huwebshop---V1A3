def insert_Querry(tabelnaam, *column):
    query = "INSERT IGNORE INTO " + tabelnaam
    qColumn = " (" + column[0]
    values = " VALUES (%s"
    i = 1
    while i < len(column):
        qColumn += ", " + column[i]
        values += ", %s"
        i += 1
    query += qColumn + ")" + values + ")"
    return query

def selectTable(selectList, fromlist, where):
    query = "SELECT "

    for item in range(len(selectList) - 1):
        query += str(selectList[item]) + ", "
    query += selectList[-1] + " "

    query += "FROM "

    for item in range(len(fromlist) - 1):
        query += str(fromlist[item]) + ", "
    query += fromlist[-1] + " "

    query += "WHERE "

    count = 0
    while count != len(where):
        query += str(where[count]) + " = " + str(where[count + 1])
        count += 2
        if count != len(where):
            query += " AND "

    return query