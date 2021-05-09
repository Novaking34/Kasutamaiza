import discord
from discord.ext import commands
from discord.utils import get

class c181(commands.Cog, name="c181"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Devoted_Servant_Carla', aliases=['c181', 'Devoted_Servant_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Devoted Servant Carla',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2344883.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Devoted Servant)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='2 (500/2000)', inline=False)
        embed.add_field(name='Monster Effect', value='You can discard 1 "Devoted Servant" card; Special Summon 1 "Devoted Servant" monster from your Deck. When either player shuffles a card(s) into the Deck to activate a card or effect (Quick Effect): You can Special Summon this card from your hand, then apply one of these effects.\n● Negate the activation.\n● Add 1 "Devoted Servant" Card from your Deck to your hand, then discard 1 card.\nYou can only use each effect of "Devoted Servant Carla" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c181(bot))