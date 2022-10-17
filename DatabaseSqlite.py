from Abstarct_Database import Abstract_Database
import sqlite3
class DatabaseSqlite(Abstract_Database):
    def __init__(self, config, debug=False):
        self.config = config
        self.debug = debug
    
    def connect(self):
        query =  """
        CREATE TABLE IF NOT EXISTS users_statistics
            (id INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL,
            username           TEXT    NOT NULL UNIQUE,
            name            INT     NOT NULL,
            phone        VARCHAR(50)    NOT NULL);
    """
        self.conn = sqlite3.connect(self.config["filename"])
        self.execute(query)
        self.log("Openned")
    
    def close(self):
        self.conn.close()
        self.log("Closed")
    
    def execute(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            print(cursor.rowcount, "Record Inserted.")
            return cursor
        except sqlite3.IntegrityError as err:
            self.log("Error: {}".format(err))
            return None
        
    
    def insert(self, data):
        keys = [key for key in data.keys()];
        table_name  = data["table"]
        keys.pop(0)
        query = "INSERT INTO {} ({}) VALUES ({})".format(table_name,", ".join(keys), ", ".join(["'{}'".format(data[key]) for key in keys]))
        self.execute(query)   
    
    def select(self, data):
        table_name  = data["table"]
        query = ""
        if data["all"]:
            query = "SELECT * FROM {}".format(table_name)
        else:
            query = "SELECT {} FROM {}".format(", ".join(data["columns"]), table_name)
        if "where" in data.keys():
            for i in range(len(data["where"])):
                if(type(data["where"][i]["value"]) == str):
                    query += " WHERE {} {} '{}'".format(data["where"][i]["column"], data["where"][i]["operator"], data["where"][i]["value"])
                else:
                    query += " WHERE {} {} {}".format(data["where"][i]["column"], data["where"][i]["operator"], data["where"][i]["value"])
    
                    
        #print(query)
        cursor = self.conn.cursor()
        cursor.execute(query)

        res = cursor.fetchall()

        for row in res:
            print(row)

    def update(self, data):
        table_name  = data["table"]
        query = "UPDATE {} ".format(table_name)
        if "set" in data.keys():
            for i in range(len(data["set"])):
                if(type(data["set"][i]["value"]) == str):
                    query += "SET {} = '{}'".format(data["set"][i]["column"], data["set"][i]["value"])
                else:
                    query += "SET {} = {}".format(data["set"][i]["column"], data["set"][i]["value"])
                if i < len(data["set"]) - 1:
                    query += ", "
        if "where" in data.keys():
            for i in range(len(data["where"])):
                if(type(data["where"][i]["value"]) == str):
                    query += " WHERE {} {} '{}'".format(data["where"][i]["column"], data["where"][i]["operator"], data["where"][i]["value"])
                else:
                    query += " WHERE {} {} {}".format(data["where"][i]["column"], data["where"][i]["operator"], data["where"][i]["value"])
        
        print(query)
        self.execute(query)
    #sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
    def delete(self, data):
        table_name  = data["table"]
        query = "DELETE FROM {} ".format(table_name)
        if "where" in data.keys():
            for i in range(len(data["where"])):
                if(type(data["where"][i]["value"]) == str):
                    query += " WHERE {} {} '{}'".format(data["where"][i]["column"], data["where"][i]["operator"], data["where"][i]["value"])
                else:
                    query += " WHERE {} {} {}".format(data["where"][i]["column"], data["where"][i]["operator"], data["where"][i]["value"])
        
        print(query)
        self.execute(query)
