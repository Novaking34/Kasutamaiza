import discord
from discord.ext import commands
from discord.utils import get

class c51(commands.Cog, name="c51"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='A-dorawisp', aliases=['c51','A-dora_3'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='A-dorawisp',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321453.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (A-dora)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (300/200)', inline=False)
        embed.add_field(name='Monster Effect', value='Any battle damage involving this card is reduced to 0. You can Tribute this Normal Summoned card; Special Summon 1 Level 4 or lower Normal Monster from your Deck. You can only activate this effect of "A-dorawisp" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c51(bot))