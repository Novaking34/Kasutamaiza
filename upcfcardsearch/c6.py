import discord
from discord.ext import commands
from discord.utils import get

class c6(commands.Cog, name="c6"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Plague_of_Doubt', aliases=['c6'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Plague of Doubt',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2308467.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Activate 1 of these effects:\n● Negate the effects of 2 monsters your opponent controls in adjacent Main Monster Zones to each other, also, after that, until the end of the next turn, the activated effects of your monsters in those negated cards\' columns are negated.\n● Destroy 1 monster and Spell/Trap your opponent controls in the same column, also, after that, until the end of the next turn, the activated effects of your cards in that column are negated.\nYou can only use this effect of "Plague of Doubt" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c6(bot))