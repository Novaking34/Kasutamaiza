import discord
from discord.ext import commands
from discord.utils import get

class c265(commands.Cog, name="c265"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Choixier_Prayer', aliases=['c265', 'Choixier_3'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Choixier Prayer',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360654.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Choixier)', inline=True)
        embed.add_field(name='Type', value='Spell/Quick-Play', inline=False)
        embed.add_field(name='Card Effect', value='Activate 1 of the followings effects;\n● 1 face-up monster you control cannot be destroyed until the End Phase, additionally, all Battle Damage taken involving that monster becomes 0.\n● During the End Phase of the turn this card was activated: Set up to 2 Normal Spells from your GY to your field that were sent to the GY this turn.\nYou can only activate each effect of "Choixier Prayer" once per turn.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c265(bot))