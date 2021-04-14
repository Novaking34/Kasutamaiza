import os
from discord.ext import commands

def main ():
    client = commands.Bot(command_prefix="uf!")

    @client.event
    async def on_ready():
        print(f"{client.user.name} has rose from his slumber")

    @client.event
    async def on_message(ctx):
        if (ctx.content.startswith("Hello"))
        await ctx.channel.send(f"Greetings {ctx.author.mention}")

    client.run(os.getenv("DISCORD_TOKEN"))

if __name__ == '__main__':
    main()