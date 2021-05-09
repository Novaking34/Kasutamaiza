import discord
from discord.ext import commands
from discord.utils import get

class c172(commands.Cog, name="c172"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Phantaclysmic_Zombie', aliases=['c172', 'Phantaclysms_5'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Phantaclysmic Zombie',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2344794.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Phantaclysms)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Zombie/Effect (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='2 (1200/0)', inline=False)
        embed.add_field(name='Monster Effect', value='This card can attack directly. If a "Phantaclysm" card is destroyed and sent to the GY: You can Special Summon this card from your hand, then, if the card was destroyed by an opponent\'s card or effect, draw 1 card. You can only activate the effect of "Phantaclysmic Zombie" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c172(bot))