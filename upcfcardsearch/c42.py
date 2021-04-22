import discord
from discord.ext import commands
from discord.utils import get

class c42(commands.Cog, name="c42"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='A_Gift_from_the_Divine', aliases=['c42'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='A Gift from the Divine',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321412.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Banish 1 Divine-Beast monster from your hand; draw 2 cards. You can only activate 1 "A Gift from the Divine" per turn', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c42(bot))