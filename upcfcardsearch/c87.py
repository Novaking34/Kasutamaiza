import discord
from discord.ext import commands
from discord.utils import get

class c87(commands.Cog, name="c87"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Too_Cute_for_You!', aliases=['c87'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Too Cute for You!',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321528.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Add 1 "A-dora" monster from your GY to your hand OR Special Summon 1 "A-dora" monster from your hand. If this card is sent directly from your Deck to the GY while you control an "A-dora" monster: Draw 1 card, then if you only control "A-dora" monsters, Set this card directly from your GY to the field, but banish it when it leaves the field.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c87(bot))