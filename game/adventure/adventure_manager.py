import random

class AdventureManager:

    def __init__(self, randomizer):
        self.randomizer = randomizer

        goblins = Entity("Goblin", [
            "Eerd", "Iabs", "Clurd", "Giats", "Trogz",
            "Plykozz", "Vaahekt", "Protmoisz", "Glybrozz", "Aatac",
            "Rienqea", "Khalkai", "Elx", "Gneld", "Flinqe",
            "Statiosxea", "Wrianuns", "Flaarynq", "Kleafurt", "Thimofs" ], [
            ("Warrior", ["waves &!hisher!& axe at &!player!&!", "threatens &!player!& with &!hisher!& sword!", "snarls at &!player!&!"]),
            ("Shaman", ["waves &!hisher!& staff at &!player!&!", "hurls foul smelling concoction at &!player!&!", "calls warriors of &!hisher!& tribe to attack &!player!&!"]),
            ("Berserker", ["roars at &!player!&!", "charges &!player!&!", "threatens &!player!& with &!hisher!& axe!"]),
            ("Archer", ["shoots an arrow at &!player!&!", 'conjures two magical blades from thin air and charges at &!player!&, yelling "I am the bone of my sword!"', "busts out some sweet sweet dance moves!"]),
            ("Pugilist", ["uses Dempsey Roll at &!player!&!!", "uses the legendary Gazelle Punch at &!player!&!", "launches a liver blow at &!player!&!"])
        ], self.randomizer)
        hobgoblins = Entity ("Hobgoblin", [
            "Shadreler", "Guvlorg", "Krolzur", "Zondor", "Dukvazag",
            "Nug", "Zrugrunol", "Dralvrol", "Khogal", "Venkug",
            "Luknar", "Luvorg", "Azrel", "Shoderz", "Mogor",
            "Rudrerz", "Grendrerz", "Glorded", "Zreroc", "Elzelur" ], [
            ("Warrior", ["waves &!hisher!& axe at &!player!&!", "threatens &!player!& with &!hisher!& sword!", "snarls at &!player!&!"]),
            ("Chief", ["orders &!hisher!& goblin warriors to attack &!player!&!", "calls for the goblin cavalry to charge at &!player!&!", "threatens &!player!& with &!hisher!& sword!"]),
            ("Berserker", ["roars at &!player!&!", "charges &!player!&!", "threatens &!player!& with &!hisher!& axe!"])
        ], self.randomizer)

        slimes = Entity("Slime", [
            "Rimuru", "Spattle", "Mucy", "Octo", "Joggle",
            "Slop", "Spatter", "Hopper", "Pokey", "Bean" ], [
            ("Ambusher", ["ambushes &!player!& with &!hisher!& special ambush technique!", "ambushes &!player!& from the shadows!", "launches an attack from the shadows!"]),
            ("Cube", ["turns transparent and waits for &!player!& to walk into it.", "falls on top of &!player!&!", "turns into a gamecube! &!player!& can't resist the urge to play games for hours!"]),
            ("Queen", ["divides to dozens of smaller slimes and surrounds &!player!&!", "creates several slime spawns to attack &!player!&!", "ambushes &!player!& with several of &!hisher!& spawns!"])
        ], self.randomizer, ["it"], {"it": "it's"})
        shadows = Entity("Shadow", [
            "Ss'zah", "Sh'doh", "Zh'bri", "Zz'sah", "Szah'el",
            "Sohh'al", "Sz'z'al", "Ss's'as", "Sl'ils", "Sus'pe" ], [
            ("Stalker", ["ambushes &!player!& from the... shadows!", "punches &!player!&'s shadow in the face... from the shadows!", "does some shady stuff!"]),
            ("Warrior", ["gets in an argument with &!player!&'s shadow!", "puts &!player!&'s shadow in full nelson!", "uses piledriver on &!player!&!"])
        ], self.randomizer, ["it"], {"it": "it's"})

        ranged_minion = Entity("Ranged Minion", [
            "Johan", "Stacy", "Jonathan", "Esquir", "Bob",
            "Ester", "Eleanor", "Jack", "Mack", "Edd",
            "Edward", "Joan", "Jace", "Kent", "Owen",
            "Oscar", "Oliver", "Alice", "Anne", "Andrew"], [
            ("Sharpshooter", ["snipes down &!player!& who was about to survive with 1 hit points!", "snipes down all of &!player!&'s lane minions!", "blocks &!player!&'s pathing!"]),
            ("General Annoyance", ["synchronizes &!hisher!& ranged attack with &!hisher!& fellow minions!", "changes target to another enemy minion for no reason!", "doesn't start attacking enemy champion when it attacks &!player!&!"])
        ], self.randomizer)

        melee_minions = Entity("Melee", [
            "Sean", "Alfred", "Chester", "Oakley", "Hallie",
            "Noah", "Leo", "Alfie", "Theo", "George",
            "Aurora", "Ivy", "Lisa", "Amelia", "Elsie",
            "Teddy", "Theodore", "Florence", "Harper", "Isla"], [
            ("Minion Path Blocker", ["blocks &!player!&'s pathing several times in a row!", "makes sure &!player!& gets stuck inside it's pathing!", "pushes &!player!& to path that will allow enemy team to do some pokes!"]),
            ("Minion", ["attacks &!player!& after &!player!& attacks a champion on &!hisher!& team!", "deals minimal amount of damage to &!player!&!", "steals one of &!player!&'s lane minion kills!"])
        ], self.randomizer)

        cannon_minions = Entity("Cannon", [
            "Howitzer", "Mortar", "Ordnance", "Big Bertha", "Long Tom", "Heavy Artillery"], [
            ("Minion", ["shoots at &!player!&'s tower!", "destroys &!player!&'s tower just before enemy team arrives for a gank!", "hits &!player!& with an attack, dealing like 25 damage!"])
        ], self.randomizer)

        limsa_erp = Entity ("Lominsan", [
            "Catgirl", "Catboy", "Hrothgar"], [
            ("ERP:er", ["call's &!player!& their mommy!", "snuggle wuggles &!player!&!", "hits on &!player!&!"])
        ], self.randomizer, ["it"], {"it": "it's"})

        limsa_afk = Entity ("Lominsan", [
            "Lalafell", "Hyur", "Au Ra"], [
            ("AFKer", ["is afk next to &!player!&!", "doesn't respond to &!player!&'s messages!", "get's booted from the server next to &!player!&!"])
        ], self.randomizer)

        self.locations = [
            Location("a Goblin Camp", [goblins, goblins, goblins, hobgoblins], ["Barracks", "Chief's Tent", "Arena", "Fight Pit", "loo", "captured ruins", "Shaman's Tent"], self.randomizer),
            Location("an Abandoned Dungeon", [slimes, shadows], ["Torture Chambers", "Deepest Dungeon", '"Waste" room', "solitary confinement cell", "Fight pit", "hidden entrance to the severs", "warden's office"], self.randomizer),
            Location("the Summoner's Rift", [ranged_minion, ranged_minion, melee_minions, melee_minions, cannon_minions], ["top lane", "mid lane", "bot lane", "blue team jungle", "red team jungle", "river", "red team base", "blue team base", "dragon pit", "baron pit"], self.randomizer),
            Location("Limsa Lominsa", [limsa_erp, limsa_afk], ["Market Board", "Side Bench", "Limsa Tree", "Abandoned Zone", "Blue Mage Starter Area", "Aetheryte", "Glitch Pillar"], self.randomizer)
        ]

        self.monie_rewards = [
            "a Common Treasure Chest", "a Exquisite Tresure Chest", "a Luxurious Treasure Chest",
            "a Bag of Goodies", "a Beautiful Gem", "some Shiny Coins",
            "a Diamond", "hundred-million USD", "999$",
            "a Golden Chocobo Feather", "a Silver Chocobo Feather", "an Allagan Tomestone of Poetics"
        ]

        self.play_rewards = [
            "a Hero's Wits", "a Hero's Experience", "a Hero's Advice",
            "an Allagan Tomestone of Phantasmagoria", "an Allagan Tomestone of Allegory", "an Allagan Tomestone of Revelation"
        ]
    
    def adventure(self, player_name, roll_method, power, special_attack_text=None):
        location = self.randomizer.choice(self.locations)
        message = "**The adventure starts!**\n**" + player_name + "** ventures to **" + location.name + "**!"
        monies = 0
        plays = 0
        baits = 0
        victories = 0
        defeats = 0
        turn = 0
        while True:
            rand = self.randomizer.randint(0, max(34, 42 - int(turn / 12)))
            if rand == 0:
                message += "\n\n" + location.treasure(player_name)
                message += "\n**" + player_name + "** found **" + self.randomizer.choice(self.play_rewards) + "**!"
                plays += 1
                message += "\n**" + player_name + "** gains **1** additional play for today!"
            elif rand < 6:
                message += "\n\n" + location.treasure(player_name)
                message += "\n**" + player_name + "** found **" + self.randomizer.choice(self.monie_rewards) + "**!"
                amount = self.randomizer.randint(1,2 + int(turn / 18))
                monies += amount
                message += "\n**" + player_name + "** gains **" + str(amount) + "** monies!"
            elif rand < 11:
                message += "\n\n" + location.treasure(player_name)
                fish_amount = self.randomizer.randint(2, 4 + int(turn / 14))
                baits += fish_amount
                message += "\n**" + player_name + "** found **" + str(fish_amount) + "** fish baits!"
            else:
                attack = roll_method(power)
                difficulty = (victories + 1) * max(1, int((victories+1)/2)) * 9 - 5
                if (power < 200 and power >= 4 * difficulty) or (power < 400 and power >= 2.5 * difficulty) or (power < 600 and power >= difficulty) or (power >= 600 and power >= difficulty * 0.5):
                    message += "\n**" + player_name + "** is too powerful and swats away any opposition with ease!"
                    defeated_status = False
                else:
                    if special_attack_text:
                        rand = self.randomizer.randint(1,10)
                        if rand <= 2:
                            attack = attack * 2
                            roll_text = "**" + player_name + "** uses special attack; **" + special_attack_text + "**, unleasing power level of **" + str(attack) + "** against difficulty rating of **" + str(difficulty) + "**!"
                        else:
                            roll_text = "**" + player_name + "** clashes power level of **" + str(attack) + "** against difficulty rating of **" + str(difficulty) + "**!"
                    else:
                        roll_text = "**" + player_name + "** clashes power level of **" + str(attack) + "** against difficulty rating of **" + str(difficulty) + "**!"
                    defeated_status = True
                    if attack >= difficulty:
                        defeated_status = False
                        victory = "defeats"
                    else:
                        victory = "is defeated by"
                    message += "\n\n" + location.adventure(player_name, roll_text, victory)
                if defeated_status:
                    if defeats == 2:
                        message += "\n**" + player_name + "** is defeated for the last time for this adventure!"
                        break
                    else:
                        defeats += 1
                        message += "\n**" + player_name + "** is defeated, **" + str((3-defeats)) + "** defeats left in this adventure!"
                else:
                    victories += 1
                    monies += 1 + int(turn / 10)
                turn += 1
        message += "\n\nThe adventure lasted **" + str(turn) + "** turns."
        return message, monies, plays, baits

