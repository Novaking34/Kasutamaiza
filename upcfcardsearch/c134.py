import discord
from discord.ext import commands
from discord.utils import get

class c134(commands.Cog, name="c134"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Da_Princess_Blam!', aliases=['c134'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Da Princess Blam!',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334903.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Psychic/Normal (WIND)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (1500/500)', inline=False)
        embed.add_field(name='Monster Effect', value='She roams the free forest and is looking for her prince. Determined to rule her own kingdom, she takes no prisoners.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c134(bot))