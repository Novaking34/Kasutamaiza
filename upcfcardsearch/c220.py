import discord
from discord.ext import commands
from discord.utils import get

class c220(commands.Cog, name="c220"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Guard_Priestess', aliases=['c220'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Guard Priestess',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2356410.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (0/2000)', inline=False)
        embed.add_field(name='Monster Effect', value='When your opponent declares an attack, or activates a card or effect that would inflict damage to your LP (Quick Effect): You can discard this card; the first time you would take damage, you gain that much LP instead.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c220(bot))