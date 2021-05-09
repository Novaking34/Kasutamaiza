import discord
from discord.ext import commands
from discord.utils import get

class c182(commands.Cog, name="c182"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Devoted_Servant_Maria', aliases=['c182', 'Devoted_Servant_3'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Devoted Servant Maria',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2345137.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Devoted Servant)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (1000/1000)', inline=False)
        embed.add_field(name='Monster Effect', value='You can shuffle 1 of your banished "Devoted Servant" cards into the Deck; add 1 "Devoted Servant" monster from your GY to your hand. When either player banishes a card(s) to activate a card or effect (Quick Effect): You can Special Summon this card from your hand, then apply one of these effects.\n● Negate the activation.\n● Add 1 "Devoted Servant" Card from your Deck to your hand, then discard 1 card.\nYou can only use each effect of "Devoted Servant Maria" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c182(bot))