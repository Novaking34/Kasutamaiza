import discord
from discord.ext import commands
from discord.utils import get

class c302(commands.Cog, name="c302"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Otherwhorld', aliases=['c302'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Otherwhorld',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361245.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Target 1 Spell/Trap on the field; shuffle it into the Deck, and if you do, discard 1 card. You can only activate 1 "Otherwhorld" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c302(bot))