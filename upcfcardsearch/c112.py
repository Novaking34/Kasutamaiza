import discord
from discord.ext import commands
from discord.utils import get

class c112(commands.Cog, name="c112"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Villianous_Akuma_Stormy_Weather', aliases=['c112', 'Villianous_Akuma_1', 'Miraculous_Ladybug_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Villianous Akuma Stormy Weather',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321574.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Villianous Akuma/Miraculous Ladybug)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Aqua/Fusion/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='6 (1000/2000)', inline=False)
        embed.add_field(name='Monster Effect', value='2 monsters in the Main Monster Zone, including 1 WATER monster\nMust be Fusion Summoned. If this card is Fusion Summoned: Change control of this card. During your Standby Phase: Destroy 1 other card you control, and if you cannot, take 500 damage. If this card on the field is returned to the Extra Deck: The player who controlled this card takes 500 damage.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c112(bot))