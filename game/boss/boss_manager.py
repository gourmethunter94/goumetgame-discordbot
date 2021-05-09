# power: 130 - rating: 1088.98624
# power: 150 - rating: 1444.86295
# power: 170 - rating: 1843.13724
# power: 190 - rating: 2308.19679
# power: 210 - rating: 2807.44932
# power: 230 - rating: 3363.10488

class BossManager:
    def __init__(self, randomizer):
        self.randomizer = randomizer
        self.bosses = [
            Boss( "Burger Kong", 8, 2, 5, [
                    "throws a burger at &!player!&!",
                    "yells McFeast!",
                    "hurls spinning burger that kills &!player!& in real life!",
                    "dips french fry in mayonnaise!"
                ], [
                    'says, "Omae no namae wa Burger Kong de wa nai!"',
                    'retaliates by yelling, "Nugget Attack!"',
                    'yells, "Activating Phase 3!"',
                    'says "Hesburger has better mayonnaise than McDonalds!"'
                ], self.randomizer
            ),
            Boss( "Pesto Pasta", 33, 2, 5, [
                    'yells, "Carbonara Attack!"',
                    'yells, "Kingis Kongis!"',
                    'attacks &!player!& with spaghetti lasso!',
                    "shoots penne pasta at &!player!& with it's PenneBazooka!"
                ], [
                    'shouts, "Bolognese Power," and looks at you angrily!',
                    "kills all it's enemies in it's imagination!",
                    'gets really angry!',
                    'tries to prepare "Explosion Nuke Attack 5", but realizes it does not have such a thing!'
                ], self.randomizer
            ),
            Boss( "Sprite Overlord", 57, 3, 5, [
                    'uses "Citrus Fresh Breeze" to attack &!player!&!',
                    'summons pepsi man! to fight!',
                    'thinks it gets a stacking rage buff when it attacks!',
                    'uses "Galaxy Destruction Beam Ultimate form" to attack &!player!&!'
                ], [
                    'falls asleep!',
                    'tries to use "Multiverse Bomb Slayer Counter" but fails!',
                    'gets a headache!',
                    'yells "Baka-yaro!"'
                ], self.randomizer
            ),
            Boss( "MiHoYo's CEO", 100, 3, 10, [
                    'pulls attack from Gacha game to attack &!player!&!',
                    'throws a credit card at &!player!&!',
                    'summons the president of Sony to fight against &!player!&!',
                    'hits &!player!& with a golf club!'
                ], [
                    "tries to decrease &!player!&'s pull rate by 50 percent but fails!",
                    'fires &!player!& from the company!',
                    "doesn't know so he throws something at &!player!&!",
                    'eats his own papers!'
                ], self.randomizer
            ),
            Boss( "Postman", 140, 4, 10, [
                    'insults you from the letter box!',
                    "opens &!player!&'s mail and reads them out loud.",
                    'yells "You have important mail &!player!&," and then proceeds to eat the mail!',
                    'delivers &!player!& a letter bomb!',
                    'yells "Come open the door you fucking shit head!"'
                ], [
                    "delives &!player!&'s mail to &!player!&'s neighbour!",
                    "writes hatemail on the &!player!&'s name and delivers them to the &!player!&'s neighbours!",
                    "delivers &!player!&'s mail a week late!",
                    "delivers extreme amount of advertisements to &!player!&!"
                ], self.randomizer
            ),
            Boss( "Galaxy Master", 247, 4, 10, [
                'shoots &!player!& with a gun, but it is a space gun!',
                'puts on meteorite armour and shoots &!player!& with free space gun shots!',
                'tries to convince &!player!& that his character design is original!',
                'uses force lightning!' 
                ], [
                'shouts, "Very limited power!"',
                "just doesn't remember.",
                'just like... beats up everyone around himself with like... godly powers.',
                'eats some pesto pasta.'
            ], self.randomizer),
            Boss( "Trashcan", 323, 5, 15, [
                'eats some garbage... meaning it eats &!player!&!',
                'puts &!player!& in the trashcan!',
                "tries to eat &!player!& but has to spit them out since they taste too disgusting!",
                "does trashcan things." 
                ], [
                'is a trashcan!',
                'spills out trash all over the place!',
                'eats some delicious trashfood!',
                'realizes it is a trash can and gets depressed!'
            ], self.randomizer),
            Boss( "League of Legends Player", 520, 5, 15, [
                'spam mastery 7 emote at &!player!&',
                'writes lots of questionmarks in the chat!',
                'asks &!player!& to surrender!',
                'critically hits &!player!& 15 times in a row with 1 percent crit chance!'
                ], [
                'blames his jungler!',
                'starts shouting at his team mates in all chat.',
                'wants to 9x all his whole team!',
                'blames the lag!'
            ], self.randomizer),
            Boss( "Big Boi", 780, 6, 15, [
                'is a very big boi!',
                "does some big boi things to &!player!&'s face!",
                "eats some snow and then spits it at &!player!&'s face!",
                "farts in &!player!&'s general direction!"
                ], [
                'throws a tantrum!',
                "eats some pesto pasta but doesn't like it and starts crying!",
                "goes to cry to his mommy!",
                "changes his own diapers!"
            ], self.randomizer),
            Boss( "Burger Boi", 2166, 8, 25, [
                "doesn't even know.",
                'is silent.',
                'smirks scornfully, and eats 15 cheese burger babies.',
                'sends his henchmen from McDonalds after &!player!&!'
            ],[
                'is amateur putter.',
                'asks, "is that even a five start roll?"',
                "fucking dies of food poisoning because his burgers were actually syrgers.",
                "cries tears of burger sauce."
            ], self.randomizer),
            Boss( "Pepsi Max Can", 2888, 9, 30, [
                'sprays pepsi all over &!player!&!',
                'summons 13 legions of pepsi demons to attack &!player!&!',
                "shuts down &!player!&'s computer!",
                "cries pepsi tears that deal over 16 million dps. The attacks name is 'yhyy yhyy'!"
            ], [
                "doesn't even form any yeast foam!",
                "tells &!player!&'s mother that &!player!& attacked it!",
                "gives &!player!& life time pepsi max ban.",
                "buys RP with 20€."
            ], self.randomizer),
            Boss( "Gourmet Hunter", 3686, 10, 50, [
                'uses the power of eternal gourmet grace; "Gourmet Thousand Year Fever!"',
                "summons the gourmet legions to destroy &!player!&!",
                "eats some buff food and gains 15 million attack power and hits &!player!& on the face.",
                "destroys 13 galaxies via exessive foraging and then cooks powerfull buff food to defeat the evil &!player!&!"
            ], [
                "goes to cry in a corner after failing to cook good food.",
                "tosses himself in a trashcan with his failed cooking creation.",
                "tries to sustain his gourmet power with filthy cheeseburger but it's not enough.",
                "eats baked beans."
            ], self.randomizer),
            Boss( 'Gourmet "Ultra Mega Special" Hunter', 7372, 12, 90, [
                'uses the power of the true eternal gourmet grace; "Gourmet Ten Thousand Year Mega Fever!"',
                "summons the 13 gourmet legions to destroy &!player!&!",
                "eats some deluxe buff food and gains 155 million attack power and hits &!player!& on the face ten times.",
                "destroys 133 galaxies via extremely exessive foraging and then cooks super powerfull buff food to defeat the extremely evil &!player!&!"
            ], [
                "goes to cry in a corner after failing to cook even remotely good food.",
                "tosses himself in an extremely large trashcan with his very failed cooking creation.",
                "tries to sustain his gourmet power with extremely filthy cheeseburger but it's not nearly enough.",
                "eats ten cans of baked beans."
            ], self.randomizer),
            Boss ( 'Gourmet "The True God of Food" Hunter', 14742, 13, 125, [
                'pulls out an AK-47 and shoots &!player!& to death, yelling "This is my true power!"',
                "sends cross-continential ballistic missile at &!player!&'s IRL home!",
                "breaks &!player!& like a kit-kat bar!",
                "eats cheese burger!",
                "shows off his 3-Michelin :star: restaurants menu to &!player!&!",
                "uses attack that can't be explained with words so we're now using images, :point_up: :skull_crossbones: :rofl:"
            ], [
                "is actually dead for good.",
                "eats fifteen-hundred cheese burgers to cheer himself up!",
                "cooks some pesto-pasta!",
                "puts some of those uMaam's in his food to cheer himself up after nearly dying!",
                "goes to China to eat some dog meat, but is put to prison since that is illegal now!",
                'yells, "I am the gods be damned admin of this game!? How am I losing!?"'
            ], self.randomizer),
            Boss ( 'Gourmet "The True God of Food" Hunter, "The True Final Form"', 29484, 14, 165, [
                'pulls out two AK-47 and shoots &!player!& to death, yelling "This is my truest power!"',
                "sends cross-dimensional ballistic missile at &!player!&'s IRL home!",
                "breaks &!player!& like a kit-kat bar!",
                "eats double cheese burger!",
                "shows off his 4-Michelin :star: restaurants menu to &!player!&!",
                "uses attack that can't be explained with words so we're now using images, :point_up: :skull_crossbones: :rofl:",
                'Says, "Omae no inochi wa mou owatta", and kills &!player!&!'
            ], [
                "is actually dead for good.",
                "eats sixteen-hundred double cheese burgers to cheer himself up!",
                "cooks some pesto-pasta!",
                "puts some of those uMaam's in his food to cheer himself up after nearly dying!",
                "goes to China to eat some dog meat, but is put to prison since that is illegal now!",
                'yells, "I am the gods be damned admin of this game!? How am I losing!?"',
                "realizes the food he was eating is actually poisoned!"
            ], self.randomizer),
            Boss ( 'Gourmet "The True God of Food" Hunter, "The Truer Final Form"', 58968, 15, 180, [
                'pulls out three AK-47 and shoots &!player!& to death, yelling "This is my truester power!"',
                "sends cross-omni-dimensional ballistic missile at &!player!&'s IRL home!",
                "breaks &!player!& like a kit-kat bar!",
                "eats triple cheese burger!",
                "shows off his 5-Michelin :star: restaurants menu to &!player!&!",
                "uses attack that can't be explained with words so we're now using images, :point_up: :skull_crossbones: :rofl:"
                'Says, "Omae no inochi wa mou owatta", and kills &!player!&!',
                "Orders his foodora driver minions to driver over &!player!&!"
            ], [
                "is actually dead for good.",
                "eats seventeen-hundred triple cheese burgers to cheer himself up!",
                "cooks some pesto-pasta!",
                "puts some of those uMaam's in his food to cheer himself up after nearly dying!",
                "goes to China to eat some dog meat, but is put to prison since that is illegal now!",
                'yells, "I am the gods be damned admin of this game!? How am I losing!?"',
                "realizes the food he was eating is actually poisoned!",
                "chokes on the food he was eating!"
            ], self.randomizer),
            Boss ( 'Gourmet "The True God of Food" Hunter, "The Truest Final Form"', 117936, 16, 195, [
                'pulls out four AK-47 and shoots &!player!& to death, yelling "This is my truestest power!"',
                "sends omnipresent god-like ballistic missile at &!player!&'s IRL home!",
                "breaks &!player!& like a kit-kat bar!",
                "eats quadruple cheese burger!",
                "shows off his 666-Michelin :star: restaurants menu to &!player!&!",
                "uses attack that can't be explained with words so we're now using images, :point_up: :skull_crossbones: :rofl:"
                'Says, "Omae no inochi wa mou owatta", and kills &!player!&!',
                "Orders his foodora driver minions to driver over &!player!&!",
                "Poisons &!player!&'s food!"
            ], [
                "is actually dead for good.",
                "eats eighteen-hundred quadruple cheese burgers to cheer himself up!",
                "cooks some pesto-pasta!",
                "puts some of those uMaam's in his food to cheer himself up after nearly dying!",
                "goes to China to eat some dog meat, but is put to prison since that is illegal now!",
                'yells, "I am the gods be damned admin of this game!? How am I losing!?"',
                "realizes the food he was eating is actually poisoned!",
                "chokes on the food he was eating!",
                "starves since he doesn't have any food remaining!"
            ], self.randomizer),
            Boss ( 'Tom Nook', 235872, 17, 210, [
                'gives you a house and makes you pay for it!"',
                "calls you trash and says he can't accept trash!",
                "forces his children to work for him while he takes a vacation!",
                "adds five million bells to your debt!",
                "identifies your white shark as sea bass.",
                "forces you to watch Isabell's morning routine.",
                "snookers &!player!&!"
            ], [
                "decides &!player!& must shop at re-tail instead, but &!player!& shops where &!player!& fucking wants to.",
                "buys a forgery from crazy Redd!",
                "can't find Timmy and Tommy and has to do some actual work!",
                "runs into Tortimer and has to pay his rent!",
                "fails to sell you on Nook Miles!",
                'fails to sell his turnips in time and loses five million bells!',
                "explodes!",
                "tries to claim his right to shoot &!player!& if he wants to, but &!player!& shoots him first!",
                "starts his isekai adventure with a little help from &!player!&!",
                "time travels and gets Resetti'd!"
            ], self.randomizer)
        ]

        self.event_bosses = {
            "pirates" : Boss( "Strawface Pirates", 140, 4, 5, [
                "send their captain **Nibjwt S. Kyddt** to punch &!player!&!",
                "send their swordsman **Eieibiä Miei** to slice &!player!&!",
                "send their navigator **Bänu** to steal all &!player!&'s money!",
                "send their cook **Qubanijw Aäbhu** to kick &!player!&!",
            ], [
                'panic as their ship starts to sink!"',
                'just stand and watch as **Ribt Rbit Xgioowe** does a silly dance with chopstick stuck on his nose.',
                "send their captain **Nibjwt S. Kyddt** to punch &!player!&, but he falls in to the ocean and drowns.",
                "send their swordsman **Eieibiä Miei** to slice &!player!&, but his sword is made out of sausages.",
                "send their navigator **Bänu** to steal all &!player!&'s money, but she navigates herself into a trashcan!",
                "send their cook **Qubanijw Aäbhu** to kick &!player!&, but he gets kicked out of the discord server!",
                "try escape with **Debjt**'s magnificent cola cannon motor."
            ], self.randomizer),
            "megalodon" : Boss( "Megalodon", 323, 5, 10, [
                "sneaks up on &!player!& and takes a bite!",
                "__dun dun dun dun__'s behind &!player!&!",
                "grows feet and turns into a street shark to punch &!player!& in the face!",
                "rams the ship &!player!& is on!",
            ], [
                'takes heavy damage!"',
                'embarasses itself!"',
                'realizes it is on sweet water and panics!"',
                'takes a drink if sea water!"'
            ], self.randomizer)
        }

        self.missing_no = Boss( "MissingNo", 999999999, 999999999, 1, [
            "kills &!player!&!"
        ], [
            'is confused!"',
        ], self.randomizer)

    def fight_boss(self, boss_id, player_name, attack_method, power, special_attack_text=None):
        hit_points = 3
        reward = 0
        if boss_id.__class__ == int:
            boss = self._get_boss(boss_id)
        else:
            boss = self._get_event_boss(boss_id)
        if boss != None:
            lives = boss.lives
            msg = "**" + player_name + "** begins a fight against the **" + boss.name + "**!"
            difficulty = boss.difficulty
            while True:
                attack = attack_method(power)
                if special_attack_text:
                    rand = self.randomizer.randint(1,10)
                    if rand <= 2:
                        attack = attack * 2
                        msg += "\n\n**" + player_name + "** uses their special attack; **" + special_attack_text + "**, unleashing power level of **" + str(attack) + "** against difficulty rating of **" + str(difficulty) + "**!"
                    else:
                        msg += "\n\n**" + player_name + "** clashes power level of **" + str(attack) + "** against difficulty rating of **" + str(difficulty) + "**!"
                else:
                    msg += "\n\n**" + player_name + "** clashes power level of **" + str(attack) + "** against difficulty rating of **" + str(difficulty) + "**!"
                if attack >= difficulty:
                    lives = lives - 1
                    msg += "\n" + boss.get_hit(player_name) + " - **" + boss.name + "** has **" + str(lives) + "** hit points remaining!"
                    if lives == 0:
                        reward = boss.reward
                        msg += "\n\n**" + player_name + "** has defeated **" + boss.name + "**!"
                        break
                else:
                    hit_points = hit_points - 1
                    msg += "\n" + boss.get_attack(player_name) + " - **" + player_name + "** has **" + str(hit_points) + "** hit points remaining!"
                    if hit_points == 0:
                        msg += "\n\n**" + player_name + "** has been defeated by **" + boss.name + "**!"
                        break
        else:
            msg = "**" + player_name + "** has defeated all the available bosses!"
        return msg, reward

    def _get_boss(self, tier):
        if tier < len(self.bosses) and tier >= 0:
            return self.bosses[tier]
        else:
            return None
    
    def _get_event_boss(self, name):
        boss = self.event_bosses.get(name)
        if boss == None:
            boss = self.missing_no
        return boss

class Boss:
    def __init__(self, name, difficulty, lives, reward, attacks, hits, randomizer):
        self.name = name
        self.difficulty = difficulty
        self.lives = lives
        self.reward = reward
        self.attacks = attacks
        self.hits = hits
        self.randomizer = randomizer
    
    def get_attack(self, player_name):
        return self._solve_sentence(self.randomizer.choice(self.attacks), player_name)
    
    def get_hit(self, player_name):
        return self._solve_sentence(self.randomizer.choice(self.hits), player_name)
    
    def _solve_sentence(self, sentence, player_name):
        return "**" + self.name + "** " + sentence.replace("&!player!&", ("**" + player_name + "**"))
    
