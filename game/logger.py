import sqlite3
from contextlib import closing
import os

class Logger:
    def __init__(self, address, logger):
        self.address = address
        self.tables = [
            ("log_entry", "user_id TEXT, user_name TEXT, time TEXT, log_level TEXT, log_entry TEXT")
        ]
        self.write_tables(logger)
    
    def write_tables(self, logger):
        if not os.path.isfile(self.address):
            logger("Creating database: " + self.address, "5", "Logger Database", "System")
            for table in self.tables:
                try:
                    with closing(sqlite3.connect(self.address)) as connection:
                        with closing(connection.cursor()) as cursor:
                            cursor.execute("CREATE TABLE " + table[0] + "(" + table[1] + ");")
                            connection.commit()
                    logger("Building database table: " + table[0] + " - SUCCESS", "4", "Logger Database", "System")
                except:
                    logger("Building database table: " + table[0] + " - FAILURE : Suspected: Table already exists", "4", "Logger Database", "System")
        else:
            logger("Database: " + self.address + " already exists", "5", "Logger Database", "System")



    def write_entry(self, user_id, user_name, time, log_level, log_entry):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('INSERT INTO log_entry VALUES ("' + str(user_id) + '","' + str(user_name) + '","' + str(time) + '","' + str(log_level) + '","' + str(log_entry) + '")')
                connection.commit()