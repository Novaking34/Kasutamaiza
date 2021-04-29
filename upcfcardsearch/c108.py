import discord
from discord.ext import commands
from discord.utils import get

class c108(commands.Cog, name="c108"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='King_Frost', aliases=['c108'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='King Frost',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321567.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Aqua/Fusion/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='2 (200/300)', inline=False)
        embed.add_field(name='Monster Effect', value='2 WATER monsters\nIf this card is Special Summoned during your opponent\'s turn, banish it when it leaves the field. If this card is Special Summoned: The turn player cannot conduct their Battle Phase this turn, but they can Normal Summon/Set 1 monster this turn in addition to their Normal Summon/Set this turn (you can only gain this effect once per turn.) Once per turn, during the Main Phase 1 (Quick Effect): You can target 1 card on the field; this turn, that card cannot activate its effects', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c108(bot))