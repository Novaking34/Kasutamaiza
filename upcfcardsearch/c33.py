import discord
from discord.ext import commands
from discord.utils import get

class c33(commands.Cog, name="c33"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='The_Hidden_Treasure', aliases=['c33'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='The Hidden Treasure',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321346.jpg')
       
        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Hidden Treasure)', inline=True)
        embed.add_field(name='Type', value='Spell/Field', inline=False)
        embed.add_field(name='Card Effect', value='When this card is activated: Add 1 "Hidden Treasure" card from your Deck to your hand. Beast monsters you control gain 100 ATK/DEF for each Beast monster in the GY. If a "Hidden Treasure" monster is discarded by the effect of a "Hidden Treasure" monster with a different name: You can Special Summon that monster. During your End Phase: You can discard 1 card; draw 1 card, also Beast monsters cannot be destroyed by your opponent\'s card effects until the start of your next Standby Phase. You can only activate 1 "The Hidden Treasure" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c33(bot))