class EventManager:
    def __init__(self, randomizer, boss_manager, game):
        self.randomizer = randomizer
        self.events = {
            "celebration":self._celebration,
            "pirates":self._pirates,
            "megalodon":self._megalodon,
            "weekend":self._weekend,
            "personaltrainer":self._personaltrainer,
            "mysteriousmap":self._mysterious_map
        }
        self._trainers = [
            ["Pekka Pouta", ["shares wisdom of the ancients with &!player!&.", "teaches &!player!& how the tell the weather.", "teaches some sick dance moves to &!player!&."], "his"],
            ["Dio Brando", ["tells &!player!& it's him, Dio.", "teaches &!player!& the secrets of stand and hamon.", "gives you some &!player!& food but was actually him, Dio!"], "his"],
            ["Tifa Lockhart", ["teaches &!player!& how to set up a nucklear bomb.", "gives &!player!& some home cooking and turns &!player!& into a fat boi.", "wants &!player!& to share their unemployment money."], "her"],
            ["Oyster Saucer", ["cooks some delicious oysters for &!player!&.", "doesn't know what to teach to &!player!&", "smells like umami."], "it's"],
            ["Rick Astley", ["is never gonna give &!player!& up!", "is never gonna let &!player!& go!", "is never gonna run around and desert &!player!&!"], "his"],
            ["Rick Astley", ["is never gonna make &!player!& cry!", "is never gonna say goodbye!", "is never gonna tell a lie and hurt &!player!&!"], "his"]
        ]
        self.boss_manager = boss_manager
        self.game = game
    
    def play_event(self, player, nickname, event_name):
        event = self.events.get(event_name)
        if event:
            return event(player, nickname)
        else:
            return "The event: **" + event_name + "** has not yet been implemented!", 0, 0, []
    
    def _mysterious_map(self, player, nickname):
        message = ""
        player_data = self.game.get_player(player)
        if player_data == None:
            self.add_player(player)
            player_data = self.game.get_player(player)
        power = int(player_data[4])
        special = self.game.get_special(player)
        if special:
            special_attack_text = special[1]
        else:
            special_attack_text = None
        msg, currency, plays, baits = self.game.adventure.adventure(nickname, self.game._attack_roll, power, special_attack_text)
        message += msg

        if baits > 0:
            message += "\n\n**" + nickname + "** gains **" + str(baits) + "** baits for fishing!"
            fishing_data = self.game.get_fishing(player)
            if fishing_data == None:
                self.game.add_fishing(player, baits)
            else:
                self.game.edit_fishing(player, (int(fishing_data[1]) + baits))
        message += "\n**" + nickname + "**'s *mysteriousmap* event adventure is at it's end.!"
    
        return message, currency, plays, []

    def _celebration(self, player, nickname):
        currency = 0
        events = []
        message = "**" + nickname + "** celebrates something, the atmosphere of the celebration fills you with **DETERMINATION**, you gain **1** extra play!"
        plays = 1
        return message, currency, plays, events
    
    def _pirates(self, player, nickname):
        message = "**" + nickname + "** hunts down a band of pirates terrorizing the seas!\n\n"
        msg, reward, plays, events = self._play_event_boss(player, nickname, "pirates")
        return message + msg, reward, plays, events
    
    def _megalodon(self, player, nickname):
        message = "**" + nickname + "** hunts terrible sea beast, Megalodon the ancient terror!\n\n"
        msg, reward, plays, events = self._play_event_boss(player, nickname, "megalodon")
        return message + msg, reward, plays, events
    
    def _weekend(self, player, nickname):
        currency = 5
        events = ["celebration"]
        message = "**" + nickname + "** Celebrates the end of the week, and begining of two days of freedom!"
        plays = 3
        return message, currency, plays, events

    def _play_event_boss(self, player, nickname, boss_name):
        message = ""
        reward = 0
        events = []
        player_data = self.game.get_player(player)
        if player_data == None:
            self.game.add_player(player)
            player_data = self.game.get_player(player_data)
        last_played = player_data[1]
        if last_played != self.game._get_date():
            plays_left = self.game.plays_per_day
        else:
            plays_left = int(player_data[2])
        currency = int(player_data[3])
        power = int(player_data[4])
        special = self.game.get_special(player)
        if special:
            special_attack_text = special[1]
        else:
            special_attack_text = None
        msg, reward = self.game.bosses.fight_boss(boss_name, nickname, self.game._attack_roll, power, special_attack_text)
        message += msg + "\n\n"

        if reward > 0:
            message += "**" + nickname + "** gains **" + str(reward) + "** monies for defeating the boss!"
        else:
            message += "**" + nickname + "** was defeated by the boss!"
        return message, reward, 0, events
    
    def _personaltrainer(self, player, nickname):
        reward = 0
        events = []
        power = int(self.game.get_player(player)[4])
        tokens = 0
        currency = 0
        plays = 0
        trainer = self.randomizer.choice(self._trainers)

        message = "**" + trainer[0] + "** shares " + trainer[2] + " wisdom with &!player!&.\n"

        for training in trainer[1]:
            message += "\n    **" + trainer[0] + "** " + training
            tokens += len(str(self.randomizer.randint(1, int(10000 + pow(power/6, max(1,power/21))))))
            message += "\n    &!player!& has gained total of **" + str(tokens) + "** training tokens from the lessons.\n"
        
        for _ in range(0, tokens):
            if self.randomizer.randint(1, 10) == 1:
                currency += 1

        currency = max(1, currency)

        message += "\n&!player!& exchanges **" + str(tokens) + "** training tokens to **" + str(currency) + "** monies."

        return self._solve_sentence(message, nickname), currency, plays, events

    def _solve_sentence(self, sentence, player_name):
        return sentence.replace("&!player!&", ("**" + player_name + "**"))
