import discord
from discord.ext import commands
from discord.utils import get

class c188(commands.Cog, name="c188"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Devoted_Servant\'s_Preparation', aliases=['c188', 'Devoted_Servant_10'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Devoted Servant\'s Preparation',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2345156.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Devoted Servant)', inline=True)
        embed.add_field(name='Type', value='Trap/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='You can discard 1 "Devoted Servant" card, or banish 2 "Devoted Servant" cards from your GY, or shuffle 3 banished "Devoted Servant" cards into the Deck; add 1 "Devoted Servant" monster from your Deck to your hand. If this card is banished: You can send 1 "Devoted Servant" card from your Deck to the GY. You can only use each effect of "Devoted Servant\'s Preparation" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c188(bot))