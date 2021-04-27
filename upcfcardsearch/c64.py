import discord
from discord.ext import commands
from discord.utils import get

class c64(commands.Cog, name="c64"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Sunny_Season_&_Tranquil_Weather', aliases=['c64','Season_&_3'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Sunny Season & Tranquil Weather',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321479.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Season &)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Pyro/Tuner/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (200/1800)', inline=False)
        embed.add_field(name='Monster Effect', value='If your opponent Special Summon a monster(s) (Quick Effect): You can discard this card; destroy 1 Special Summoned monster your opponent controls, then, if you have 5 or more "Season &" monster in your GY, inflict 1000 points of damage to your opponent. Your opponent can discard 1 monster to negate this card\'s effect.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c64(bot))