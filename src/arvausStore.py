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
    connection = getConnection()
    cur = connection.cursor()
    cur.execute('DELETE FROM answers')
    connection.commit()
    connection.close()

def getAll():
    connection = getConnection()
    cur = connection.cursor()
    cur.execute('SELECT * FROM answers')
    result = cur.fetchall()
    connection.close()
    return result

def getWinners():
    connection = getConnection()
    cur = connection.cursor()
    cur.execute('SELECT DISTINCT username FROM answers ORDER BY timestamp DESC LIMIT 5')
    result = cur.fetchall()
    connection.close()
    return result