class Entity:
    def __init__(self, race, names, types, randomizer, gender=None, hisher=None):
        self.randomizer = randomizer
        self.race = race
        self.names = names
        self.types = types
        if gender:
            self.gender = gender
            self.hisher = hisher
        else:
            self.gender = ["male", "female"]
            self.hisher = {"male":"his", "female":"her", "it": "it's"} 
    
    def _solve_sentence(self, sentence, player_name, gender, hisher):
        return sentence.replace("&!hisher!&", self.hisher.get(gender)).replace("&!player!&", ("**" + player_name + "**"))
    
    def _get_gender(self):
        return self.randomizer.choice(self.gender)
    
    def _get_hisher(self, gender):
        return self.hisher.get(gender)
    
    def _get_name(self):
        return self.randomizer.choice(self.names)

    def get_sentence(self, player_name):
        name = self._get_name()
        gender = self._get_gender()
        hisher = self._get_hisher(gender)
        sentence = self.randomizer.choice(self.types)
        return "**" + name + "** the " + self.race + " " + sentence[0] + " " + self._solve_sentence(self.randomizer.choice(sentence[1]), player_name, gender, hisher), name + " the " + self.race + " " + sentence[0]

class Location:
    def __init__(self, name, creatures, locations, randomizer, descriptions=None):
        self.name = name
        self.creatures = creatures
        self.randomizer = randomizer
        self.locations = locations
        if descriptions:
            self.descriptions = descriptions
        else:
            self.descriptions = [
                "a dirty",
                "rather large",
                "extremely wide",
                "adequately sized",
                "a beautiful",
                "a strange",
                "a blue",
                "an orange",
                "a green",
                "an yellow",
                "an overpopulated",
                "a dingy",
                "a damp",
                "a dank",
                "an ugly",
                "an old",
                "a recently built",
                "an overrated",
                "an uninteresting",
                "a dysfunctional",
                "an interesting",
                "quite sizable",
                "somewhat interesting",
                "kind of boring",
                "pretty cool",
            ]

    def adventure(self, player_name, roll_text, victory):
        location = self.randomizer.choice(self.locations)
        description = self.randomizer.choice(self.descriptions)
        creature_data = self.randomizer.choice(self.creatures).get_sentence(player_name)
        message = "**" + player_name + "** encounters **" + creature_data[1] + "** at **" + description + " " + location + "**!"
        message += "\n" + creature_data[0]
        message += "\n" + roll_text
        message += "\n**" + player_name + "** " + victory + " **" + creature_data[1] + "**!"
        return message
    
    def treasure(self, player_name):
        location = self.randomizer.choice(self.locations)
        description = self.randomizer.choice(self.descriptions)
        message = "**" + player_name + "** ventures to **" + description + " " + location + "**!"
        return message

    

