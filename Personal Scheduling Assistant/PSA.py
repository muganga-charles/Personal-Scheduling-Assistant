from cs50 import SQL
database = SQL("sqlite:///Events.db")

def createDatabase():
   
    
    database.execute("CREATE TABLE categories (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)")
    database.execute("CREATE TABLE events (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, category_id INTEGER NOT NULL, start_time TEXT NOT NULL, end_time TEXT NOT NULL, status TEXT NOT NULL ,FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE)")

def addCategory(name):
    category_names = database.execute("SELECT name FROM categories")
    category = []
    for category_name in category_names:
        category.append(category_name["name"])

    if name not in category:
        database.execute("INSERT INTO categories (name) VALUES (?)", name)


def addEvent(name, category, start_time, end_time,status):
    database.execute("INSERT INTO events (name, category_id, start_time, end_time, status) VALUES (?, (SELECT id FROM categories WHERE name = ?), ?, ?, ?)", name, category, start_time, end_time, status)

def getCategories():
    work = database.execute("SELECT name FROM categories")
    categories = []
    for category in work:
        categories.append(category["name"])
    for i in range(len(categories)):
        print(categories[i].capitalize())

def getEvents():
    return database.execute("SELECT * FROM events")

def deleteCategory(name):
    database.execute("DELETE FROM categories WHERE name = ?", name)

def deleteEvent(category,name):
    database.execute("DELETE FROM events WHERE name = ? and category_id = (SELECT id FROM categories WHERE name = ?)",name ,category)

def markAsFinished(name,category):
    status = "TRUE"
    database.execute("UPDATE events SET status = ? WHERE name = ? and category_id = (SELECT id FROM categories WHERE name = ?)",status , name,category)
    print("Event marked as finished successfully")

def getOverdueEvents():
    return database.execute("SELECT * FROM events WHERE status = 'TRUE'")

def getPendingEvents():
    return database.execute("SELECT * FROM events WHERE status = 'FALSE'")

def validEvent(category,name):
    category_id = database.execute("SELECT id FROM categories WHERE name = ?",category)
    #check if the event exists
    for i in getEvents():
        if i["name"] == name and i["category_id"] == category_id[0]["id"]:
            return True
    return False
def PrintEvents():
    for i in getEvents():
        print(i["name"])

def upcommingEvents():
    for i in getEvents():
        if i["status"] == "FALSE":
            print(i["name"] + " is due on " + i["end_time"])
        
def overDueEvents():
    for i in getEvents():
        if i["status"] == "TRUE":
            print(i["name"] + " is expired on " + i["end_time"])

def editEvent(category,name,start_time,end_time,name1):
    database.execute("UPDATE events SET name = ?, category_id = (SELECT id FROM categories WHERE name = ?), start_time = ?, end_time = ? WHERE id = (SELECT id FROM events WHERE name = ?)", name, category, start_time, end_time,name1)
def main():
    getCategories()
    getEvents()
main()
