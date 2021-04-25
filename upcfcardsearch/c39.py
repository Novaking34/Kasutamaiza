import discord
from discord.ext import commands
from discord.utils import get

class c39(commands.Cog, name="c39"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Hidden_Treasure_Mystical_Ball', aliases=['c39','Hidden_Treasure_15'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Hidden Treasure Mystical Ball',
                              color=0x00008B)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321355.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Hidden Treasure)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Beast/Xyz/Effect (EARTH)', inline=False)
        embed.add_field(name='Link Rating (ATK/Link Arrows)', value='1 (0/⬇️)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Beast monster\nIf this card is Link Summoned using a "Hidden Treasure" monster, you take no battle damage involving battles with this card. Each time a card is discarded from your hand by the effects of a "Hidden Treasure" monster, you can shuffle 1 card from your GY into your Deck. Once per turn, during your opponent\'s Main Phase or your Battle Phase, if this card is in your GY (Quick Effect): You can target 1 "Hidden Treasure" Xyz Monster you control; attach this card and 1 other "Hidden Treasure" monster to that target as material, but banish this card when it is sent to the GY.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c39(bot))