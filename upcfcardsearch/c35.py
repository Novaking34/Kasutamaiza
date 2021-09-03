import discord
from discord.ext import commands
from discord.utils import get

class c35(commands.Cog, name="c35"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Treasured_Assault', aliases=['c35','Hidden_Treasure_11'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Treasured Assault',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://images.duelingbook.com/custom-pics/2300000/2321349.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Hidden Treasure)', inline=True)
        embed.add_field(name='Type', value='Trap/Counter', inline=False)
        embed.add_field(name='Card Effect', value='When a Spell/Trap Card or effect is activated, OR when a monster(s) would be Special Summoned from the Deck or Extra Deck: Discard 2 cards or 1 "Hidden Treasure" monster; negate that card\'s activation or Summon, then destroy that card. If this card is discarded: You can Set this card directly to the field, but banish it when it leaves the field. You must control 2 or more Beast monster or a "Hidden Treasure" monster to activate and resolve this effect.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c35(bot))