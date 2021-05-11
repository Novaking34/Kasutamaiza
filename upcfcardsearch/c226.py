import discord
from discord.ext import commands
from discord.utils import get

class c226(commands.Cog, name="c226"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Mountain_Turtle', aliases=['c226'])    
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Mountain Turtle',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359077.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Rock/Normal (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='6 (0/3200)', inline=False)
        embed.add_field(name='Lore Text', value='If you walk through the green fields, you might see this beautiful sight. A gigantic turtle, whose shell almost touches the sky. Nobody can stop this creature, but it is actually harmless due to it\'s peaceful nature.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c226(bot))