import discord
from discord.ext import commands
from discord.utils import get

class c120(commands.Cog, name="c120"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Spring\'s_Herald', aliases=['c120'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Spring\'s Herald',
                              color=0x00008B)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2328211.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Link/Effect (EARTH)', inline=False)
        embed.add_field(name='Link Rating (ATK/Link Arrows)', value='2 (500/⬆️⬇️)', inline=False)
        embed.add_field(name='Monster Effect', value='2 Effect Monsters\nYou can banish 1 monster that this card points to until your next Standby Phase. You can target 3 of your banished monsters or 3 of your opponent\'s banished monsters; shuffle them into the Deck, and if you do, draw 1 card. You can only use each effect of "Spring\'s Herald" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c120(bot))