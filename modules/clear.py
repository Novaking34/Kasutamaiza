from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

class Clear(commands.Cog, name="Clear"):
    """Receives ping commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def clear(self, ctx, amount=5):
	    await ctx.channel.purge(limit=amount)

def setup(bot: commands.Bot):
    bot.add_cog(Clear(bot))