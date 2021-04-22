import discord
from discord.ext import commands
from discord.utils import get

class c38(commands.Cog, name="c38"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Hidden_Treasure_Silver_Crystal_Dragon', aliases=['c38'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Hidden Treasure Silver Crystal Dragon')
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321354.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Hidden Treasure)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Beast/Xyz/Effect (EARTH)', inline=False)
        embed.add_field(name='Rank (ATK/DEF)', value='4 (2000/1900)', inline=False)
        embed.add_field(name='Monster Effect', value='2+ Level 4 Beast monsters\nThis card gains 200 ATK/DEF for each material attached to this card. Once per turn, if a card is discarded from your hand by the effects of a "Hidden Treasure" monster, you can attach the discarded card to this card. Once per turn (Quick Effect): You can detach 2 materials from this card, then target 1 card on each field; return them to the hand.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c38(bot))