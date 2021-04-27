import discord
from discord.ext import commands
from discord.utils import get

class c96(commands.Cog, name="c96"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Iron_Wall_of_Defense', aliases=['c96'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Iron Wall of Defense',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321542.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='When a monster you control with 500 or less ATK is targeted for an attack: Negate that attack, then change the attacking monster\'s battle position to face down Defense Position.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c96(bot))