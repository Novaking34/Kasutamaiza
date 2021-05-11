import discord
from discord.ext import commands
from discord.utils import get

class c228(commands.Cog, name="c228"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Dark_Tornado', aliases=['c228'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Dark Tornado',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359190.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Target 1 Spell/Trap your opponent controls; destroy it. Your opponent cannot activate the targeted card, or its effects, in response to this card\'s activation.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c228(bot))