import discord
from discord.ext import commands
from discord.utils import get

class c100(commands.Cog, name="c100"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Vigil_of_Foresight', aliases=['c100'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Vigil of Foresight',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321549.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='When this card is activated: Banish 1 Level 9 or higher monster from your Deck. During your 2nd Standby Phase after this card\'s activation: You can send this face-up card to the GY; Special Summon the monster banished by this effect, but shuffle it into your Deck during the End Phase. You can only activate 1 "Vigil of Foresight" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c100(bot))