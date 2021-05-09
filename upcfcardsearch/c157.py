import discord
from discord.ext import commands
from discord.utils import get

class c157(commands.Cog, name="c157"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Ougala', aliases=['c157'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Ougala',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336265.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Psychic/Normal (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='8 (2600/200)', inline=False)
        embed.add_field(name='Lore Text', value='In times of despair, its said that an Ougala is near, feasting on the darkness and hopelessness.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c157(bot))