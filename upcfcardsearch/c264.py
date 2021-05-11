import discord
from discord.ext import commands
from discord.utils import get

class c264(commands.Cog, name="c264"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Choixier_Perseverance', aliases=['c264', 'Choixier_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Choixier Perseverance',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360649.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Choixier)', inline=True)
        embed.add_field(name='Type', value='Spell/Quick-Play', inline=False)
        embed.add_field(name='Card Effect', value='Activate 1 of the followings effects;\n● 1 face-up monster you control becomes unaffected by other card effects until the end of the turn.\n● During the End Phase of the turn this card was activated: Return up to 2 monsters from your GY to your hand that were sent there this turn.\nYou can only activate each effect of "Choixier Perseverance" once per turn.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c264(bot))