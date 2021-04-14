import os
from dotenv import load_dotenv
from discord.ext import commands

def main():
    client = commands.Bot(command_prefix="uf!")

    load_dotenv()

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")
    
    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, ".py")):
            client.load_extension(f"modules.{folder}")

    for folder in os.listdir("upcfcardsearch"):
        if os.path.exists(os.path.join("upcfcardsearch", folder, ".py")):
            client.load_extension(f"upcfcardsearch.{folder}")

    client.run(os.getenv("DISCORD_TOKEN"))

if __name__ == '__main__':
    main()