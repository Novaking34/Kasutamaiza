import discord
from discord.ext import commands
from discord.utils import get

class c75(commands.Cog, name="c75"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Contract_of_Good_Faith', aliases=['c75'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Contract of Good Faith',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321498.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Target 1 monster in your GY with a Level/Rank, then send 1 card from your hand or Extra Deck with the same Level/Rank as the targeted card\'s to the GY; add that target to your hand or Extra Deck, then you lose LP equal to that targets Level/Rank x 300. You can only activate 1 "Contract of Good Faith" per turn. You cannot activate the effects of the monster sent to the GY for the activation of this card.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c75(bot))