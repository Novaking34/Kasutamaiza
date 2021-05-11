import discord
from discord.ext import commands
from discord.utils import get

class c225(commands.Cog, name="c225"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Time_Enchanter_Tifa', aliases=['c225'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Time Enchanter Tifa',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359074.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Tuner/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (0/0)', inline=False)
        embed.add_field(name='Monster Effect', value='During your opponent\'s Main Phase or Battle Phase (Quick Effect): You can discard this card; apply the appropriate effect depending on the current phase:\n● Main Phase 1: Skip this turn\'s Battle Phase.\n● Battle Phase: Skip your opponent\'s Main Phase 2.\n● Main Phase 2: Skip your opponent\'s next Main Phase 1.\nYou can only use the effect of "Time Enchanter Tifa" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c225(bot))