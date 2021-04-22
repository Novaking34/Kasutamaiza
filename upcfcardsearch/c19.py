import discord
from discord.ext import commands
from discord.utils import get

class c19(commands.Cog, name="c19"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Vaera_Temporal_Magistrate', aliases=['c19'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Vaera, Temporal Magistrate',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2320746.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Temporal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Pyro/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (1500/1500)', inline=False)
        embed.add_field(name='Monster Effect', value='During your Main Phase: You can Special Summon 1 of your banished non-Pyro "Temporal" monster. During the Main Phase (Quick Effect): You can banish this card from your GY, then target 1 Pyro "Temporal" monster you control; apply its effect on the field. (The monster\'s activation requirements do not need to be correct). You can only activate each effect of "Vaera, Temporal Magistrate" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c19(bot))