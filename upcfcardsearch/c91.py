import discord
from discord.ext import commands
from discord.utils import get

class c91(commands.Cog, name="c91"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Cosmic_Absolution', aliases=['c91'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Cosmic Absolution',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321534.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='At the start of your Main Phase 1: Pay 4000 LP; banish the top 10 cards of your Deck, face down, then draw 2 cards, and if you have more cards in your hand than your opponent, discard cards until you have the same number of cards. For the rest of the turn, you cannot activate or resolve card effects. You can only activate 1 "Cosmic Absolution" per Duel.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c91(bot))