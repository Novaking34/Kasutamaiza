import discord
from discord.ext import commands
from discord.utils import get

class c233(commands.Cog, name="c233"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Moon_Deity_Tsukuyomi', aliases=['c233'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Moon Deity Tsukuyomi',
                              color=0xcccccc)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359209.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Synchro/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='8 (2500/3000)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Tuner + 1 non-Tuner monster\nOnce per turn, when your opponent activates a monster effect (Quick Effect): You can target 1 card you control; destroy it, and if you do, negate that activation. If this card on the field is destroyed, during the Standby Phase of the next turn: You can Special Summon 1 "Sun Deity Susanowo" from your GY.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c233(bot))