import discord
from discord.ext import commands
from discord.utils import get

class c66(commands.Cog, name="c66"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='The_True_Tyrant_of_the_Sky', aliases=['c66','True_Tryant_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='The True Tyrant of the Sky',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321481.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (True Tyrant)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Winged Beast/Effect (WIND)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='8 (1800/2800)', inline=False)
        embed.add_field(name='Monster Effect', value='You can Special Summon this card (from your hand) to your opponent\'s field in Defense Position, by Tributing 1 monster your opponent controls. You can only control 1 "True Tyrant" monster. As long as you control this card, you cannot Special Summon monsters directly from your Main Deck. You can banish the top card of your Deck face-down; change control of this card.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c66(bot))