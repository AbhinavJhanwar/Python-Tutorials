

import pymssql

server = "ip address"
user = "user"
password = "password"


conn = pymssql.connect(server, user, password, "table")
cursor = conn.cursor()
cursor.execute('SELECT * FROM table')

for row in cursor:
    print('row = %r' % (row,))

conn.close()