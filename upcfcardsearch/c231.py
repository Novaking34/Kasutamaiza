import discord
from discord.ext import commands
from discord.utils import get

class c231(commands.Cog, name="c231"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='A_Gift_from_the_Dark_Bride', aliases=['c231'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='A Gift from the Dark Bride',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359201.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Counter', inline=False)
        embed.add_field(name='Card Effect', value='When a monster(s) would be Special Summoned, or a monster effect is activated: Negate the Summon or activation, and if you do, destroy that card. After this card resolves, Set it to your opponent\'s Spell & Trap Zone instead of sending it to the GY.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c231(bot))