import discord
from discord.ext import commands
from discord.utils import get

class c205(commands.Cog, name="c205"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Manoeuvre_Synthetic_Motion', aliases=['c205', 'Scorn_Operative_12'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Manoeuvre - Synthetic Motion',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2348918.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Scorn_Operative)', inline=True)
        embed.add_field(name='Type', value='Trap/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='Once per turn: You can discard 1 card, then target 1 "Scorn Operative" monster you control and 1 card your opponent controls in the same column, OR a Field Spell you control and a card in your opponent\'s Field Zone; negate the effects of your opponent\'s card, and if you do, destroy it. Then, if you targeted a monster with less ATK than your "Scorn Operative" monster by this effect: You can inflict the difference to your opponent as battle damage. You can only control 1 "Manoeuvre - Synthetic Motion".', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c205(bot))