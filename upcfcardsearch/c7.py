import discord
from discord.ext import commands
from discord.utils import get

class c7(commands.Cog, name="c7"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Research_Rage_Gene', aliases=['c7'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Research - Rage Gene',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2308473.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='You can discard 1 card, then target 1 monster you control and 1 card your opponent controls in the same column; destroy your opponent\'s card, then, if you destroyed a monster with less ATK than the ATK of your monster you targeted by this effect, inflict damage to your opponent equal to the difference. You can only use this effect of "Research - Rage Gene" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c7(bot))