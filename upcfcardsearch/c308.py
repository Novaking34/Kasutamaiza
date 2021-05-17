import discord
from discord.ext import commands
from discord.utils import get

class c308(commands.Cog, name="c308"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Red_Dusk', aliases=['c308'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Red Dusk',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361270.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='When a monster(s) is Summoned from the Extra Deck: You can pay 2000 LP; negate their effects, and if you do, destroy that monster(s).', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c308(bot))