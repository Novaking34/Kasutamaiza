import discord
from discord.ext import commands
from discord.utils import get

class c190(commands.Cog, name="c190"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Head_of_the_Mechanical_Servants', aliases=['c190', 'Devoted_Servant_11'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Head of the Mechanical Servants',
                              color=0xcccccc)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2345157.jpg?version=2')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Devoted Servant)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Synchro/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='8 (2500/2500)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Tuner + "Head of the Devoted Servants"\nCannot be targeted by your opponent\'s card effects. If a monster is Special Summoned from the hand: You can target 1 card on the field; return it to the hand. If this card is destroyed by battle or card effect: You can target 1 level 7 or lower "Mechanical Servant" or "Devoted Servant" monster in your GY: Special Summon it. You can only use each effect of "Head of the Mechanical Servants" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c190(bot))