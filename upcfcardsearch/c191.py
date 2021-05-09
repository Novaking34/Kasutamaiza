import discord
from discord.ext import commands
from discord.utils import get

class c191(commands.Cog, name="c191"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Mechanical_Servant_Anna', aliases=['c191', 'Devoted_Servant_12'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Mechanical Servant Anna',
                              color=0xcccccc)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2345158.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Devoted Servant)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Synchro/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='7 (2500/500)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Tuner + "Devoted Servant Anna"\nEach time your opponent discards a card(s) to activate a card or effect, inflict 1000 damage to your opponent. (Quick Effect): You can banish 1 card from your GY; your opponent cannot activate cards or effects during the Battle Phase this turn. When either player discards a card(s) to activate a card of effect (Quick Effect): You can have your opponent send 1 card they control to the GY. You can only use each effect of "Mechanical Servant Anna" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c191(bot))