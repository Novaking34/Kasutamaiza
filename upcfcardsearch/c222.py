import discord
from discord.ext import commands
from discord.utils import get

class c222(commands.Cog, name="c222"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Injection_Fairy_Leah', aliases=['c222'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Injection Fairy Leah',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359063.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (400/1500)', inline=False)
        embed.add_field(name='Monster Effect', value='During the Damage Step, if this card is battling an opponent\'s monster (Quick Effect): You can pay LP in multiples of 100; your opponent\'s monster loses ATK equal to the LP you paid, and if it does, this card gains that lost ATK during damage calculation only.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c222(bot))