## Rock-Paper-Scissors

# Installing Packages
`pip install PyQt5 ` 
\
`pip install pandas `
\
`pip install sqlite3 `
```python
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

# Screenshots

![alt text](zrzut1.png)
![alt text](zrzut2.png)
![alt text](zrzut3.png)
![alt text](zrzut4.png)
![alt text](zrzut5.png)
![alt text](zrzut6.png)


