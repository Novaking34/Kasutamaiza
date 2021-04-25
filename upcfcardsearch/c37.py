import discord
from discord.ext import commands
from discord.utils import get

class c37(commands.Cog, name="c37"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Hidden_Treasure_Sapphire_Cat', aliases=['c37','Hidden_Treasure_13'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Hidden Treasure Sapphire Cat')
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321353.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Hidden Treasure)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Beast/Xyz/Effect (EARTH)', inline=False)
        embed.add_field(name='Rank (ATK/DEF)', value='4 (1800/2200)', inline=False)
        embed.add_field(name='Monster Effect', value='2 Level 4 Beast monster\nIf this card is Xyz Summoned: Draw 1 card, and if it is not a "Hidden Treasure" monster, discard 1 card, also, after that, shuffle up to 3 "Hidden Treasure" cards from your GY into your Deck. You can only Xyz Summon 1 "Hidden Treasure Sapphire Cat" per turn. Once per turn, if a card is discarded from your hand by the effects of a "Hidden Treasure" monster, you can attach the discarded card to this card. (Quick Effect): You can detach 1 material from this card; this turn, Beast monsters you control can attack directly, but all battle damage is halved.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c37(bot))