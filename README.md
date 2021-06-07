# goumetgame-discordbot

GourmetGame is a discord bot meant for a smallish (*1-50*) user base.

The bot itself runs a game played through discord chat client.

## Set up

Create **GourmetGamer** role that the bot can manage in your discord server.

The project needs a ***settings.txt*** file in same location as ***bot.py***.

settings.txt file structure
```
[Discord Bot Token]
[Admin 1 Discord unique id],[Admin 2 Discord unique id], ..., [Admin n Discord unique id]
[Game Database path]
[Logger Database Path]
[Backup Folder Path]
```

test_settings.txt file structure
```
[Game Test Database path]
[Logger Test Database Path]
```

database tables
```
CREATE TABLE adventures (user_id TEXT, last_adventure TEXT);
CREATE TABLE event(user_id TEXT, event_name TEXT);
CREATE TABLE fishing(user_id TEXT, baits INTEGER);
CREATE TABLE specials (user_id TEXT, special_attack TEXT);
CREATE TABLE bosses (user_id TEXT, last_attempt TEXT, tier INTEGER);
CREATE TABLE extra_plays(user_id TEXT, amount INTEGER);
CREATE TABLE nicknames (user_id TEXT, nickname TEXT);
CREATE TABLE users (user_id TEXT, last_played TEXT, plays_left INTEGER, currency INTEGER, power INTEGER);
```

Logger database tables
```
CREATE TABLE log_entry(user_id TEXT, user_name TEXT, time TEXT, log_level TEXT, log_entry TEXT);
```

dependencies (*should be installable with pip*)
```
sqlite3
discord
```
