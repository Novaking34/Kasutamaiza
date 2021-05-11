import discord
from discord.ext import commands
from discord.utils import get

class c291(commands.Cog, name="c291"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Rage_of_the_Dragon', aliases=['c291'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Rage of the Dragon',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361114.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='If you control only Dragon monsters (min. 2), target 2 cards on your opponent\'s field; destroy them. During the Main Phase, except the turn this card was sent to the GY, you can banish this card from your GY: Dragon monsters you control gain 100 ATK for each Dragon monster you control.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c291(bot))