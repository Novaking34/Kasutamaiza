import discord
from discord.ext import commands
from discord.utils import get

class c8(commands.Cog, name="c8"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Sacrosanct_Devouring_Pyre', aliases=['c8'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Sacrosanct Devouring Pyre',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2308475.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Tribute 2 monsters, then target 2 monsters; destroy those targets. You can only activate 1 "Sacrosanct Devouring Pyre" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c8(bot))