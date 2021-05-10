import discord
from discord.ext import commands
from discord.utils import get

class c214(commands.Cog, name="c214"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Double_Magician', aliases=['c214'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Double Magician',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2356377.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Fusion/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (2100/2000)', inline=False)
        embed.add_field(name='Monster Effect', value='2 Xyz, Synchro and/or Fusion monsters with different names\n(Quick Effect): Target 1 face-up Spell you control; apply its effect. If this Fusion Summoned card is destroyed by battle or by card effect: You can Set 1 Spell/Trap from your GY directly to the field. You can only activate each effect of "Double Magician" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c214(bot))