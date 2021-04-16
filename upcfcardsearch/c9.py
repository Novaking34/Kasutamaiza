import discord
from discord.ext import commands
from discord.utils import get

class c9(commands.Cog, name="c9"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Worldweave_Unravelled', aliases=['c9'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Worldweave Unravelled',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2308763.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='During your opponent\'s turn, each time your opponent activates a card or effect, place 1 Instability Counter on this card (max. 10) immediately after it resolves. During your opponent\'s turn, if this card has 10 Instability Counters: It becomes the End Phase, also remove all Instability Counters on this card.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c9(bot))