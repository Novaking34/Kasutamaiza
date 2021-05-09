import discord
from discord.ext import commands
from discord.utils import get

class c164(commands.Cog, name="c164"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Thundara', aliases=['c164'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Thundara',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2344695.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3=', inline=True)
        embed.add_field(name='Type (Attribute)', value='Thunder/Normal (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='7 (2100/800)', inline=False)
        embed.add_field(name='Lore Text', value='Master of the sky\'s and watchers of the clouds, Thundara lighting bolt never misses it mark and can destroy even the mightiest of beast.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c164(bot))