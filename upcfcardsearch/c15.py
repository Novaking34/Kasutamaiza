import discord
from discord.ext import commands
from discord.utils import get

class c15(commands.Cog, name="c15"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Qora_Temporal_Magistrate', aliases=['c15','Temporal_6'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Qora, Temporal Magistrate',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2320734.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Temporal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Rock/Effect (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (1500/1500)', inline=False)
        embed.add_field(name='Monster Effect', value='During your Main Phase: Return 1 banished non-Rock "Temporal" monster to your GY, and if you do, you can draw 1 card. During the Main Phase (Quick Effect): You can banish this card from your GY, then target 1 Rock "Temporal" monster you control; apply its effect on the field. (The monster\'s activation requirements do not need to be correct). You can only activate each effect of "Qora, Temporal Alchemist" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c15(bot))