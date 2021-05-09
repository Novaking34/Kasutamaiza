import discord
from discord.ext import commands
from discord.utils import get

class c125(commands.Cog, name="c125"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Skeletal_Shogun', aliases=['c125'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Skeletal Shogun',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334816.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Zombie/Normal (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (2000/1000)', inline=False)
        embed.add_field(name='Lore Text', value='The desecrated corpse of a formidable warrior. After a year of service to the necromancer that raised it, it proved worthy of commanding the entire army of undead. While it may look dim, the Skeletal Shogun is a strategic genius.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c125(bot))