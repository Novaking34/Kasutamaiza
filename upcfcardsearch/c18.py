import discord
from discord.ext import commands
from discord.utils import get

class c18(commands.Cog, name="c18"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Sylvette_Temporal_Queen', aliases=['c18'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Sylvette, Temporal Queen',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2320745.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Temporal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Aqua/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='7 (2500/2500)', inline=False)
        embed.add_field(name='Monster Effect', value='During your Main Phase: You can target 1 Spell/Trap your opponent controls; Return it to the hand, and if you do, until your next End Phase, its effects are negated, as well as the activated effects and effects on the field of cards with the same original name. During the Main Phase (Quick Effect): You can banish this card from your GY, then target 1 Aqua "Temporal" monster you control; apply its effect on the field. (The monster\'s activation requirements do not need to be correct). You can only activate each effect of "Sylvette, Temporal Queen" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c18(bot))