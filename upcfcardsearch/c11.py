import discord
from discord.ext import commands
from discord.utils import get

class c11(commands.Cog, name="c11"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Arabora_Temporal_King', aliases=['c11','Temporal_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Arabora, Temporal King',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2320722.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Temporal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Pyro/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='7 (2500/2500)', inline=False)
        embed.add_field(name='Monster Effect', value='During your Main Phase: You can Special Summon 1 "Temporal" monster from your hand. During the Main Phase (Quick Effect): You can banish this card from your GY, then target 1 Pyro "Temporal" monster you control; apply its effect on the field. (The monster\'s activation requirements do not need to be correct). You can only activate each effect of "Arabora, Temporal King" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c11(bot))