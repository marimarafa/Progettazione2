import psycopg2

#Dettagli di connessione 
host="localhost"
port="5432"
dbname="Anagrafe"
user="postgres"
password="postgres"

#Connessione al database 
try:
    connection = psycopg2.connect(
        host = host,
        port = port,
        dbname = dbname,
        user = user ,
        password = password
    )
    print("Connessione al database avvenuta con successo\n")
except Exception as e:
    print(f"Errore durante la connessione al database :{e}")
