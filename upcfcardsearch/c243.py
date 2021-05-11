import discord
from discord.ext import commands
from discord.utils import get

class c243(commands.Cog, name="c243"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Magia_Dance_Immitis', aliases=['c243', 'Magia_8'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Magia Dance Immitis',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359457.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Magia)', inline=True)
        embed.add_field(name='Type', value='Spell/Quick-Play', inline=False)
        embed.add_field(name='Card Effect', value='Destroy up to 2 other "Magia" cards you control or in your hand, then, if you destroyed 2 cards with this effect, draw 1 card. You can only activate 1 "Magia Dance Immitis" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c243(bot))