import discord
import random
import game.game as game
import sys

arguments = sys.argv

settings_file = open("settings.txt", "r")
lines = settings_file.readlines()
TOKEN = lines[0]
ADMINS = lines[1:]


class MyClient(discord.Client):
    async def on_ready(self):
        print("Initializing")
        self.randomizer = random.Random()
        self.game_instance = game.Database("D:/programming/code/projects/python/discordbot/game/database.db")
        print('Logged on as', self.user)
        self.ready = True
        if arguments:
            if (not "-silent" in arguments) and (not "-s" in arguments):
                await self._announcement("GourmetGame is Online!")

    async def on_message(self, message):
        try:
            if not self.ready:
                print("The client is not ready yet!")
                return
        except:
            print("The client is not ready yet!")
            return


        # don't respond to ourselves
        if message.author == self.user:
            return

        cmd = str(message.content).lower()

        if cmd[0:4] == '!gg ':
            self.game_instance.update_nickname(str(message.author.id), message.author.display_name)
            commands = cmd.split(" ")[1:]
            if len(commands) > 0:
                if commands[0] == 'start':
                    if self.game_instance.get_player(str(message.author.id)) == None:
                        self.game_instance.add_player(str(message.author.id))
                        print("*** " + "Added " + str(message.author.id) + " to the game.")
                        await message.channel.send('**' + message.author.display_name + '** is now added to the game!')
                    else:
                        await message.channel.send('**' + message.author.display_name + '** was already added to the game!')
                elif commands[0] == 'play':
                    if self.game_instance.get_player(str(message.author.id)):
                        print("*** " + str(message.author.id) + " played the game.")
                        await message.channel.send(self.game_instance.play(str(message.author.id), message.author.display_name))
                    else:
                        await message.channel.send('**' + message.author.display_name + '** is not part of the game!')
                elif commands[0] == 'adventure':
                    if self.game_instance.get_player(str(message.author.id)):
                        print("*** " + str(message.author.id) + " went to an adventure.")
                        msg = self.game_instance.play_adventure(str(message.author.id), message.author.display_name)
                        if len(msg) < 2000:
                            await message.channel.send(msg)
                        else:
                            msg_parts = msg.split("\n")
                            msg = ""
                            for line in msg_parts:
                                if len(msg + line + "\n") < 2000:
                                    msg = msg + line + "\n"
                                else:
                                    await message.channel.send(msg)
                                    msg = line + "\n"
                            await message.channel.send(msg)
                    else:
                        await message.channel.send('**' + message.author.display_name + '** is not part of the game!')
                elif commands[0] == 'pull':
                    if self.game_instance.get_player(str(message.author.id)):
                        print("*** " + str(message.author.id) + " pulled.")
                        await message.channel.send(self.game_instance.roll(str(message.author.id), message.author.display_name))
                    else:
                        await message.channel.send('**' + message.author.display_name + '** is not part of the game!')
                elif commands[0] == 'status':
                    if self.game_instance.get_player(str(message.author.id)):
                        await message.channel.send(self.game_instance.status(str(message.author.id), message.author.display_name))
                    else:
                        await message.channel.send('**' + message.author.display_name + '** is not part of the game!')
                elif commands[0] == 'chances':
                    star_1 = len(self.game_instance.roll_1) * 10 / len(self.game_instance.roll_table) * 100
                    star_2 = len(self.game_instance.roll_2) * 6 / len(self.game_instance.roll_table) * 100
                    star_3 = len(self.game_instance.roll_3) * 3 / len(self.game_instance.roll_table) * 100
                    star_4 = len(self.game_instance.roll_4) * 2 / len(self.game_instance.roll_table) * 100
                    star_5 = len(self.game_instance.roll_5) * 1 / len(self.game_instance.roll_table) * 100
                    await message.channel.send('**Chances when pulling!**\n' +
                                               '    :star:; ' + str(star_1)[0:5] + '%\n' +
                                               '    :star::star:; ' + str(star_2)[0:5] + '%\n' +
                                               '    :star::star::star:; ' + str(star_3)[0:5] + '%\n' +
                                               '    :star::star::star::star:; ' + str(star_4)[0:5] + '%\n' +
                                               '    :star::star::star::star::star:; ' + str(star_5)[0:5] + '%')
                elif commands[0] == 'leaderboard':
                    await message.channel.send(self.game_instance.leaderboard())
                elif commands[0] == 'special':
                    if self.game_instance.get_player(str(message.author.id)):
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
                            await message.channel.send(msg)
                        else:
                            await message.channel.send('**' + message.author.display_name + '** needs power level of atleast 50!')
                    else:
                        await message.channel.send('**' + message.author.display_name + '** is not part of the game!')
                elif commands[0] == 'boss':
                    msg = ""
                    if self.game_instance.get_player(str(message.author.id)):
                        print("*** " + str(message.author.id) + " fought a boss.")
                        msg = self.game_instance.play_bosses(str(message.author.id), message.author.display_name)
                        if len(msg) < 2000:
                            await message.channel.send(msg)
                        else:
                            msg_parts = msg.split("\n")
                            msg = ""
                            for line in msg_parts:
                                if len(msg + line + "\n") < 2000:
                                    msg = msg + line + "\n"
                                else:
                                    await message.channel.send(msg)
                                    msg = line + "\n"
                            await message.channel.send(msg)
                    else:
                        msg = '**' + message.author.display_name + '** is not part of the game!'
                elif commands[0] == 'fish':
                    if self.game_instance.get_player(str(message.author.id)):
                        print("*** " + str(message.author.id) + " went fishing.")
                        msg = ""
                        if len(commands) >= 2 and commands[1] == "all":
                            msg = self.game_instance.fishing(str(message.author.id), message.author.display_name, True)
                        else:
                            msg = self.game_instance.fishing(str(message.author.id), message.author.display_name, False)
                        if len(msg) < 2000:
                            await message.channel.send(msg)
                        else:
                            msg_parts = msg.split("\n")
                            msg = ""
                            for line in msg_parts:
                                if len(msg + line + "\n") < 2000:
                                    msg = msg + line + "\n"
                                else:
                                    await message.channel.send(msg)
                                    msg = line + "\n"
                            await message.channel.send(msg)
                    else:
                        await message.channel.send('**' + message.author.display_name + '** is not part of the game!')
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
                            await message.channel.send('Invalid command type "!gg" for help!')
                    else:
                        await message.channel.send('Invalid command type "!gg" for help!')
        elif cmd == "!gg":
            self.game_instance.update_nickname(str(message.author.id), message.author.display_name)
            await message.channel.send("Commands\n" +
                                    "!gg\n" +
                                    "       start - adds you into the game!\n" +
                                    "       play - plays the game!\n" + 
                                    "       adventure - player can go to an adventure once per day!\n" +
                                    "       boss - player can attempt to defeat a boss once per day!\n" +
                                    "       pull - rolls with currency in game! 5 Monies per roll!\n" +
                                    "       fish - use bait to fish, might grant monies or plays! !gg fish all to use all baits with one message!\n"
                                    "\n" +
                                    "       status - shows your current status in the game!\n" +
                                    "       special - use to name your special attack (_ex. !gg special Turbo Attack_). Special attack is unlocked after reaching 50 power.\n" +
                                    "       chances - lists pull chances.\n" +
                                    "       leaderboard - lists out players sorted by power.")
                                       
    
    async def _announcement(self, announcement):
        for channel in self.get_all_channels():
            if channel.name == 'gourmet-game':
                await channel.send(str(announcement))

client = MyClient()
client.run(TOKEN)