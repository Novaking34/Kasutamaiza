import discord
from discord.ext import commands
from discord.utils import get

class c232(commands.Cog, name="c232"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Compulsory_Recoil_Device', aliases=['c232'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Compulsory Recoil Device',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359205.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='Once per turn: You can discard 1 card, then target 1 monster on the field; return it to the hand.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c232(bot))