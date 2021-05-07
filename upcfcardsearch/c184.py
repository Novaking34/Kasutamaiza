import discord
from discord.ext import commands
from discord.utils import get

class c184(commands.Cog, name="c184"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Head of the Devoted Servants', aliases=['c184', 'Devoted_Servant_6'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Head of the Devoted Servants',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2345151.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Devoted Servant)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (2000/2000)', inline=False)
        embed.add_field(name='Monster Effect', value='(Quick Effect): You can reveal this card in your hand, then target 1 "Devoted Servant" monster you control, except "Head of the Devoted Servants", Special Summon this card, and if you do, return that monster to the hand. If this card is used as Synchro Material and sent to the GY: You can add 1 "Devoted Servant" card from your GY to your hand, except "Head of the Devoted Servants". You can only use each effect of "Head of the Devoted Servants" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c184(bot))