import discord
from discord.ext import commands
from discord.utils import get

class c209(commands.Cog, name="c209"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Scorn_Operative_Crescent', aliases=['c209','Scorn_Operative_15'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Scorn Operative - Crescent',
                              color=0x00008B)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2348926.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Scorn Operative)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Link/Effect (EARTH)', inline=False)
        embed.add_field(name='Link Rating (ATK/Link Arrows)', value='1 (500/↙️)', inline=False)
        embed.add_field(name='Monster Effect', value='1 "Scorn Operative" non-Effect Monster\nThis card gains 250 ATK for each card you control in the same column as a "Scorn Operative" monster. This card gains 1000 ATK for each non-Effect Monster(s) that was Summoned during this turn. If this card has 2500 or more ATK: You can add 1 "Scorn Operative" monster from your Deck to your hand. You can only use this effect of "Scorn Operative - Crescent" once per turn. If this card with 2500 or more ATK battles: its ATK becomes 2000.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c209(bot))