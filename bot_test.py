from bot import GourmetGame
import asyncio
import os

settings_file = open("test_settings.txt", "r")
lines = settings_file.readlines()
if lines[0][-1] == "\n":
    TEST_DATABASE_ADDRESS = lines[0][:-1]
else: 
    TEST_DATABASE_ADDRESS = lines[0]
TEST_LOG_ADDRESS = lines[1]

class Author:
    def __init__(self, author_id, display_name):
        self.id = author_id
        self.display_name = display_name

class Message:
    def __init__(self, author_id, display_name, content):
        self.author = Author(author_id, display_name)
        self.channel = None
        self.content = content

async def run_help(client):
    command = input("> ")
    if command == "quit" or command == "exit":
        delete_databases()
        return False
    elif command == "help" or command == "!gg":
        await client.on_message(Message("3", "Manual Tester", "!gg"))
    else:
        await client.on_message(Message("3", "Manual Tester", "!gg " + command))
    return True
    
def run(token, client):
    while True:
        if not asyncio.run(run_help(client)):
            break

async def send_message(message, channel):
    print(message.replace("*", ""))

def delete_databases():
    try:
        os.remove(TEST_DATABASE_ADDRESS)
        print("Test game database deleted.")
    except:
        print("Test game database did not exist.")
    try:
        os.remove(TEST_LOG_ADDRESS)
        print("Test log database deleted.")
    except:
        print("Test log database did not exist.")

if __name__ == "__main__":
    delete_databases()
    client = GourmetGame(TEST_DATABASE_ADDRESS, TEST_LOG_ADDRESS, run, send_message, silent_logging=True)
    client.run(None, client)
