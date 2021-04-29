import discord
from discord.ext import commands
from discord.utils import get

class c126(commands.Cog, name="c126"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Grudge_of_the_Orcs', aliases=['c126'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Grudge of the Orcs',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334838.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Until the End Phase, the ATK/DEF of all monsters on the field becomes their original ATK/DEF.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c126(bot))