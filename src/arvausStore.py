import sqlite3


def getConnection():
    return sqlite3.connect('otamikki.db')

def init():
    connection = getConnection()
    cur = connection.cursor()
    cur.execute('CREATE TABLE answers (timestamp text, username text, answer text)')
    connection.commit()
    connection.close()

def add(timestamp, username, answer):
    connection = getConnection()
    cur = connection.cursor()
    cur.execute('INSERT INTO answers VALUES (?, ?, ?)', (timestamp, username, answer))
    connection.commit()
    connection.close()

def clear():
    # TODO
    pass

def getAll():
    connection = getConnection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM answers')
    result = cur.fetchall()
    connection.close()
    return result

def getWinners():
    # TODO
    pass
