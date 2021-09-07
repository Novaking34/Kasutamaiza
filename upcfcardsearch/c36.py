import discord
from discord.ext import commands
from discord.utils import get

class c36(commands.Cog, name="c36"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Hidden_Treasure_Rainbow_Gem_Dragon', aliases=['c36','Hidden_Treasure_12'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Hidden Treasure Rainbow Gem Dragon')
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321351.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Hidden Treasure)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Beast/Xyz/Effect (EARTH)', inline=False)
        embed.add_field(name='Rank (ATK/DEF)', value='5 (2400/2000)', inline=False)
        embed.add_field(name='Monster Effect', value='3 Level 5 Beast monster\nDuring your Main Phase 2: You can also Xyz Summon this card using 1 Rank 4 Beast Xyz Monster with no material as material, but if Summoned this way, you cannot activate this card\'s effect this turn. You can only Special Summon 1 "Hidden Treasure Rainbow Gem Dragon" per turn this way. This card gains 300 ATK/DEF for each material attached to this card. Up to twice per turn, if a card is discarded from your hand by the effects of a "Hidden Treasure" card, you can attach the discarded card to this card after that effect resolves. Once per turn (Quick Effect): You can detach any number of materials from this card, then target the same number of cards on the field; return them to the hand.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c36(bot))