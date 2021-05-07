import discord
from discord.ext import commands
from discord.utils import get

class c200(commands.Cog, name="c200"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Manoeuvre_Death_March', aliases=['c200', 'Scorn_Operative_7'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Manoeuvre - Death March',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2348905.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Scorn Operative)', inline=True)
        embed.add_field(name='Type', value='Spell/Quick-Play', inline=False)
        embed.add_field(name='Card Effect', value='Cannot be activated from the Deck, unless its activation conditions are met. If you control a "Scorn Operative" monster and 3 or more "Manoeuvre -" cards: Special Summon as many "Scorn Operatives - Sundown" from your Extra Deck as possible, and if you do, send as many "Scorn Operatives - Sundown" from your Extra Deck to the GY as possible.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c200(bot))