import discord
from discord.ext import commands
from discord.utils import get

class c84(commands.Cog, name="c84"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Prey_on_the_Weak', aliases=['c84'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Prey on the Weak',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321523.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='If this card is activated while you have more LP than your opponent: Take 700 damage. During the Battle Phase, your opponent must attack the monster you control with the lowest ATK (their choice, if tied). During the End Phase, if you have more LP than your opponent: Destroy this card.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c84(bot))