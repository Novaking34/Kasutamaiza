import discord
from discord.ext import commands
from discord.utils import get

class c12(commands.Cog, name="c12"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Arte_Temporal_Magistrate', aliases=['c12','Temporal_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Arte, Temporal Magistrate',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2320725.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Temporal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Aqua/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (1500/1500)', inline=False)
        embed.add_field(name='Monster Effect', value='During your Main Phase: You can send 1 non-Aqua "Temporal" monster from your Deck to the GY. During the Main Phase (Quick Effect): You can banish this card from your GY, then target 1 Aqua "Temporal" monster you control; apply its effect on the field. (The monster\'s activation requirements do not need to be correct). You can only activate each effect of "Arte, Temporal Magistrate" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c12(bot))