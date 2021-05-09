import sqlite3
from contextlib import closing

class Logger:
    def __init__(self, address):
        self.address = address
    
    def write_entry(self, user_id, user_name, time, log_level, log_entry):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('INSERT INTO log_entry VALUES ("' + str(user_id) + '","' + str(user_name) + '","' + str(time) + '","' + str(log_level) + '","' + str(log_entry) + '")')
                connection.commit()