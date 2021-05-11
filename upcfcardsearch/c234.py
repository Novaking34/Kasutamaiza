import discord
from discord.ext import commands
from discord.utils import get

class c234(commands.Cog, name="c234"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Sun_Deity_Susanowo', aliases=['c234'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Sun Deity Susanowo',
                              color=0xcccccc)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359215.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Synchro/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='8 (3000/2500)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Tuner + 1 non-Tuner monster\nOnce per turn (Quick Effect): You can target 1 card you control and 1 monster your opponent controls; destroy them. If this card on the field is destroyed, during the Standby Phase of the next turn: You can Special Summon 1 "Moon Deity Tsukuyomi" from your GY.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c234(bot))