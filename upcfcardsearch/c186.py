import discord
from discord.ext import commands
from discord.utils import get

class c186(commands.Cog, name="c186"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Devoted_Servant_Reinforcements', aliases=['c186', 'Devoted_Servant_8'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Devoted Servant\'s Reinforcements',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2345153.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Devoted Servant)', inline=True)
        embed.add_field(name='Type', value='Spell/Quick-Play', inline=False)
        embed.add_field(name='Card Effect', value='Activate 1 of these effects:\n● Discard 1 "Devoted Servant" card; return 1 card on the field to the hand.\n● Banish up to 2 "Devoted Servant" card from your GY: banish the same number of cards from your opponent\'s GY.\n● Shuffle up to 3 of your banished "Devoted Servant" cards into your Deck; inflict 500 damage to your opponent for each.\nYou can only activate 1 "Devoted Servant\'s Reinforcements" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c186(bot))