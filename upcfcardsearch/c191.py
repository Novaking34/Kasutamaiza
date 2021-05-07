import discord
from discord.ext import commands
from discord.utils import get

class c191(commands.Cog, name="c191"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Mechanical_Servant_Carla', aliases=['c191', 'Devoted_Servant_13'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Mechanical Servant Carla',
                              color=0xcccccc)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2345159.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Devoted Servant)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Synchro/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (1000/2000)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Tuner + "Devoted Servant Carla"\nEach time your opponent shuffles a card(s) into the Deck to activate a card or effect, inflict 1000 damage to your opponent. (Quick Effect): You can discard 1 card and target 1 Spell/Trap your opponent controls; negate its effects until the end of the turn. When either player shuffles a card(s) into the Deck to activate a card or effect (Quick Effect): You can target 1 monster on the field; banish it. You can only use each effect of "Mechanical Servant Carla" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c191(bot))