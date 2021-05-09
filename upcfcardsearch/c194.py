import discord
from discord.ext import commands
from discord.utils import get

class c194(commands.Cog, name="c194"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Mechanical_Servant_Nana', aliases=['c194', 'Devoted_Servant_15'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Mechanical Servant Nana',
                              color=0xcccccc)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2345163.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Devoted Servant)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Synchro/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (1000/1000)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Tuner + "Devoted Servant Nana"\nDuring your turn (Quick Effect): You can banish 1 "Devoted Servant" card from your GY and target 1 card in your opponent\'s GY; banish it. During your opponent\'s turn (Quick Effect): You can discard 1 card and target 1 card on the field; that card cannot be destroyed or banished by card effects this turn. If this card destroyed: You can shuffle 1 banished "Devoted Servant" card into the Deck; gain 1000 LP. You can only use each effect of "Mechanical Servant Nana" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c194(bot))