import discord
from discord.ext import commands
from discord.utils import get

class c47(commands.Cog, name="c47"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='A_la_Mode_Donna', aliases=['c47'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='A la Mode Donna',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321443.jpg?version=2')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (100/2500)', inline=False)
        embed.add_field(name='Monster Effect', value='(Quick Effect): You can discard this card, then target 1 monster your opponent\'s control; this turn, that card cannot be destroyed by battle or card effect and cannot be used as Material for a Summoning of an Extra Deck monster, but you cannot activate monster effects during your next turn. You can only use 1 "A la Mode Donna" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c47(bot))