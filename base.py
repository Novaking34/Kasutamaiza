import os
from dotenv import load_dotenv
from discord.ext import commands

def main():
    client = commands.Bot(command_prefix="uf!")

    load_dotenv()

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")

    for file in os.listdir("modules"):
        if file.endswith(".py"):
            name = file[:-3]
            client.load_extension(f"modules.{name}")

    for file in os.listdir("upcfcardsearch"):
        if file.endswith(".py"):
            name = file[:-3]
            client.load_extension(f"upcfcardsearch.{name}")          

    client.run(os.getenv("DISCORD_TOKEN"))

if __name__ == '__main__':
    main()