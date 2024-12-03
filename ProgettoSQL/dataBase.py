import DBconnection as db
import sys

cursor = db.connection.cursor()
def PrintQuery():
    rows = cursor.fetchall()
    count = 0
    for row in rows:
        count +=1   
        print(row)
    print("\tTotal rows : " , count)

while True :
    op = print("\nScegliere query da eseguire:\n1)scegli la tabella \n2)scegli la tabella con condizione \n3)Stampa query \n4)esci ")
    num_op = input("--> ")
    if num_op == "1":
        tabella = input("Inserisci nome della tabella -> ")
        query1 = f"select * from {tabella} "
        cursor.execute(query1)
        PrintQuery()
        
    elif num_op == "2":
        tabella = input("Inserisci nome della tabella -> ")
        condizione = input("inserisci la condizione ->  ")
        query2 = f"select * from {tabella} where {condizione} "
        cursor.execute(query2)
        PrintQuery()
       
    elif num_op == "3":
        query3 = "select * from AttivitaProgetto where tipo = 'Ricerca e Sviluppo' and oredurata = 6"
        cursor.execute(query3)
        PrintQuery()
    else:
        sys.exit()



 
