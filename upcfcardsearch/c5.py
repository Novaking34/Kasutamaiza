import discord
from discord.ext import commands
from discord.utils import get

class c5(commands.Cog, name="c5"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Futureproof', aliases=['c5'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Futureproof',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2308464.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='During the next turn after this card\'s activation, your opponent cannot target cards you control with card effects. You can only activate 1 "Futureproof" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c5(bot))