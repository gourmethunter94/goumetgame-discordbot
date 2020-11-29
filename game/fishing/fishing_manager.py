class FishingManager:

    def __init__(self, randomizer):
        self.randomizer = randomizer
        self.money_fish = [
            Fish("Goldteeth Tetra", "It's scales match the hue of gold perfectly and shine the same way.", 2),
            Fish("Diamondfin Shark", "The tips of it's dorsal fin is hard as diamond.", 2),
            Fish("Rainbow Eel", "Especially long eel, it's colouration shifts through all the colours of the rainbow.", 1),
            Fish("Ghostfish", "It's otherworly glow gives it mystique, it is a rare delicacy.", 1),
            Fish("Cake Fish", "A peculiar fish whose meat is soft and sweet as a cake.", 1),
            Fish("Freakfish", "Pretty freakish.", 1),
            Fish("Godfish", "Angelfish's master, this fish thinks it is a god.", 1),
            Fish("Blue-redstripe Purplefish", "Very colourful!", 1)
        ]
        self.play_fish = [
            Fish("Seerfish", "Some say that eating the meat of this fish grants visions of the future.", 1),
            Fish("Dumbbell", "It is not a fish, but it can be used for training!", 1),
            Fish("Timmy's Pigeons", "They are not fish but you decided to grab some grub on the way to the lake.", 1),
            Fish("Surgeon", "The older brother of sturgeon!", 1)
        ]
        self.trash_fish = [
            Fish("Gourmet Fish", "It's name is misleading, the fish was named after Gourmet Hunter, it's worth nothing!"),
            Fish("Trash", "It's not even a fish..."),
            Fish("Boot", "You never seem to catch a matching pair..."),
            Fish("Joja Cola", "Some consider this thing poison."),
            Fish("Stick", "These things get stuck on the fishing line way too often."),
            Fish("Pickled Herring", "It has been out for so long it rotted."),
            Fish("Common Torpedo", "Not the fish, just ordinary common torpedo warhead."),
            Fish("Dud", "Someone seems to have tried to fish with explosives..."),
            Fish("Lauwiliwilinukunuku'oi'oi", "This fish actually exists."),
            Fish("Sturgeon", "Eh... it's edible."),
            Fish("Salmon", "Getting actual edible fish in this game is really rare.")
        ]
    
    def fish(self):
        rand = self.randomizer.randint(1, 100)
        money = 0
        plays = 0
        if rand  <= 8:
            fish = self.randomizer.choice(self.play_fish)
            plays = fish.value
        elif rand <= 40:
            fish = self.randomizer.choice(self.money_fish)
            money = fish.value
        else:
            fish = self.randomizer.choice(self.trash_fish)
        message = fish.get_name() + "\n" + fish.get_flavour()
        return message, money, plays

class Fish:

    def __init__(self, name, flavour, value=0):
        self.name = name
        self.flavour = flavour
        self.value = value
    
    def get_flavour(self):
        return "_" + self.flavour + "_"
    
    def get_name(self):
        return "**" + self.name + "**"