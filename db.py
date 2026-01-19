import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="faisal999",   
    database="university_events"
)

cursor = conn.cursor()
