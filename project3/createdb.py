import csv
import sqlite3

fileName = 'heart.csv'
file = open(fileName, 'r', encoding="unicode_escape")
reader = csv.reader(file)

conn = sqlite3.connect('/Users/hyegwan/codestates/project3/heartDB.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE HeartDisease(
    Age INTEGER,
    Sex VARCHAR(5),
    ChestPain VARCHAR(5),
    RestingBP INTEGER,
    Cholesterol INTEGER,
    FastingBS INTEGER,
    RestingECG VARCHAR(30),
    MaxHR INTEGER,
    ExerciseAngina VARCHAR(30),
    Oldpeak FLOAT,
    ST_slope VARCHAR(30),
    Heartdisease INTEGER
    )"""
)

empty = []

for row in reader:
    empty.append(row)

for row in empty:
    strSQL = 'INSERT INTO HeartDisease(Age, Sex, ChestPain, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR,  ExerciseAngina,  Oldpeak, ST_slope, Heartdisease)values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cur.execute(strSQL, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))

DEL_FIRST = """DELETE FROM HeartDisease WHERE Age = 'Age'"""
cur.execute(DEL_FIRST)
conn.commit()

cur.close()
conn.close()