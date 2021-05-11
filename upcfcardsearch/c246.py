import discord
from discord.ext import commands
from discord.utils import get

class c246(commands.Cog, name="c246"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Magia_Dance_Sacramentum', aliases=['c246', 'Magia_11'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Magia Dance Sacramentum',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359467.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Magia)', inline=True)
        embed.add_field(name='Type', value='Trap/Counter', inline=False)
        embed.add_field(name='Card Effect', value='When a card or effect is activated: Banish 2 "Magia" cards from your GY; negate the activation, and if you do, place that card on the bottom of the Deck. You can only activate 1 "Magia Dance Sacramentum" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c246(bot))