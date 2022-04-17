import sqlite3

connect = sqlite3.connect('database.sqlite')
cursor = connect.cursor()

sql_text = """
    CREATE table phrases (
        id integer primary key,
        phrase text,
        answer text
    )
"""

sql_text = "INSERT INTO phrases values (1,'Привет','И тебе привет');"
cursor.execute(sql_text)
sql_text = "INSERT INTO phrases values (2,'Как дела?','Хорошо');"
cursor.execute(sql_text)
sql_text = "INSERT INTO phrases values (3,'Как дела?','А как твои?');"
cursor.execute(sql_text)
#sql_text = 'SELECT * from cars'

#result = cursor.fetchall()
#print(result)

connect.commit()
connect.close()