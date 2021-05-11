import discord
from discord.ext import commands
from discord.utils import get

class c223(commands.Cog, name="c223"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Lady_of_the_Night_Butterflies', aliases=['c223'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Lady of the Night Butterflies',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359068.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (200/200)', inline=False)
        embed.add_field(name='Monster Effect', value='You can discard this card and 1 LIGHT or DARK monster; draw 1 card. If this card is banished: You can target 1 of your banished LIGHT or DARK monsters, except "Lady of the Night Butterflies"; return that target to the GY, and if you do, add this card to your hand. You can only use each effect of "Lady of the Night Butterflies" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c223(bot))