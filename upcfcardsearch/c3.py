import discord
from discord.ext import commands
from discord.utils import get

class c3(commands.Cog, name="c3"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Reflect_Attack', aliases=['c3'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Reflect Attack',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2304615.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Quick-Play', inline=False)
        embed.add_field(name='Card Effect', value='When a monster declares an attack: Negate the attack, and if you do, destroy all other monsters the turn player controls', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c3(bot))