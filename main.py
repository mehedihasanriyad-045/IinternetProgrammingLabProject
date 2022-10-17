from DatabaseMysql import DatabaseMysql
from DatabaseMysql import DatabaseMysql
from DatabaseSqlite import DatabaseSqlite
import json

def getDatabase(config, debug=False):
    # Gives mysql of sqlite database depending on the config specification
    database = None
    if(config["databaseToUse"] == "sqlite"):
        database = DatabaseSqlite(config["sqlite"], debug)
    else :
        database = DatabaseMysql(config["mysql"], debug)
    return database



# Main thread
if __name__ == "__main__":

    inp = None 
    
    with open('query_file.json', 'r') as f: # reads config from json file
        inp = json.load(f)

    # initiats a database
    # function returns a database depending on the config specification
    # sqlite / mysql

    database = getDatabase(inp["config"], debug=True)
    
    # Connects and executes queries needed
    database.connect()

    # inserts datas
    database.insert(inp["insert_queries"][0])
    database.insert(inp["insert_queries"][1])
    database.insert(inp["insert_queries"][2])

    # selects datas
    print(inp["select_query"])
    database.select(inp["select_query"])

    # updates datas
    database.update(inp["update_query"])

    # deletes datas
    database.delete(inp["delete_entry"])