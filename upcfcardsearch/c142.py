import discord
from discord.ext import commands
from discord.utils import get

class c142(commands.Cog, name="c142"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Gilligan_the_Iron_Knight', aliases=['c142'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Gilligan the Iron Knight',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336207.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Warrior/Normal (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='7 (2100/1000)', inline=False)
        embed.add_field(name='Lore Text', value='Wandering the great forest, Gilligan works night and day, hoping to prevent the new Darkness from falling to the land.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c142(bot))