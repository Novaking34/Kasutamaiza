import discord
from discord.ext import commands
from discord.utils import get

class c217(commands.Cog, name="c217"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Ches-Neko_Kotori', aliases=['c217', 'Ches-Neko_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Ches-Neko Kotori',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2356402.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Ches-Neko)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Beast-Warrior/Effect (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (1200/1000)', inline=False)
        embed.add_field(name='Monster Effect', value='If your opponent Special Summons a Pendulum or Xyz monster(s): You can discard this card, then target 1 of those monsters; destroy it. You can only use the effect of "Ches-Neko Kotori" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c217(bot))