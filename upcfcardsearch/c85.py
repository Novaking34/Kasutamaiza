import discord
from discord.ext import commands
from discord.utils import get

class c85(commands.Cog, name="c85"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Shifting_Gear', aliases=['c85'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Shifting Gear',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321524.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Quick-Play', inline=False)
        embed.add_field(name='Card Effect', value='Target 1 Machine monster you control and 1 Machine monster in the GY with an equal or lower Level; return the first target to your hand, then Special Summon the second target from your GY in Defense Position. Until the end of this turn, you cannot Special Summon Machine monsters from your hand. You can only activate "Shifting Gear" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c85(bot))