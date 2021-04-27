import discord
from discord.ext import commands
from discord.utils import get

class c52(commands.Cog, name="c52"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Accursed_Jar', aliases=['c52'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Accursed Jar',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321455.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Rock/Effect (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (0/0)', inline=False)
        embed.add_field(name='Monster Effect', value='Any battle damage involving this card is reduced to 0. You can Tribute this Normal Summoned card; add 1 Level 4 or lower Normal Monster from your Deck to your hand. You can only activate this effect of "A-dorawisp" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c52(bot))