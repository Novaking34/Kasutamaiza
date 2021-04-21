from discord.ext import commands

class duel(commands.Cog, name="Duel"):
    """Receives ping commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def duel(self, ctx: commands.Context):
        """Checks for a response from the bot"""
        await ctx.send("Of course, all duels are conducted here https://www.duelingbook.com/")

def setup(bot: commands.Bot):
    bot.add_cog(duel(bot))