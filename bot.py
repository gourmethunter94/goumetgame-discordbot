import discord
import random
import game.game as game
import sys
import threading
import time
import datetime

arguments = sys.argv

settings_file = open("settings.txt", "r")
lines = settings_file.readlines()
TOKEN = lines[0]
ADMINS = []
for line in lines[1].split(","):
    ADMINS.append(int(line))
DATABASE_ADDRESS = lines[2]

class MyClient(discord.Client):

    def __init__(self):
        super().__init__()
        self._unregistered_commands = ["start", "chances", "leaderboard", "repository"]
        self._commands = {
            "play":self._play,
            "adventure":self._adventure,
            "pull":self._pull,
            "status":self._status,
            "chances":self._chances,
            "special":self._special,
            "boss":self._boss,
            "fish":self._fish,
            "event":self._event,
            "start":self._start,
            "chances":self._chances,
            "leaderboard":self._leaderboard,
            "repository":self._repository
        }
        self.ready = False

    async def _start(self, commands, message):
        if self.game_instance.get_player(str(message.author.id)) == None:
            self.game_instance.add_player(str(message.author.id))
            print("*** " + "Added " + str(message.author.id) + " to the game.")
            await self._send_message('**' + message.author.display_name + '** is now added to the game!', message.channel)
        else:
            await self._send_message('**' + message.author.display_name + '** was already added to the game!', message.channel)

    async def _play(self, commands, message):
        print("*** " + str(message.author.id) + " played the game.")
        await self._send_message(self.game_instance.play(str(message.author.id), message.author.display_name), message.channel)

    async def _adventure(self, commands, message):
        print("*** " + str(message.author.id) + " went to an adventure.")
        msg = self.game_instance.play_adventure(str(message.author.id), message.author.display_name)
        await self._send_message(msg, message.channel)

    async def _pull(self, commands, message):
        print("*** " + str(message.author.id) + " pulled.")
        if len(commands) >= 2 and commands[1] == "all":
            msg = self.game_instance.roll(str(message.author.id), message.author.display_name, True)
        else:
            msg = self.game_instance.roll(str(message.author.id), message.author.display_name, False)
        await self._send_message(msg, message.channel)

    async def _status(self, commands, message):
        await self._send_message(self.game_instance.status(str(message.author.id), message.author.display_name), message.channel)

    async def _chances(self, commands, message):
        await self._send_message('**Chances when pulling!**\n' +
                                   '    :star:; 52%\n' +
                                   '    :star::star:; 28%\n' +
                                   '    :star::star::star:; 12%\n' +
                                   '    :star::star::star::star:; 5%\n' +
                                   '    :star::star::star::star::star:; 3%' +
                                   'Average power increase per pull **1.79**.',
                                   message.channel)

    async def _leaderboard(self, commands, message):
        await self._send_message(self.game_instance.leaderboard(), message.channel)

    async def _special(self, commands, message):
        player = self.game_instance.get_player(str(message.author.id))
        player_id = player[0]
        power = player[4]
        if power >= 50:
            msg = ""
            try:
                special_name = ' '.join(commands[1:]).replace(";", "").replace("'", "").replace('"', "")
                if special_name and len(special_name) > 0:
                    self.game_instance.edit_special(player_id, special_name)
                    msg = "**" + message.author.display_name + "**'s special attack was renamed to **" + special_name + "**!"
                    print("*** " + str(message.author.id) + " renamed their special attack.")
                else:
                    msg = 'Entered special attack name is too short!'
            except:
                msg = 'Write "!gg" for help with commands!'
            await self._send_message(msg, message.channel)
        else:
            await self._send_message('**' + message.author.display_name + '** needs power level of atleast 50!', message.channel)

    async def _boss(self, commands, message):
        print("*** " + str(message.author.id) + " fought a boss.")
        msg = self.game_instance.play_bosses(str(message.author.id), message.author.display_name)
        await self._send_message(msg, message.channel)

    async def _fish(self, commands, message):
        print("*** " + str(message.author.id) + " went fishing.")
        msg = ""
        if len(commands) >= 2 and commands[1] == "all":
            msg = self.game_instance.fishing(str(message.author.id), message.author.display_name, True)
        else:
            msg = self.game_instance.fishing(str(message.author.id), message.author.display_name, False)
        await self._send_message(msg, message.channel)

    async def _event(self, commands, message):
        if len(commands) == 1:
            msg = self.game_instance.events(str(message.author.id), message.author.display_name)
            await self._send_message(msg, message.channel)
        elif len(commands) >= 2:
            msg = self.game_instance.event(str(message.author.id), message.author.display_name, " ".join(commands[1:]))
            print("*** " + str(message.author.id) + " activated event: " + " ".join(commands[1:]))
            await self._send_message(msg, message.channel)

    async def _repository(self, commands, message):
        await self._send_message("https://github.com/ollikkarki/goumetgame-discordbot", message.channel)

    async def on_ready(self):
        print("Initializing")
        self.randomizer = random.Random()
        self.game_instance = game.Game(DATABASE_ADDRESS)
        print('Logged on as', self.user)
        self.ready = True
        if arguments:
            if (not "-silent" in arguments) and (not "-s" in arguments):
                await self._announcement("GourmetGame is Online!")

    async def on_message(self, message):
        if not self.ready:
            print("The client is not ready yet!")
            return

        if message.author == self.user:
            return

        cmd = str(message.content).lower()

        if cmd[0:4] == '!gg ':
            self.game_instance.update_nickname(str(message.author.id), message.author.display_name)
            commands = cmd.split(" ")[1:]
            if len(commands) > 0:
                command = self._commands.get(commands[0])
                if command and commands[0] in self._unregistered_commands:
                    await command(commands, message)
                elif command:
                    if self.game_instance.get_player(str(message.author.id)):
                        await command(commands, message)
                    else:
                        await self._send_message('**' + message.author.display_name + '** is not part of the game!', message.channel)
                else:
                    if message.author.id in ADMINS:
                        if commands[0] == 'addplays':
                            amount = 1
                            try:
                                amount = max(int(commands[1]), 1)
                            except:
                                amount = 1
                            self.game_instance.add_plays(amount)
                            print("****** " + "Added " + str(amount) + " plays to all players.")
                            try:
                                await self._announcement(str(' '.join(commands[2:])))
                            except:
                                await self._announcement("You have been gifted " + str(amount) + " extra plays for today by the administrator!")
                        elif commands[0] == 'addevent':
                            if len(commands) >= 2:
                                if self.game_instance.add_event(str(" ".join(commands[1:]))):
                                    await self._announcement("Added **" + str(' '.join(commands[1:])) + "** event to all players!")
                                    print("****** " + "Added " + str(" ".join(commands[1:])) + " event to all players.")
                                else:
                                    await self._send_message('The event **' + str(' '.join(commands[1:])) +'** does not exist!', message.channel)
                        elif commands[0] == 'addcurrency':
                            amount = 1
                            try:
                                amount = max(int(commands[1]), 1)
                            except:
                                amount = 1
                            self.game_instance.add_currency(amount)
                            print("****** " + "Added " + str(amount) + " currency to all players.")
                            try:
                                await self._announcement(str(' '.join(commands[2:])))
                            except:
                                await self._announcement("You have been gifted " + str(amount) + " extra monies by the administrator!")
                        else:
                            await self._send_message('Invalid command type "!gg" for help!', message.channel)
                    else:
                        await self._send_message('Invalid command type "!gg" for help!', message.channel)
        elif cmd == "!gg":
            self.game_instance.update_nickname(str(message.author.id), message.author.display_name)
            await self._send_message("Commands\n" +
                                    "!gg\n" +
                                    "       start - adds you into the game!\n" +
                                    "       play - plays the game!\n" + 
                                    "       adventure - player can go to an adventure once per day!\n" +
                                    "       boss - player can attempt to defeat a boss once per day!\n" +
                                    "       pull - rolls with currency in game! 5 Monies per roll! !gg pull all to use all monies with one message!\n" +
                                    "       fish - use bait to fish, might grant monies or plays! !gg fish all to use all baits with one message!\n" +
                                    "       event - lists events you have available! !gg event [event name] to play the event!\n" +
                                    "\n" +
                                    "       status - shows your current status in the game!\n" +
                                    "       special - use to name your special attack (_ex. !gg special Turbo Attack_). Special attack is unlocked after reaching 50 power.\n" +
                                    "       chances - lists pull chances.\n" +
                                    "       leaderboard - lists out players sorted by power.\n" +
                                    "\n" +
                                    "       repository - sends a link to the game's github repository\n\n" +
                                    "**Warning: whenever you do an action in game, your current nickname is stored and may be displayed in other servers with access to the game.**", message.channel)

    async def _send_message(self, message, channel):
        if len(message) < 2000:
            await channel.send(message)
        else:
            msg_parts = message.split("\n")
            msg = ""
            for line in msg_parts:
                if len(msg + line + "\n") < 2000:
                    msg = msg + line + "\n"
                else:
                    await channel.send(msg)
                    msg = line + "\n"
            await channel.send(msg)

    async def _announcement(self, announcement):
        for channel in self.get_all_channels():
            if channel.name == 'gourmet-game':
                await channel.send(str(announcement))

date = datetime.datetime

def get_date():
    return str(date.now()).split(" ")[0]

client = MyClient()

client.run(TOKEN)