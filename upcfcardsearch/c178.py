import discord
from discord.ext import commands
from discord.utils import get

class c178(commands.Cog, name="c178"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Lich_of_Phantaclysms_Thanatos', aliases=['c178', 'Phantaclysms_11'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Lich of Phantaclysms, Thanatos')
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2344838.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Phantaclysms)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Psychic/Xyz/Effect (LIGHT)', inline=False)
        embed.add_field(name='Rank (ATK/DEF)', value='2 (1500/0)', inline=False)
        embed.add_field(name='Monster Effect', value='2 Level 2 monsters\nThis card can attack directly. When an opponent\'s monster activates its effect (except during the Damage Step): You can detach 2 material from this card; the activated effect becomes "Destroy 1 monster your opponent controls".', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c178(bot))