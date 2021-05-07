import discord
from discord.ext import commands
from discord.utils import get

class c185(commands.Cog, name="c185"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Devoted_Servant_Mansion', aliases=['c185', 'Devoted_Servant_7'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Devoted Servant Mansion',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2345152.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Devoted Servant)', inline=True)
        embed.add_field(name='Type', value='Spell/Field', inline=False)
        embed.add_field(name='Card Effect', value='When this card is activated: You can add 1 "Devoted Servant" monster from your Deck to your hand. Once per turn: You can activate one of the following effects.\n● Discard 1 card; add 1 "Devoted Servant" card from your GY to your hand.\n● Banish 1 card from your GY; return 1 banished "Devoted Servant" card to your GY.\n● Shuffle 1 of your banished cards into your Deck; banish 1 "Devoted Servant" card from your Deck.\nYou can only activate 1 "Mansion of Devotion" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c185(bot))