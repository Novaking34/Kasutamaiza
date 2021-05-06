import discord
from discord.ext import commands
from discord.utils import get

class c32(commands.Cog, name="c32"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Retrieve_the_Hidden_Treasure', aliases=['c32','Hidden_Treasure_8'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Retrieve the Hidden Treasure',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321343.jpg')
     
        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Hidden Treasure)', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Discard 1 card; apply 1 of the following effects, depending on the number of "Retrieve the Hidden Treasure"(s) are in your GY.\n● 0+: Add 1 "Hidden Treasure" monster from your Deck to your hand.\n● 1+: Add 1 "Hidden Treasure" card from your GY to your hand, except "Retrieve the Hidden Treasure"\n● 2: Add 1 "Hidden Treasure" card from your Deck to your hand.\nIf this card is discarded: You can add 1 "Hidden Treasure" monster from your GY to your hand. You must control 2 or more Beast monsters or a "Hidden Treasure" monster to activate and resolve this effect of "Retrieve the Hidden Treasure".', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c32(bot))