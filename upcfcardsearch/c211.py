import discord
from discord.ext import commands
from discord.utils import get

class c211(commands.Cog, name="c211"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Scorn_Operative_Turncoat', aliases=['c211','Scorn_Operative_17'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Scorn Operative - Turncoat',
                              color=0x00008B)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2348936.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Scorn Operative)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Link/Effect (DARK)', inline=False)
        embed.add_field(name='Link Rating (ATK/Link Arrows)', value='1 (1500/⬇️)', inline=False)
        embed.add_field(name='Monster Effect', value='1 "Scorn Operative" monster with exactly 2000 ATK\nQuick Effect): You can return 1 "Scorn Operative" non-Effect Monster you control to the hand or Extra Deck; reduce the ATK of 1 monster on the field by 1500, and if you do, increase this card\'s ATK by 1000 until the End Phase.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c211(bot))