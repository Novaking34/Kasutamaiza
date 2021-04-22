import discord
from discord.ext import commands
from discord.utils import get

class c22(commands.Cog, name="c22"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Chrono_Temporal_Balance', aliases=['c22'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Chrono, Temporal Balance',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2320757.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Temporal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Pyro/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='9 (3000/3000)', inline=False)
        embed.add_field(name='Monster Effect', value='2 Aqua, Pyro and/or Rock monsters with different names\nDuring your Main Phase: Special Summon 1 "Temporal" monster from your GY. During the Main Phase (Quick Effect): You can banish this card from your GY, then target 1 Pyro "Temporal" monster you control; apply its effect on the field. (The monster\'s activation requirements do not need to be correct). You can only activate each effect of "Chrono, Temporal Balance" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c22(bot))