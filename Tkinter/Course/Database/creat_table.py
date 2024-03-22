import sqlite3
conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute( """ CREATE TABLE  if not exists todo_L(
               ID int ,
               Task text)
               """)
# cursor.execute("INSERT INTO todo_L VALUES (20, 'shark')")
# cursor.execute("INSERT INTO todo_L VALUES (10, 'cuttlefish')")
# result = cursor.execute("select * from todo_L")

# for i in result:
#     print(i)
#EACH elements
# for i in  result:
#     ids , tasks = i
#     print(ids,tasks)





#commit changes
conn.commit()
#close our connection
conn.close()