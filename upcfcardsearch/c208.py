import discord
from discord.ext import commands
from discord.utils import get

class c208(commands.Cog, name="c208"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Scorn_Operative_Sundown', aliases=['c208', 'Scorn_Operative_14'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Scorn Operative - Sundown',
                              color=0xcccccc)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2348923.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Scorn Operative)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Tuner/Synchro/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='2 (500/500)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Tuner + 1 non-Tuner monster\nThis card gains 2000 ATK for each "Scorn Operatives - Sundown" in the GY.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c208(bot))