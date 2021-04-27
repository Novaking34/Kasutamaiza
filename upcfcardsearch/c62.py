import discord
from discord.ext import commands
from discord.utils import get

class c62(commands.Cog, name="c62"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Shellman_of_the_Sea', aliases=['c62'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Shellman of the Sea',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321476.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Aqua/Flip/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (200/300)', inline=False)
        embed.add_field(name='Monster Effect', value='FLIP: Your opponent returns 1 card they control to their Deck.\nIf this card is destroyed and sent to the GY: Special Summon up to 2 "Shellman of the Sea" from your hand or Deck.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c62(bot))