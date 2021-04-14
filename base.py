import os
from dotenv import load_dotenv
from discord.ext import commands

def main():
    client = commands.Bot(command_prefix="uf!")

    load_dotenv()

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")
    
    for file in os.listdir("module"):
        if file.endswith(".py"):
            client.load_extension(f'commands.{file[:-3]}')

    for file in os.listdir("upcfcardsearch"):
        if file.endswith(".py"):
            client.load_extension(f'commands.{file[:-3]}')

    client.run(os.getenv("DISCORD_TOKEN"))

if __name__ == '__main__':
    main()