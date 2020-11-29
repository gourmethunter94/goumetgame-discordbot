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
                'eats some garbage... meaning it eats !&player&!!',
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
            ], self.randomizer)
        ]

    def fight_boss(self, tier, player_name, attack_method, power, special_attack_text=None):
        hit_points = 3
        reward = 0
        boss = self._get_boss(tier)
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
                        msg += "\n\n**" + player_name + "** uses their special attack; **" + special_attack_text + "**, unleasing power level of **" + str(attack) + "** against difficulty rating of **" + str(difficulty) + "**!"
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
    
