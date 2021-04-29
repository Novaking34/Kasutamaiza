import discord
from discord.ext import commands
from discord.utils import get

class c115(commands.Cog, name="c115"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Machine_Lord_the_Shining', aliases=['c115', 'Machine_Lord_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Machine Lord the Shining',
                              color=0xcccccc)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321579.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Machine Lord)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Synchro/Effect (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='7 (2500/2400)', inline=False)
        embed.add_field(name='Monster Effect', value='1 "Machine Lord" Tuner + 1+ non Tuner monsters\nIf this card is Synchro Summoned using only Machine monsters, this card cannot be destroyed by battle or targeted by your opponent\'s card effects. Once per turn: You can target 1 Level 5 or lower Machine monster in your GY; banish that monster, and if you do, inflict 700 damage to your opponent. You can only Special Summon 1 "Machine Lord the Shining" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c115(bot))