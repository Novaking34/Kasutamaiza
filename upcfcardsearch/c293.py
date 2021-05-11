import discord
from discord.ext import commands
from discord.utils import get

class c293(commands.Cog, name="c293"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='A_Fierce_Kitten', aliases=['c293'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='A Fierce Kitten',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361133.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Beast-Warrior/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (1700/1500)', inline=False)
        embed.add_field(name='Monster Effect', value='When exactly 1 card or effect would be negated by a card or effect (Quick Effect): You can banish this card from your hand; negate the activation. You can only use this effect of "A Fierce Kitten" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c293(bot))