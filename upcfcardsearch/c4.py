import discord
from discord.ext import commands
from discord.utils import get

class c4(commands.Cog, name="c4"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Rose_Knight_of_Evening_Light', aliases=['c4'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Rose Knight of Evening Light')
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2304691.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Warrior/Xyz/Effect (LIGHT)', inline=False)
        embed.add_field(name='Rank (ATK/DEF)', value='4 (2500/2000)', inline=False)
        embed.add_field(name='Monster Effect', value='2 Level 4 monsters\nIf a monster(s) you control is destroyed by a card effect: This card gains ATK equal to half the total original ATK of the destroyed monsters. If this card\'s attack is negated: You can detach 1 material; this card can make a second attack during each Battle Phase this turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c4(bot))