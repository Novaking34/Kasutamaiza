import discord
from discord.ext import commands
from discord.utils import get

class c162(commands.Cog, name="c162"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='The_Water_Spirit_Nuro', aliases=['c162'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='The Water Spirit Nuro',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2344690.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3=', inline=True)
        embed.add_field(name='Type (Attribute)', value='Aqua/Normal (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (300/200)', inline=False)
        embed.add_field(name='Lore Text', value='It is said that within all water lies the free spirit, Nuro. Nuro flows from river to river, guided by the Elementist for support.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c162(bot))