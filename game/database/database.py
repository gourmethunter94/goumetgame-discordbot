
import sqlite3
from contextlib import closing

class Database:

    def __init__(self, address, event_manager_instance, _get_date):
        self.address = address
        self.event_manager_instance = event_manager_instance
        self._get_date = _get_date

    def get_player(self, player):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('SELECT * FROM users WHERE user_id="'+player+'"')
                return cursor.fetchone()
    
    def get_players(self):
        player_ids = []
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                for user_id in cursor.execute('SELECT * FROM users'):
                    player_ids.append(user_id[0])
        return player_ids

    def get_special(self, player):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('SELECT * FROM specials WHERE user_id="'+player+'"')
                return cursor.fetchone()
    
    def update_nickname(self, player, nickname):
        both = self.get_nicknames()
        nicknames = both[0]
        if player in nicknames:
            self.edit_nickname(player, nickname)
        else:
            self.add_nickname(player, nickname)

    def get_nicknames(self):
        userids = []
        nicknames = []
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                results = cursor.execute('SELECT * FROM nicknames')
                for row in results:
                    userids.append(str(row[0]))
                    nicknames.append(row) 
        return userids, nicknames

    def get_adventure(self, player):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('SELECT * FROM adventures WHERE user_id="' + player + '"')
                return cursor.fetchone()

    def get_fishing(self, player):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('SELECT * FROM fishing WHERE user_id="' + str(player) + '"')
                return cursor.fetchone()
    
    def edit_fishing(self, player, amount):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('UPDATE fishing SET baits=' + str(amount) + ' WHERE user_id="' + str(player) + '"')
                connection.commit()
    
    def add_fishing(self, player, amount):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('INSERT INTO fishing VALUES ("' + str(player) + '",' + str(amount) + ')')
                connection.commit()

    def get_extra_plays(self, player):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('SELECT * FROM extra_plays WHERE user_id="' + str(player) + '"')
                return cursor.fetchone()
    
    def edit_extra_plays(self, player, amount):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('UPDATE extra_plays SET amount=' + str(amount) + ' WHERE user_id="' + str(player) + '"')
                connection.commit()

    def get_bosses(self, player):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('SELECT * FROM bosses WHERE user_id="' + player + '"')
                return cursor.fetchone()

    def edit_adventure(self, player):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('UPDATE adventures SET last_adventure="' + str(self._get_date()) + '" WHERE user_id="' + player + '"')
                connection.commit()
    
    def edit_bosses(self, player, tier, edit_time=True):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                if edit_time:
                    time_string = 'last_attempt="' + str(self._get_date()) + '", '
                else:
                    time_string = ""
                cursor.execute('UPDATE bosses SET ' + time_string + 'tier=' + str(tier) + ' WHERE user_id="' + player + '"')
                connection.commit()

    def add_adventure(self, player):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('INSERT INTO adventures VALUES ("' + str(player) + '","' + str(self._get_date()) + '")')
                connection.commit()

    def add_bosses(self, player):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('INSERT INTO bosses VALUES ("' + str(player) + '","' + str(self._get_date()) + '",0)')
                connection.commit()

    def edit_nickname(self, player, nickname):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('UPDATE nicknames SET nickname="' + str(nickname) + '" WHERE user_id="' + player + '"')
                connection.commit()
    
    def add_nickname(self, player, nickname):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('INSERT INTO nicknames VALUES ("' + str(player) + '","' + str(nickname) + '")')
                connection.commit()

    def add_player(self, player):
        if self.get_player(player) == None:
            with closing(sqlite3.connect(self.address)) as connection:
                with closing(connection.cursor()) as cursor:
                    cursor.execute('INSERT INTO users VALUES ("' + player + '","' + self._get_date() + '", ' + str(self.plays_per_day) + ', 0, 6)')
                    connection.commit()
                    return True
        else:
            return False
    
    def add_special(self, player):
        if self.get_special(player) == None:
            with closing(sqlite3.connect(self.address)) as connection:
                with closing(connection.cursor()) as cursor:
                    cursor.execute('INSERT INTO specials VALUES ("' + player + '", "Special Attack")')
                    connection.commit()
    
    def edit_special(self, player, special_attack):
        if self.get_special(player):
            with closing(sqlite3.connect(self.address)) as connection:
                with closing(connection.cursor()) as cursor:
                    cursor.execute('UPDATE specials SET special_attack="' + str(special_attack) + '" WHERE user_id="' + player + '"')
                    connection.commit()

    def _add_event(self, player, event_name):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('INSERT INTO event VALUES ("' + str(player) + '", "' + event_name.lower() + '")')
                connection.commit()
    
    def get_events(self, player):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                events = {}
                for event in cursor.execute('SELECT * FROM event WHERE user_id="' + str(player) + '"'):
                    if events.get(event[1]):
                        events.update({event[1] : (events.get(event[1]) + 1)})
                    else:
                        events.update({event[1] : 1})
                return events

    def has_event(self, player, event_name):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('SELECT * FROM event WHERE user_id="' + str(player) + '" AND event_name="' + event_name.lower() + '"')
                return (cursor.fetchone() != None)

    def delete_event(self, player, event_name):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('DELETE FROM event WHERE rowid=(SELECT MIN(rowid) FROM event WHERE user_id="' + str(player) + '" AND event_name="' + event_name.lower() + '")')
                connection.commit()

    def _plays_left(self, player):
        player_data = self.get_player(player)
        if player_data:
            return player_data[2]
        else:
            return None
    
    def _last_played(self, player):
        player_data = self.get_player(player)
        if player_data:
            return player_data[1]
        else:
            return None
        
    def update_player(self, player, plays_left, currency, power):
        if self.get_player(player):
            with closing(sqlite3.connect(self.address)) as connection:
                with closing(connection.cursor()) as cursor:
                    cursor.execute('UPDATE users SET last_played="' + self._get_date() + '", plays_left=' + str(plays_left) + ', currency=' + str(currency) + ', power=' + str(power) + ' WHERE user_id="' + player + '"')
                    connection.commit()
                    return True
        else:
            return False
    
    def add_currency(self, currency):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('UPDATE users SET currency=' + str(currency) + '+currency')
                connection.commit()
    
    def add_currency_to(self, currency, player):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('UPDATE users SET currency=' + str(currency) + '+currency WHERE user_id="' + str(player) + '"')
                connection.commit()

    def add_plays(self, plays):
        for player_id in self.get_players():
            extra_plays = self.get_extra_plays(player_id)
            if extra_plays:
                self.edit_extra_plays(player_id, (int(extra_plays[1])+plays))
            else:
                self.add_extra_plays(player_id, plays)

    def add_event(self, event_name):
        if event_name in list(self.event_manager_instance.events):
            for player_id in self.get_players():
                self._add_event(player_id, event_name)
            return True
        else:
            return False

    def leaderboard(self):
        message = "**Global list of users sorted by power!**"
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                for row in cursor.execute('SELECT * FROM users LEFT JOIN nicknames ON users.user_id = nicknames.user_id ORDER BY users.power DESC'):
                    name = str(row[6])
                    power = str(row[4])
                    currency = str(row[3])
                    message += "\n      **" + name + "** with **" + power + "** power and **" + currency + "** monies."
        return message