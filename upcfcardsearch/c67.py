import discord
from discord.ext import commands
from discord.utils import get

class c67(commands.Cog, name="c67"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='The_True_Tyrant_of_the_World', aliases=['c67','True_Tryant_3'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='The True Tyrant of the World',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321483.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (True Tyrant)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Warrior/Effect (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='8 (2200/2700)', inline=False)
        embed.add_field(name='Monster Effect', value='You can Special Summon this card (from your hand) to your opponent\'s side of the field in Attack Position, by Tributing 1 monster they control. You can only control 1 "True Tryant" monster. During your End Phase: You can banish the top card of your Deck, face down; change control of this card. At the start of your Main Phase 1, either banish 1 card from your hand, face down, or take 700 damage.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c67(bot))