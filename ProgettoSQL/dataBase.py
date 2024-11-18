import DBconnection as db

cursor = db.connection.cursor()

query = "select * from persona where posizione = 'Ricercatore'"
query2 = "select * from progetto"

cursor.execute(query)
cursor.execute(query2)

#recupera i risultati
rows = cursor.fetchall()
count = 0
for row in rows:
    count +=1
    print(row)
print("\tTotal rows : " , count)



 
