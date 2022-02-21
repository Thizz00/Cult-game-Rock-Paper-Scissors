import sqlite3
import pandas as pd
conn = sqlite3.connect('Score') 
c = conn.cursor()
c.execute('''CREATE TABLE USER(
Username TEXT NOT NULL,
score INTEGER   DEFAULT NULL
)
 ''')
conn.close()