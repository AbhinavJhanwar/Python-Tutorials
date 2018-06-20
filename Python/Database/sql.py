'''
Created on May 3, 2018

@author: abhinav.jhanwar
'''
# PHASE 1: GETTING SERVER VERSION
import sqlite3 as lite
import sys
 
con = None
 
try:
    con = lite.connect('test.db')
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print ("SQLite version: %s" % data)
except lite.Error as e:   
    print ("Error %s:" % e.args[0])
    sys.exit(1)
finally:    
    if con:
        con.close()
        
# PHASE 2: CREATE TABLE & INSERT DATA
con = lite.connect('user.db')
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Users(Id INT, Name TEXT)")
    cur.execute("INSERT INTO Users VALUES(1, 'Michelle')")
    cur.execute("INSERT INTO Users VALUES(2, 'Sonya')")
    cur.execute("INSERT INTO Users VALUES(3, 'Greg')")
    cur.execute("INSERT INTO Users VALUES(4, 'Chris')")
    
# PHASE 3: EXPLORE
con = lite.connect('user.db')
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Users")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# PHASE 3: WORKING WITH MULTIPLE TABLES
con = lite.connect('system.db')
with con:
    cur = con.cursor()    
    #cur.execute("DROP TABLE Users")
    cur.execute("CREATE TABLE Users(Id INT, Name TEXT)")
    cur.execute("INSERT INTO Users VALUES(1,'Michelle')")
    cur.execute("INSERT INTO Users VALUES(2,'Howard')")
    cur.execute("INSERT INTO Users VALUES(3,'Greg')")
    
    #cur.execute("DROP TABLE Jobs")
    cur.execute("CREATE TABLE Jobs(Id INT, Uid INT, Profession TEXT)")
    cur.execute("INSERT INTO Jobs VALUES(1,1,'Scientist')")
    cur.execute("INSERT INTO Jobs VALUES(2,2,'Marketeer')")
    cur.execute("INSERT INTO Jobs VALUES(3,3,'Developer')")


