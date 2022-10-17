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

