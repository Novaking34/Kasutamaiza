import discord
from discord.ext import commands
from discord.utils import get

class c221(commands.Cog, name="c221"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Ice_Lake_Lady', aliases=['c221'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Ice Lake Lady',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359060.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (0/0)', inline=False)
        embed.add_field(name='Monster Effect', value='If you control no monsters (Quick Effect): You can discard this card, then target 1 Effect Monster your opponent controls; negate the effects of that face-up monster while it is on the field, also that face-up monster cannot attack.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c221(bot))