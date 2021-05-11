import discord
from discord.ext import commands
from discord.utils import get

class c258(commands.Cog, name="c258"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Abyssal_Ambush', aliases=['c258', 'Abyssal_9'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Abyssal Ambush',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360320.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Abyssal)', inline=True)
        embed.add_field(name='Type', value='Spell/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='You can Normal Set Level 5 or higher monsters without Tributing. Once per turn: You can reveal any number of "Abyssal" monsters in your hand and shuffle them into the Deck, then draw cards equal to the number of cards you shuffled into the Deck. If this face-up card is sent to the GY by an opponent\'s card: You can add 1 "Abyssal" card from your Deck to your hand.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c258(bot))