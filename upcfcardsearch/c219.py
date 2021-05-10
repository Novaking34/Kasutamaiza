import discord
from discord.ext import commands
from discord.utils import get

class c219(commands.Cog, name="c219"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Ches-Neko_Tsukasa', aliases=['c219', 'Ches-Neko_3'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Ches-Neko Tsukasa',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2356406.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Ches-Neko)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Beast-Warrior/Effect (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (1200/1000)', inline=False)
        embed.add_field(name='Monster Effect', value='If your opponent Special Summons a Fusion or Synchro monster(s): You can discard this card, then target 1 of those monsters; destroy it. You can only use the effect of "Ches-Neko Tsukasa" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c219(bot))