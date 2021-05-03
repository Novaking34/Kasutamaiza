import discord
from discord.ext import commands
from discord.utils import get

class c141(commands.Cog, name="c141"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Genie_of_the_Sand', aliases=['c141'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Genie of the Sand',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336204.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Rock/Normal (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (300/200)', inline=False)
        embed.add_field(name='Lore Text', value='Without the mystic lamp to hold him back, the Genie is now free to run amok amongst the people. Some say a powerful bond can tame this Genie\'s heart, however.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c141(bot))