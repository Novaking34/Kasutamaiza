import discord
from discord.ext import commands
from discord.utils import get

class c177(commands.Cog, name="c177"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Phantaclysmic_Phenomena', aliases=['c177', 'Phantaclysms_10'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Phantaclysmic Phenomena',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2344831.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Phantaclysms)', inline=True)
        embed.add_field(name='Type', value='Trap/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='When this card is activated: Target 1 "Phantaclysmic" monster in your GY; Special Summon that target. If a face-up "Phantaclysmic" card you control is destroyed by an opponent\'s card or effect, while this card is face-up on the field: You can Set this card.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c177(bot))