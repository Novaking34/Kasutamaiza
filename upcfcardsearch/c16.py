import discord
from discord.ext import commands
from discord.utils import get

class c16(commands.Cog, name="c16"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Quoroq_Temporal_Justiciar', aliases=['c16'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Quoroq, Temporal Justiciar',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2320737.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Temporal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Rock/Effect (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (2000/2000)', inline=False)
        embed.add_field(name='Monster Effect', value='During your Main Phase: You can Fusion Summon 1 Aqua, Pyro or Rock Fusion Monster from your Extra Deck banishing cards from your hand, field, or either players GY as Fusion Material. During the Main Phase (Quick Effect): You can banish this card from your GY, then target 1 Rock "Temporal" monster you control; apply its effect on the field. (The monster\'s activation requirements do not need to be correct). You can only activate each effect of "Quoroq, Temporal Justiciar" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c16(bot))