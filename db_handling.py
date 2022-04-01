import sqlite3

conn = sqlite3.connect('/Users/rsi/github/initial_auto/initial.db')
c = conn.cursor()

def setMessage(type, code, message):
    c.execute('INSERT INTO initial VALUES(?,?,?,?);', (None, type, code, message))
    conn.commit()
    #conn.close()    

def selectCount():
    c.execute('select count(*) from initial')
    count = c.fetchone()[0]
    return count
    print (count)

def deleteMessage(code):
    c.execute('delete from initial where code= CODE', {"CODE":code})
    conn.commit()
    #conn.close()  

def deleteAllMessage():
    c.execute('delete from initial')
    conn.commit()
    #conn.close()  

def selectCode():
    c.execute('select code from initial')
    code = c.fetchone()[0]
    return code
    #print(code)


    
