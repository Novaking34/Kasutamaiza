import discord
from discord.ext import commands
from discord.utils import get

class c20(commands.Cog, name="c20"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Varatora_Temporal_Justiciar', aliases=['c20'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Varatora, Temporal Justiciar',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2320748.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Temporal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Pyro/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (2000/2000)', inline=False)
        embed.add_field(name='Monster Effect', value='You can target 1 face-up Pyro monster you control; it gains 1000 ATK until your next End Phase. During the Main Phase (Quick Effect): You can banish this card from your GY, then target 1 Pyro "Temporal" monster you control; apply its effect on the field. (The monster\'s activation requirements do not need to be correct). You can only activate each effect of "Varatora, Temporal Justiciar" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c20(bot))