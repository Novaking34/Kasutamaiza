import discord
from discord.ext import commands
from discord.utils import get

class c90(commands.Cog, name="c90"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='A_Term_for_Peace', aliases=['c90'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='A Term for Peace',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321533.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='If each player has 2 or less cards in their hand: Pay LP in multiples of 1000 (max. 3000); each player draws 1 card for each 1000 LP paid, then each player discards cards from their hand equal to the number of cards drawn -1. You can banish this card from your GY, except the turn it was sent there; draw 1 card. You can only use this effect of "A Term for Peace" once per turn. You can only activate 1 "A Term for Peace" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c90(bot))