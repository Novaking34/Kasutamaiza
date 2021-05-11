import discord
from discord.ext import commands
from discord.utils import get

class c289(commands.Cog, name="c289"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Cloudjumper_Dragon', aliases=['c289'])    
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Cloudjumper Dragon',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361108.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Dragon/Normal (WIND)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='6 (2000/1000)', inline=False)
        embed.add_field(name='Lore Text', value='If one were to look to the sky on a cloudy day, they may see this creature leaping through the heavens.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c289(bot))