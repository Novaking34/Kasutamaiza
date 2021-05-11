import discord
from discord.ext import commands
from discord.utils import get

class c290(commands.Cog, name="c290"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Facing_the_Dragon', aliases=['c290'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Facing the Dragon',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361111.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Target 1 Dragon monster you control; all monsters your opponent controls lose ATK equal to the monster\'s Level x 200. If a Dragon monster you control would be targeted or destroyed, you can banish this card from your GY instead.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c290(bot))