import discord
from discord.ext import commands
from discord.utils import get

class c193(commands.Cog, name="c193"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Mechanical_Servant_Maria', aliases=['c193', 'Devoted_Servant_14'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Mechanical Servant Maria',
                              color=0xcccccc)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2345160.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Devoted Servant)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Synchro/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='6 (1500/1500)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Tuner + "Devoted Servant Maria"\nEach time your opponent banishes a card(s) to activate a card or effect, inflict 1000 damage to your opponent. (Quick Effect): You can shuffle 1 of your banished cards into the Deck and target 1 monster on the the field; its ATK/DEF become 0 until the end of the turn. When either player banishes a card(s) to activate a card of effect (Quick Effect): You can target 1 Spell/Trap card on the field; banish it. You can only use each effect of "Mechanical Servant Maria" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c193(bot))