import discord
from discord.ext import commands
from discord.utils import get

class c132(commands.Cog, name="c132"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Atamotona', aliases=['c132'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Atamotona',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334895.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Normal (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='7 (2050/2650)', inline=False)
        embed.add_field(name='Lore Text', value='MECHA-MECHA! Machine...loading...updating......GO! ATAMOTONA FULL THROTTLE!!!', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c132(bot))