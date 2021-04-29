import discord
from discord.ext import commands
from discord.utils import get

class c119(commands.Cog, name="c119"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Sacrificial_Discharge', aliases=['c119'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Sacrificial Discharge',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2328209.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Target 1 card you control; destroy it, and if you do, destroy all other cards in its column.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c119(bot))