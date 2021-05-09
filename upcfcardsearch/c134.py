import discord
from discord.ext import commands
from discord.utils import get

class c134(commands.Cog, name="c134"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Da_Prince_Charmed!', aliases=['c134'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Da Prince Charmed!',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334900.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Aqua/Normal (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (1800/100)', inline=False)
        embed.add_field(name='Lore Text', value='He is in search for his princess, hoping to break the curse that is upon him.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c134(bot))