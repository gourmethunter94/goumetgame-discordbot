import sqlite3
import datetime
import random
from contextlib import closing
import game.adventure.adventure_manager as adventure_manager # pylint: disable=no-name-in-module,import-error
import game.boss.boss_manager as boss_manager # pylint: disable=no-name-in-module,import-error
import game.fishing.fishing_manager as fishing_manager # pylint: disable=no-name-in-module,import-error
#connection = sqlite3.connect("database.db")
#cursor = connection.cursor()
#cursor.execute('SELECT * FROM users WHERE user_id="asd"')
#print(cursor.fetchone()==None)
#cursor.execute('CREATE TABLE users (user_id TEXT, last_played TEXT, plays_left INTEGER, currency INTEGER, power INTEGER)')
#UPDATE users SET power="51" WHERE user_id="132843182965653513"

class Database:

    def __init__(self, address):
        self.address = address
        self.date = datetime.datetime
        self.randomizer = random.Random()
        self.enemies = ["the Aqua", "the Lin", "the Nepnep", "the Sawakoji", "the Karin", "the Konakon", "the Chiku", "that guy from mafia", "the Team Rocket", "the Gary Oak", "the Red", "the Alluusio", ",the P0k5", "a Prinny", "a Shroomish", "a Dude", "the Gourmet", "a Golbat", "the Hieno", "the Sana", "a Sanamon", "the Kumiperuna", "the Ukkounen!", "some League of Legends Tilt", "the Rito Freak", "the Riot Phreak", "the Gen Sin Simp Pact", "the Paimon", "an Emergency Food", "your mom", "a Magikarp", "the darkness", "the everlasting empty void of nothingness", "a Bulbasaur", "a Charmander", "a Squirtle"]
        self.roll_1 = ["Paimon", "Debate Clubi", "Trash", "Stick", "Pebble", "4* Character after already having c6", "5* Character after already having c6", "Random Blue Meteor", "19 Resin", "159 Primogems", "Tomato", "Digimon", "$9 USD", "Gray Parse", "Nothing", "spam mail", "Artifact with wrong main stats", "Moldy Bread", "Diet Water", "DVD Rewinder"]
        self.roll_2 = ["Dagger", "Sword", "4* Character", "Random Purple Meteor", "PlayStation 5", "X-Box 360", "99$ USD", "iPhone"]
        self.roll_3 = ["Gun", "5* Character", "Random Golden Meteor", "Nintendo Switch", "AK-47", "999$ USD"]
        self.roll_4 = ["Venttiili", "Tortellino", "MewOne", "MewThree"]
        self.roll_5 = ["Dilukki", "MewTwo"]
        self.roll_table = self.roll_1*10 + self.roll_2*6 + self.roll_3*3 + self.roll_4*2 + self.roll_5
        self.adventure = adventure_manager.AdventureManager(self.randomizer)
        self.bosses = boss_manager.BossManager(self.randomizer)
        self.fish = fishing_manager.FishingManager(self.randomizer)
        self.plays_per_day = 3

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
    
    def add_extra_plays(self, player, amount):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('INSERT INTO extra_plays VALUES ("' + str(player) + '",' + str(amount) + ')')
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
    
    def edit_bosses(self, player, tier):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('UPDATE bosses SET last_attempt="' + str(self._get_date()) + '", tier=' + str(tier) + ' WHERE user_id="' + player + '"')
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

    def _get_date(self):
        return str(self.date.now()).split(" ")[0]

    def get_time_until_reset(self):
        current_time = str(datetime.datetime.now()).split(" ")[1].split(".")[0].split(":")
        hours = 23 - int(current_time[0])
        minutes = 60 - int(current_time[1])
        if minutes >= 60:
            hours += 1
            minutes = 0
        return "Time until reset: **" + str(hours) + " hours, " + str(minutes) + " minutes**!"

    def _random_enemy(self):
        return self.randomizer.choice(self.enemies)
    
    def update_player(self, player, plays_left, currency, power):
        if self.get_player(player):
            with closing(sqlite3.connect(self.address)) as connection:
                with closing(connection.cursor()) as cursor:
                    cursor.execute('UPDATE users SET last_played="' + self._get_date() + '", plays_left=' + str(plays_left) + ', currency=' + str(currency) + ', power=' + str(power) + ' WHERE user_id="' + player + '"')
                    connection.commit()
                    return True
        else:
            return False

    def play_adventure(self, player, nickname):
        message = ""
        last_adventure = self.get_adventure(player)
        if last_adventure == None or last_adventure[1] != self._get_date():
            if last_adventure == None:
                self.add_adventure(player)
            else:
                self.edit_adventure(player)
            player_data = self.get_player(player)
            if player_data == None:
                self.add_player(player)
                player_data = self.get_player(player_data)
            last_played = player_data[1]
            if last_played != self._get_date():
                plays_left = self.plays_per_day
            else:
                plays_left = int(player_data[2])
            currency = int(player_data[3])
            power = int(player_data[4])
            special = self.get_special(player)
            if special:
                special_attack_text = special[1]
            else:
                special_attack_text = None
            msg, monies, plays, baits = self.adventure.adventure(nickname, self._attack_roll, power, special_attack_text)
            message += msg
            currency += monies
            plays_left += plays

            if monies > 0 or plays > 0 or baits > 0:
                message += "\n"

            if monies > 0:
                message += "\n**" + nickname + "** gains **" + str(monies) + "** monies from the adventure!"
            if plays > 0:
                message += "\n**" + nickname + "** gains **" + str(plays) + "** extra plays for today from the adventure!"
            if baits > 0:
                message += "\n**" + nickname + "** gains **" + str(baits) + "** baits for fishing!"
                fishing_data = self.get_fishing(player)
                if fishing_data == None:
                    self.add_fishing(player, baits)
                else:
                    self.edit_fishing(player, (int(fishing_data[1]) + baits))
            message += "\n**" + nickname + "**'s adventure is at it's end. Adventure again tomorrow!"

            self.update_player(player, plays_left, currency, power)
        else:
            message += "**" + nickname + "** has adventured already today, adventure again tomorrow!"
            message += "\n" + self.get_time_until_reset()

        return message

    def play_bosses(self, player, nickname):
        message = ""
        last_boss = self.get_bosses(player)
        if last_boss == None or last_boss[1] != self._get_date():
            reward = 0
            if last_boss == None:
                self.add_bosses(player)
                boss_tier = 0
            else:
                boss_tier = int(last_boss[2])
            player_data = self.get_player(player)
            if player_data == None:
                self.add_player(player)
                player_data = self.get_player(player_data)
            last_played = player_data[1]
            if last_played != self._get_date():
                plays_left = self.plays_per_day
            else:
                plays_left = int(player_data[2])
            currency = int(player_data[3])
            power = int(player_data[4])
            special = self.get_special(player)
            if special:
                special_attack_text = special[1]
            else:
                special_attack_text = None
            msg, reward = self.bosses.fight_boss(boss_tier, nickname, self._attack_roll, power, special_attack_text)
            message += msg + "\n\n"

            if reward > 0:
                message += "**" + nickname + "** gains **" + str(reward) + "** monies for defeating the boss!"
                self.edit_bosses(player, boss_tier + 1)
            else:
                message += "**" + nickname + "** was defeated by the boss!"
                self.edit_bosses(player, boss_tier)

            self.update_player(player, plays_left, (currency+reward), power)
        else:
            message += "**" + nickname + "** has fought a boss already today, try again tomorrow!"
            message += "\n" + self.get_time_until_reset()

        return message

    def play(self, player, nickname):
        message = ""
        player_data = self.get_player(player)
        if player_data == None:
            self.add_player(player)
            player_data = self.get_player(player_data)
        last_played = player_data[1]
        if last_played != self._get_date():
            plays_left = self.plays_per_day
        else:
            plays_left = int(player_data[2])
        extra_plays_data = self.get_extra_plays(player)
        if extra_plays_data:
            extra_plays = int(extra_plays_data[1])
        else:
            extra_plays = 0
        if plays_left > 0 or extra_plays > 0:
            currency = int(player_data[3])
            power = int(player_data[4])
            enemy = self._random_enemy()
            message = "**" + nickname + "** encounters **" + enemy + "**!"
            attack = self._attack_roll(power)
            special = self.get_special(player)
            if special:
                chance = self.randomizer.randint(1,10)
                if chance <= 2:
                    message += "\n**" + nickname + "** uses special attack: **" + special[1] + "**!"
                    attack = attack * 2
            reward = max(1, int(1.295*len(str(attack)))) + self.randomizer.randint(0, 1) + max(0, self.randomizer.randint(0, max(1,int(len(str(power))/2))))
            message += "\n**" + nickname + "** impressed **" + enemy.replace("an ", "the ").replace("a ", "the ") + "** with power level of **" + str(attack) + "**!"
            currency += reward
            message += "\n**" + nickname + "** gains **" + str(reward) + "** monies as reward. Current total monies **" + str(currency) + "**!"
            if plays_left > 0:
                plays_left = max(0, plays_left - 1)
            else:
                extra_plays = max(0, extra_plays - 1)
                self.edit_extra_plays(player, extra_plays)
            message += "\n**" + nickname + "** has **" + str(plays_left) + "** plays left today!"
            message += "\n**" + nickname + "** has **" + str(extra_plays) + "** extra plays left!"
            self.update_player(player, plays_left, currency, power)
            rand = self.randomizer.randint(1,3)
            if rand == 1:
                baits = self.randomizer.randint(1, 2)
                fishing_data = self.get_fishing(player)
                if fishing_data == None:
                    self.add_fishing(player, baits)
                else:
                    self.edit_fishing(player, (int(fishing_data[1]) + baits))
                message += "\n**" + nickname + "** finds **" + str(baits) + "** baits!"

        else:
            message = "**" + nickname + "** doesn't have any plays left today!"
            message += "\n" + self.get_time_until_reset()
        return message
    
    def _attack_roll(self, power):
        return (1 + self.randomizer.randint(1, max(2, int(power/2)))) * max(1, int(power/4))
 
    def roll(self, player, nickname):
        message = ""
        player_data = self.get_player(player)
        if player_data == None:
            self.add_player(player)
            player_data = self.get_player(player_data)
        currency = int(player_data[3])
        if currency >= 5:
            currency -= 5
            plays_left = int(player_data[2])
            last_played = player_data[1]
            if last_played != self._get_date():
                plays_left = self.plays_per_day
            else:
                plays_left = int(player_data[2])
            power = int(player_data[4])
            item = self.randomizer.choice(self.roll_table)
            value = self._get_item_value(item)
            power += value
            message = "**" + nickname + "** spent **5** monies rolling and got... ** " + item + "** ( "
            for stars in range(0, value):
                message += ":star:"
            message += " )"
            message += "\nThe **" + item + "** increases **" + nickname + "'s** power by **" + str(value) + "**!"
            if power >= 50 and (not self.get_special(player)):
                message += "\n**" + nickname + "**'s power has reached above 50! Special attack has been unlocked!"
                self.add_special(player)
            self.update_player(player, plays_left, currency, power)
        else:
            message = "**" + nickname + "** doesn't have enough monies to roll!"
        return message
    
    def add_currency(self, currency):
        with closing(sqlite3.connect(self.address)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('UPDATE users SET currency=' + str(currency) + '+currency')
                connection.commit()

    def add_plays(self, plays):
        for player_id in self.get_players():
            extra_plays = self.get_extra_plays(player_id)
            if extra_plays:
                self.edit_extra_plays(player_id, (int(extra_plays[1])+plays))
            else:
                self.add_extra_plays(player_id, plays)

    def status(self, player, nickname):
        message = ""
        player_data = self.get_player(player)
        boss_status = self.get_bosses(player)
        adventure_status = self.get_adventure(player)
        if player_data == None:
            self.add_player(player)
            player_data = self.get_player(player_data)
        last_played = player_data[1]
        if last_played != self._get_date():
            plays_left = self.plays_per_day
        else:
            plays_left = int(player_data[2])
        if boss_status == None or boss_status[1] != self._get_date():
            boss_message = "\nA Boss fight is available today!"
        else:
            boss_message = "\nA Boss fight already fought today!"
        if adventure_status == None or adventure_status[1] != self._get_date():
            adventure_message = "\nAn Adventure is available today!"
        else:
            adventure_message = "\nAn Adventure already completed today!"
        currency = int(player_data[3])
        power = int(player_data[4])
        extra_plays = self.get_extra_plays(player)
        if extra_plays:
            extra_play_amount = extra_plays[1]
        else:
            extra_play_amount = 0
        baits = self.get_fishing(player)
        if baits:
            baits_amount = baits[1]
        else:
            baits_amount = 0
        message = "**" + nickname + "** has **" + str(plays_left) + "** plays left today, **" + str(power) + "** power and **" + str(currency) + "** monies!" + adventure_message + boss_message
        message += "\n**" + str(extra_play_amount) + "** extra plays left!"
        message += "\n**" + str(baits_amount) + "** fishing baits left!"
        message += "\n" + self.get_time_until_reset()
        return message

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

    def fishing(self, player, nickname, fish_all=False):
        message = ""
        fish_amount = 1
        amount_fished = 0
        fishing_data = self.get_fishing(player)
        if fishing_data == None:
            self.add_fishing(player, 0)
            message = "**" + nickname + "** doesn't have any bait for fishing!\nTo gain bait either play or do adventures!"
        elif int(fishing_data[1]) == 0:
            message = "**" + nickname + "** doesn't have any bait for fishing!\nTo gain bait either play or do adventures!"
        else:
            player_data = self.get_player(player)

            fish = []
            money = 0
            plays = 0

            if fish_all:
                fish_amount= fishing_data[1]

            for fishing in range(0, fish_amount):
                fish, money_instance, plays_instance = self.fish.fish()

                message += "**" + nickname + "** has caught something while fishing!\nIt is a " + fish
                
                amount_fished += 1

                if not fish_all:
                    if money_instance > 0:
                        message += "\nThe fish is worth **" + str(money_instance) + "** monies!"
                    if plays_instance > 0:
                        message += "\nThe fish is worth **" + str(plays_instance) + "** plays!"
                    if money_instance == 0 and plays_instance == 0:
                        message += "\nThe fish is not worth anything!"
                    message += "\n**" + nickname + "** has **" + str((int(fishing_data[1]) - amount_fished)) + "** baits remaining!"

                money += money_instance
                plays += plays_instance

                if fish_all:
                    message += "\n\n"

            last_played = player_data[1]
            if last_played != self._get_date():
                plays_left = self.plays_per_day + plays
            else:
                plays_left = int(player_data[2]) + plays
            currency = int(player_data[3]) + money
            power = int(player_data[4])

            if fish_all:
                message += "**" + nickname + "** got **" + str(money) + "** monies and **" + str(plays) + "** plays while fishing!"

            self.update_player(player, plays_left, currency, power)
            self.edit_fishing(player, (int(fishing_data[1]) - fish_amount))
        return message

    def _get_item_value(self, item):
        if item in self.roll_1:
            return 1
        elif item in self.roll_2:
            return 2
        elif item in self.roll_3:
            return 3
        elif item in self.roll_4:
            return 4
        elif item in self.roll_5:
            return 5
        return 0