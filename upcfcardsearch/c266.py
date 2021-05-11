import discord
from discord.ext import commands
from discord.utils import get

class c266(commands.Cog, name="c266"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Choixier_Release', aliases=['c266', 'Choixier_4'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Choixier Release',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360657.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Choixier)', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Activate 1 of the followings effects;\n● Special Summon 1 monster from your GY whose Level is greater than or equal to the combined number of cards in each player\'s hand.\n● Special Summon 1 monster from either player\'s GY but its effects are negated.\nYou can only activate each effect of "Choixier Release" once per turn.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c266(bot))