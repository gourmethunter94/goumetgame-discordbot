import datetime
import random
import game.adventure.adventure_manager as adventure_manager # pylint: disable=no-name-in-module,import-error
import game.boss.boss_manager as boss_manager # pylint: disable=no-name-in-module,import-error
import game.fishing.fishing_manager as fishing_manager # pylint: disable=no-name-in-module,import-error
import game.event.event_manager as event_manager # pylint: disable=no-name-in-module,import-error
import game.database.database as database # pylint: disable=no-name-in-module,import-error

class Game:

    def __init__(self, address, logger):
        self.date = datetime.datetime
        self.randomizer = random.Random()
        self.enemies = ["the Tarion", "a Chilled Bean", "the Aqua", "the Lin", "the Nepnep", "the Sawakoji", "the Karin", "the Konakon", "the Chiku", "that guy from mafia", "the Team Rocket", "the Gary Oak", "the Red", "the Alluusio", ",the P0k5", "a Prinny", "a Shroomish", "a Dude", "the Gourmet", "a Golbat", "the Hieno", "the Sana", "a Sanamon", "the Kumiperuna", "the Ukkounen!", "some League of Legends Tilt", "the Rito Freak", "the Riot Phreak", "the Gen Sin Simp Pact", "the Paimon", "an Emergency Food", "your mom", "a Magikarp", "the darkness", "the everlasting empty void of nothingness", "a Bulbasaur", "a Charmander", "a Squirtle", "Lominsan ERP Catgirl", "Bimbofication Gas of the Synth City"]
        self.roll_1 = ["Recycled Food", "Paimon", "Debate Clubi", "Trash", "Stick", "Pebble", "4* Character after already having c6", "5* Character after already having c6", "Random Blue Meteor", "19 Resin", "159 Primogems", "Tomato", "Digimon", "$9 USD", "Gray Parse", "Nothing", "spam mail", "Artifact with wrong main stats", "Moldy Bread", "Diet Water", "DVD Rewinder"]
        self.roll_2 = ["Dagger", "Sword", "4* Character", "Random Purple Meteor", "PlayStation 5", "X-Box 360", "99$ USD", "iPhone", "Green Parse"]
        self.roll_3 = ["Gun", "5* Character", "Random Golden Meteor", "Nintendo Switch", "AK-47", "999$ USD", "Blue Parse"]
        self.roll_4 = ["Venttiili", "Tortellino", "MewOne", "MewThree", "Ruben the Norwegian", "Chilled Beans", "Purple Parse"]
        self.roll_5 = ["Dilukki", "MewTwo", "Schlong Long", "Orange Parse"]
        self.adventure = adventure_manager.AdventureManager(self.randomizer)
        self.bosses = boss_manager.BossManager(self.randomizer)
        self.event_manager_instance = event_manager.EventManager(self.randomizer, self.bosses, self)
        self.fish = fishing_manager.FishingManager(self.randomizer)
        self.plays_per_day = 3
        self.database = database.Database(address, self.event_manager_instance, self.plays_per_day, self._get_date, logger)

    def get_player(self, player):
        return self.database.get_player(player)
    
    def get_players(self):
        return self.database.get_players()

    def get_special(self, player):
        return self.database.get_special(player)
    
    def update_nickname(self, player, nickname):
        self.database.update_nickname(player, nickname)

    def get_nicknames(self):
        return self.database.get_nicknames()

    def get_adventure(self, player):
        return self.database.get_adventure(player)

    def get_fishing(self, player):
        return self.database.get_fishing(player)
    
    def edit_fishing(self, player, amount):
        self.database.edit_fishing(player, amount)
    
    def add_fishing(self, player, amount):
        self.database.add_fishing(player, amount)

    def get_extra_plays(self, player):
        return self.database.get_extra_plays(player)
    
    def edit_extra_plays(self, player, amount):
        self.database.edit_extra_plays(player, amount)
    
    def add_extra_plays(self, player, amount):
        self.database.add_extra_plays(player, amount)

    def get_bosses(self, player):
        return self.database.get_bosses(player)

    def edit_adventure(self, player):
        self.database.edit_adventure(player)
    
    def edit_bosses(self, player, tier, edit_time=True):
        self.database.edit_bosses(player, tier, edit_time)

    def add_adventure(self, player):
        self.database.add_adventure(player)

    def add_bosses(self, player):
        self.database.add_bosses(player)

    def edit_nickname(self, player, nickname):
        self.database.edit_nickname(player, nickname)
    
    def add_nickname(self, player, nickname):
        self.database.add_nickname(player, nickname)

    def add_player(self, player):
        return self.database.add_player(player)
    
    def add_special(self, player):
        self.database.add_special(player)
    
    def edit_special(self, player, special_attack):
        self.database.edit_special(player, special_attack)

    def _add_event(self, player, event_name):
        self.database._add_event(player, event_name)
    
    def get_events(self, player):
        return self.database.get_events(player)

    def has_event(self, player, event_name):
        return self.database.has_event(player, event_name)

    def delete_event(self, player, event_name):
        self.database.delete_event(player, event_name)

    def _plays_left(self, player):
        return self.database._plays_left(player)
    
    def _last_played(self, player):
        return self.database._last_played(player)

    def _get_date(self):
        return str(self.date.now()).split(" ")[0]

    def update_player(self, player, plays_left, currency, power):
        return self.database.update_player(player, plays_left, currency, power)
    
    def add_currency(self, currency):
        self.database.add_currency(currency)
    
    def add_currency_to(self, currency, player):
        self.database.add_currency_to(currency, player)

    def add_plays(self, plays):
        self.database.add_plays(plays)

    def add_event(self, event_name):
        return self.databse.add_event(event_name)

    def leaderboard(self):
        return self.database.leaderboard()
    
    def get_finisher(self, player):
        return self.database.get_finisher(player)

    def update_finisher(self, player, finisher_name):
        self.database.update_finisher(player, finisher_name)

    def events(self, player, nickname):
        message = "**" + nickname + "** has the following events:\n"
        events = self.get_events(player)
        if len(list(events)) > 0:
            for event in list(events):
                message += "    **" + str(events.get(event)) + "** instances of **" + event + "** event!\n"
        else:
            message = "**" + nickname + "** has no events available!"
        return message

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

    def play_bosses(self, player, nickname, boss_token=False):
        message = ""
        last_boss = self.get_bosses(player)
        if last_boss == None or last_boss[1] != self._get_date() or boss_token:
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
            finishing_move_text = self.get_finisher(player)
            msg, reward = self.bosses.fight_boss(boss_tier, nickname, self._attack_roll, power, special_attack_text, finishing_move_text)
            message += msg + "\n\n"

            if reward > 0:
                message += "**" + nickname + "** gains **" + str(reward) + "** monies for defeating the boss!"
                self.edit_bosses(player, boss_tier + 1, not boss_token)
            else:
                message += "**" + nickname + "** was defeated by the boss!"
                self.edit_bosses(player, boss_tier, not boss_token)
            if not boss_token:
                self.update_player(player, plays_left, (currency+reward), power)
        else:
            message += "**" + nickname + "** has fought a boss already today, try again tomorrow!"
            message += "\n" + self.get_time_until_reset()

        if not boss_token:
            return message
        else:
            return message, reward

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
            rand = self.randomizer.randint(1,6)
            if rand == 1:
                self._add_event(str(player), "personaltrainer")
                message += "\n**" + nickname + "** gains access to **personaltrainer** event."

        else:
            message = "**" + nickname + "** doesn't have any plays left today!"
            message += "\n" + self.get_time_until_reset()
        return message
    
    def _attack_roll(self, power):
        return (1 + self.randomizer.randint(1, max(2, int(power/2)))) * max(1, int(power/4))
 
    def _roll(self):
        random_int = self.randomizer.randint(0, 100000)
        if random_int < 3000:
            return self.randomizer.choice(self.roll_5)
        elif random_int < 8000:
            return self.randomizer.choice(self.roll_4)
        elif random_int < 20000:
            return self.randomizer.choice(self.roll_3)
        elif random_int < 48000:
            return self.randomizer.choice(self.roll_2)
        else:
            return self.randomizer.choice(self.roll_1)

    def roll(self, player, nickname, roll_all):
        if roll_all:
            message = "**" + nickname + "** spends all their monies to roll!\n"
        else:
            message = ""
        player_data = self.get_player(player)
        if player_data == None:
            self.add_player(player)
            player_data = self.get_player(player_data)
        currency = int(player_data[3])
        if currency >= 5:
            if roll_all:
                rolls = int(currency / 5)
                currency = currency % 5
            else:
                rolls = 1
                currency -= 5
            plays_left = int(player_data[2])
            last_played = player_data[1]
            if last_played != self._get_date():
                plays_left = self.plays_per_day
            else:
                plays_left = int(player_data[2])
            power = int(player_data[4])
            base_power = power
            for _ in range(0, rolls):
                item = self._roll()
                value = self._get_item_value(item)
                power += value
                if roll_all == False:
                    message = "**" + nickname + "** spent **5** monies rolling and got... ** " + item + "** ( "
                else:
                    message += "\n**" + nickname + "** rolled and got... ** " + item + "** ( "
                for _ in range(0, value):
                    message += ":star:"
                message += " )"
                message += "\nThe **" + item + "** increases **" + nickname + "'s** power by **" + str(value) + "**!"
                if roll_all:
                    message += "\n"
            if roll_all:
                message += "\n**" + nickname + "**'s power increased by **" + str((power-base_power)) + "** in total!"
                average = (power-base_power) / rolls
                rate = average - 1.79
                message += "\nAverage power increase per pull was **" + str(average)[:7] + "** which was **" + str(rate)[:7] + "** ahead of average pull rate."
            if power >= 50 and (not self.get_special(player)):
                message += "\n**" + nickname + "**'s power has reached above 50! Special attack has been unlocked!"
                self.add_special(player)
            if power >= 400 and (not self.get_finisher(player)):
                message += "\n**" + nickname + "**'s power has reached above 400! Finishing move has been unlocked!"
                self.update_finisher(player, "Finisher Move")
            self.update_player(player, plays_left, currency, power)
        else:
            message = "**" + nickname + "** doesn't have enough monies to roll!"
        return message

    def event(self, player, nickname, event_name):
        message = ""
        if self.has_event(player, event_name):
            message, currency, plays, events = self.event_manager_instance.play_event(player, nickname, event_name)
            message += "\n\n**" + nickname + "** gains:"
            if plays > 0:
                extra_plays = self.get_extra_plays(str(player))
                if extra_plays:
                    self.edit_extra_plays(str(player), (int(extra_plays[1])+plays))
                else:
                    self.add_extra_plays(str(player), plays)
                message += "\n    **" + str(plays) + "** extra plays"
            if currency > 0:
                self.add_currency_to(currency, str(player))
                message += "\n    **" + str(currency) + "** monies"
            if len(events) > 0:
                for event in events:
                    self._add_event(str(player), event)
                    message += "\n    Access to **" + event + "** event"
            if len(events) == 0 and currency == 0 and plays == 0:
                    message += "\n    __Nothing__"
            self.delete_event(player, event_name)
        else:
            message = "**" + nickname + "** doesn't have access to the event: **" + event_name + "**!"
        return message

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
            events = []
            money = 0
            plays = 0

            if fish_all:
                fish_amount = fishing_data[1]

            for fishing in range(0, fish_amount):
                fish, money_instance, plays_instance, event = self.fish.fish()

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
                events = events + event

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

            if len(events) > 0:
                message += "\n\n**" + nickname + "** gains access to following events from fishing:"
                for event in events:
                    self._add_event(str(player), event)
                    message += "\n    Access to **" + event + "** event"

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