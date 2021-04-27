import discord
from discord.ext import commands
from discord.utils import get

class c70(commands.Cog, name="c70"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='A_Moment_of_Peace', aliases=['c70'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='A Moment of Peace',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321488.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='You can only activate this card during your Main Phase 1. Neither player can conduct their Battle Phase until the end of the next turn. If neither player controls a monster when this card is activated, gain 2000 LP.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c70(bot))