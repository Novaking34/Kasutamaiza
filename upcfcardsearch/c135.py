import discord
from discord.ext import commands
from discord.utils import get

class c135(commands.Cog, name="c135"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Dante\'s_Beast', aliases=['c135'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Dante\'s Beast',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334905.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Zombie/Normal (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (2300/2000)', inline=False)
        embed.add_field(name='Lore Text', value='It is said that deep in the depths of the Underworld, Dante tamed a wicked and powerful monster that holds great power. Without a soul to tether to, this beast power is unmatched, only rivaled by the Light itself.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c135(bot))