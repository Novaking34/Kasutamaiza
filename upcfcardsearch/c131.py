import discord
from discord.ext import commands
from discord.utils import get

class c131(commands.Cog, name="c131"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Aquamarine_the_Water_Bearing_Queen', aliases=['c131'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Aquamarine the Water Bearing Queen',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334891.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Aqua/Normal (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (500/750)', inline=False)
        embed.add_field(name='Lore Text', value='She hits the swimming pool scene, water so clean, they think she is so mean, but my girl Aquamarine is a Water Bearing Queen!', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c131(bot))