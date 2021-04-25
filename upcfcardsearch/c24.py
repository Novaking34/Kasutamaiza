import discord
from discord.ext import commands
from discord.utils import get

class c24(commands.Cog, name="c24"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Tide_Temporal_Balance', aliases=['c24','Temporal_14'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Tide, Temporal Balance',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321291.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Temporal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Aqua/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='9 (3000/3000)', inline=False)
        embed.add_field(name='Monster Effect', value='2 Aqua, Pyro and/or Rock monsters with different names\nDuring your Main Phase: You can target 1 card you control and 1 card your opponent controls; return them to the hand. During the Main Phase (Quick Effect): You can banish this card from your GY, then target 1 Aqua "Temporal" monster you control; apply its effect on the field. (The monster\'s activation requirements do not need to be correct). You can only activate each effect of "Tide, Temporal Balance" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c24(bot))