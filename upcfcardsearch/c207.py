import discord
from discord.ext import commands
from discord.utils import get

class c207(commands.Cog, name="c207"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Scorn_Operative_Pyre', aliases=['c207', 'Scorn_Operative_13'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Scorn Operative - Pyre',
                              color=0xcccccc)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2348919.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Scorn Operative)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Synchro/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='6 (2000/2400)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Tuner + 1 non-Tuner monster', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c207(bot))