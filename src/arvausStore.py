store = []

def add(timestamp, username):
    store.append({timestamp: timestamp, username: username})

def clear():
    store = []
