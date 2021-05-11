import discord
from discord.ext import commands
from discord.utils import get

class c294(commands.Cog, name="c294"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Augmented_Striker', aliases=['c294'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Augmented Striker',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361136.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (550/2150)', inline=False)
        embed.add_field(name='Monster Effect', value='If this card is in your hand (Quick Effect): You can discard 1 card, then target 1 Machine monster you control; banish it until the End Phase, then Special Summon this card. If Summoned this way: You can target 1 card on the field; return it to the hand. You can only Special Summon "Augmented Striker(s)" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c294(bot))