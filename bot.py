import discord
import random
import game.game as game
import sys
import threading
import time
import datetime
import game.logger as logger # pylint: disable=no-name-in-module,import-error
from shutil import copyfile
import os

def clean_line(path):
    if path[-1] == "\n":
        return path[:-1]
    return path

arguments = sys.argv

settings_file = open("settings.txt", "r")
lines = settings_file.readlines()
TOKEN = lines[0]
ADMINS = []
for line in lines[1].split(","):
    ADMINS.append(int(clean_line(line)))
DATABASE_ADDRESS = clean_line(lines[2])
LOG_ADDRESS = clean_line(lines[3])
BACKUP_PATH = clean_line(lines[4])

class GourmetGame(discord.Client):

    def __init__(self, database_address, log_address, run=None, send_message = None, silent_logging = False):
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
            "repository":self._repository,
            "finisher":self._finisher
        }
        self.silent_logging = silent_logging
        self.ready = False
        self.log_styling = "               "
        self.log_styling_long = "                                             "
        self.response_level = "Response"
        self.system_level = "System"
        self.date = datetime.datetime
        self.logger_ready = False
        self.logger = logger.Logger(log_address, self.log)
        self.logger_ready = True
        self.randomizer = random.Random()
        self.game_instance = game.Game(database_address, self.log)
        if run and send_message:
            self.run = run
            self._send_message = send_message
        self.ready = True

    async def _start(self, commands, message):
        if self.game_instance.get_player(str(message.author.id)) == None:
            self.game_instance.add_player(str(message.author.id))
            self.log("Player added to the game", message.author.id, message.author.display_name, self.response_level)
            await self._send_message('**' + message.author.display_name + '** is now added to the game!', message.channel)
        else:
            await self._send_message('**' + message.author.display_name + '** was already added to the game!', message.channel)

    async def _play(self, commands, message):
        self.log("Command executed: play", message.author.id, message.author.display_name, self.response_level)
        await self._send_message(self.game_instance.play(str(message.author.id), message.author.display_name), message.channel)

    async def _finisher(self, commands, message):
        player = self.game_instance.get_player(str(message.author.id))
        player_id = player[0]
        power = player[4]
        if power >= 400:
            msg = ""
            try:
                finisher_name = ' '.join(commands[1:]).replace(";", "").replace("'", "").replace('"', "")
                if finisher_name and len(finisher_name) > 0:
                    self.log("Command executed: finisher, subcommand: " + finisher_name, message.author.id, message.author.display_name, self.response_level)
                    self.game_instance.update_finisher(player_id, finisher_name)
                    msg = "**" + message.author.display_name + "**'s finishing move was renamed to **" + finisher_name + "**!"
                else:
                    msg = 'Entered finishing move name is too short!'
            except:
                msg = 'Write "!gg" for help with commands!'
            await self._send_message(msg, message.channel)
        else:
            await self._send_message('**' + message.author.display_name + '** needs power level of at least 400!', message.channel)

    async def _adventure(self, commands, message):
        self.log("Command executed: adventure", message.author.id, message.author.display_name, self.response_level)
        msg = self.game_instance.play_adventure(str(message.author.id), message.author.display_name)
        await self._send_message(msg, message.channel)

    async def _pull(self, commands, message):
        if len(commands) >= 2 and commands[1] == "all":
            self.log("Command executed: pull, subcommand: all", message.author.id, message.author.display_name, self.response_level)
            msg = self.game_instance.roll(str(message.author.id), message.author.display_name, True)
        else:
            self.log("Command executed: pull", message.author.id, message.author.display_name, self.response_level)
            msg = self.game_instance.roll(str(message.author.id), message.author.display_name, False)
        await self._send_message(msg, message.channel)

    async def _status(self, commands, message):
        self.log("Command executed: status", message.author.id, message.author.display_name, self.response_level)
        await self._send_message(self.game_instance.status(str(message.author.id), message.author.display_name), message.channel)

    async def _chances(self, commands, message):
        self.log("Command executed: chances", message.author.id, message.author.display_name, self.response_level)
        await self._send_message('**Chances when pulling!**\n' +
                                   '    :star:; 52%\n' +
                                   '    :star::star:; 28%\n' +
                                   '    :star::star::star:; 12%\n' +
                                   '    :star::star::star::star:; 5%\n' +
                                   '    :star::star::star::star::star:; 3%' +
                                   'Average power increase per pull **1.79**.',
                                   message.channel)

    async def _leaderboard(self, commands, message):
        self.log("Command executed: leaderboard", message.author.id, message.author.display_name, self.response_level)
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
                    self.log("Command executed: special, subcommand: " + special_name, message.author.id, message.author.display_name, self.response_level)
                    self.game_instance.edit_special(player_id, special_name)
                    msg = "**" + message.author.display_name + "**'s special attack was renamed to **" + special_name + "**!"
                else:
                    msg = 'Entered special attack name is too short!'
            except:
                msg = 'Write "!gg" for help with commands!'
            await self._send_message(msg, message.channel)
        else:
            await self._send_message('**' + message.author.display_name + '** needs power level of at least 50!', message.channel)

    async def _boss(self, commands, message):
        self.log("Command executed: boss", message.author.id, message.author.display_name, self.response_level)
        msg = self.game_instance.play_bosses(str(message.author.id), message.author.display_name)
        await self._send_message(msg, message.channel)

    async def _fish(self, commands, message):
        msg = ""
        if len(commands) >= 2 and commands[1] == "all":
            self.log("Command executed: fish, subcommand: all", message.author.id, message.author.display_name, self.response_level)
            msg = self.game_instance.fishing(str(message.author.id), message.author.display_name, True)
        else:
            self.log("Command executed: fish", message.author.id, message.author.display_name, self.response_level)
            msg = self.game_instance.fishing(str(message.author.id), message.author.display_name, False)
        await self._send_message(msg, message.channel)

    async def _event(self, commands, message):
        if len(commands) == 1:
            self.log("Command executed: event", message.author.id, message.author.display_name, self.response_level)
            msg = self.game_instance.events(str(message.author.id), message.author.display_name)
            await self._send_message(msg, message.channel)
        elif len(commands) >= 2:
            msg = self.game_instance.event(str(message.author.id), message.author.display_name, " ".join(commands[1:]))
            self.log("Command executed: event, subcommand: " + " ".join(commands[1:]), message.author.id, message.author.display_name, self.response_level)
            await self._send_message(msg, message.channel)

    async def _repository(self, commands, message):
        await self._send_message("https://github.com/ollikkarki/goumetgame-discordbot", message.channel)

    async def on_ready(self):
        self.log("Initializing", 0, "on_ready", self.system_level)
        self.log("Logged on as " + str(self.user), 0, "on_ready", self.system_level)
        if arguments:
            if (not "-silent" in arguments) and (not "-s" in arguments):
                await self._announcement("GourmetGame is Online!")
        self.ready = True

    async def on_message(self, message):
        if not self.ready:
            self.log("System was not ready respond", 0, "on_ready", self.system_level)
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
                            self.log("Command executed: addplays, subcommand: " + str(amount), 1, "Admin", self.response_level)
                            try:
                                await self._announcement(str(' '.join(commands[2:])))
                            except:
                                await self._announcement("You have been gifted " + str(amount) + " extra plays for today by the administrator!")
                        elif commands[0] == 'addevent':
                            if len(commands) >= 2:
                                if self.game_instance.add_event(str(" ".join(commands[1:]))):
                                    await self._announcement("Added **" + str(' '.join(commands[1:])) + "** event to all players!")
                                    self.log("Command executed: addevent, subcommand: " + ' '.join(commands[1:]), 1, "Admin", self.response_level)
                                else:
                                    await self._send_message('The event **' + str(' '.join(commands[1:])) +'** does not exist!', message.channel)
                        elif commands[0] == 'addcurrency':
                            amount = 1
                            try:
                                amount = max(int(commands[1]), 1)
                            except:
                                amount = 1
                            self.game_instance.add_currency(amount)
                            self.log("Command executed: addcurrency, subcommand: " + str(amount), 1, "Admin", self.response_level)
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
                                    "       special - use to name your special attack (_ex. !gg special Turbo Attack_). Special attack is unlocked after reaching 50 power. Ten percent chance to double power on every attack.\n" +
                                    "       finisher - use to name your finishing move (_ex. !gg finisher Pile Driver_). Finishing move is unlocked after reaching 400 power. Once per fight doubles power when enemy has 1 hp.\n" +
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
    
    def log(self, message, log_id, log_name, log_level):
        time = self.get_time()
        msg = time + " : " + str(log_level) + self.log_styling[len(str(log_level)):]
        msg += str(log_id) + " (" + str(log_name) + ") " + self.log_styling_long[len(str(log_id) + " (" + str(log_name) + ") "):]
        msg += str(message)
        if self.logger_ready:
            self.logger.write_entry(log_id, log_name, time, log_level, message)
        if not self.silent_logging:
            print(msg)

    def get_time(self):
        return str(self.date.now()).split(".")[0]


def get_time():
    return str(datetime.datetime.now()).split(".")[0]

if __name__ == "__main__":
    if os.path.isfile(DATABASE_ADDRESS):
        copyfile(DATABASE_ADDRESS, BACKUP_PATH + (get_time() + "_Database.db").replace(" ", "_").replace(":", "-"))
    if os.path.isfile(LOG_ADDRESS):
        copyfile(LOG_ADDRESS, BACKUP_PATH + (get_time() + "_Log.db").replace(" ", "_").replace(":", "-"))
    client = GourmetGame(DATABASE_ADDRESS, LOG_ADDRESS)
    client.run(TOKEN)