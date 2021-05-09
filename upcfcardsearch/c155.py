import discord
from discord.ext import commands
from discord.utils import get

class c155(commands.Cog, name="c155"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Magolia_the_Queen_of_the_Ghost', aliases=['c155', 'LeSpookie_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Magolia, the Queen of the Ghost',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336255.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (LeSpookie)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Zombie/Normal (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='6 (2100/2400)', inline=False)
        embed.add_field(name='Lore Text', value='Some say that late at night, a dark shadow follows Magolia, possesing anyone who may come into contact with her. Magolia haunts the mansion on LeSpookie Street, keeping hidden all of its dark secrets.\n\n(This card is always treated as a "LeSpookie" card.)', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c155(bot))