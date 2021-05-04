import discord
from discord.ext import commands
from discord.utils import get

class c179(commands.Cog, name="c179"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Devoted_Servant_Anna', aliases=['c179', 'Devoted_Servant_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Devoted Servant Anna',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2344878.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Devoted Servant)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (1500/0)', inline=False)
        embed.add_field(name='Monster Effect', value='You can banish 1 "Devoted Servant" card from your GY; send 1 "Devoted Servant" card from your Deck to the GY. When either player discards a card(s) to activate a card or effect (Quick Effect): You can Special Summon this card from your hand, then apply one of these effects.\n● Negate the activation.\n● Add 1 "Devoted Servant" Card from your Deck to your hand, then discard 1 card.\nYou can only use each effect of "Devoted Servant Anna" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c179(bot))