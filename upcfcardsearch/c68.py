import discord
from discord.ext import commands
from discord.utils import get

class c68(commands.Cog, name="c68"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Vupei', aliases=['c68'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Vupei',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321485.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Aqua/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (0/1000)', inline=False)
        embed.add_field(name='Monster Effect', value='If this card is Normal or Flip Summoned: Change it to face-up Defense Position. During your End Phase: You can send this face-up card to the GY, then target 1 Level 3 or lower monster in either GY that was destroyed this turn; Special Summon it to your field in Defense Position. You can only activate this effect of "Vupei" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c68(bot))