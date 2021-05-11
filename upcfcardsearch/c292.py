import discord
from discord.ext import commands
from discord.utils import get

class c292(commands.Cog, name="c292"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Dragon\'s_Respite', aliases=['c292'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Dragon\'s Respite',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361120.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='During your End Phase: If you did not attack this turn, draw 1 card and all Dragon monsters you control gain 200 ATK until the next End Phase. If this card is destroyed by an opponent\'s card effect and send to the GY: Special Summon 1 Level 4 or lower Dragon monster from your Deck.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c292(bot))