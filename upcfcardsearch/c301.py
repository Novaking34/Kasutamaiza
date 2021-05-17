import discord
from discord.ext import commands
from discord.utils import get

class c301(commands.Cog, name="c301"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Mage\'s_Magic', aliases=['c301'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Mage\'s Magic',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361242.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Quick-Play', inline=False)
        embed.add_field(name='Card Effect', value='Target 1 Set Spell/Trap you control; banish that target, then banish 2 Spell/Traps on the field. You cannot activate the targeted card this Chain.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c301(bot))