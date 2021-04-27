import discord
from discord.ext import commands
from discord.utils import get

class c65(commands.Cog, name="c65"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='The_True_Tyrant_of_the_Sea', aliases=['c65','True_Tryant_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='The True Tyrant of the Sea',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321480.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (True Tyrant)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Sea Serpent/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='8 (2000/2100)', inline=False)
        embed.add_field(name='Monster Effect', value='You can Special Summon this card (from your hand) to your opponent\'s field in Defense Position, by Tributing 1 monster your opponent controls. You can only control 1 "True Tyrant" monster. During your End Phase: Return 1 other card you control to your hand. You can banish the top card of your Deck face-down; change control of this card. You can only activate each effect of "The True Tyrant of the Sea" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c65(bot))