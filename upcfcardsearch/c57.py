import discord
from discord.ext import commands
from discord.utils import get

class c57(commands.Cog, name="c57"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='High_Power_&_Low_Energy', aliases=['c57'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='High Power & Low Energy',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321468.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Beast-Warrior/Tuner/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (0/1800)', inline=False)
        embed.add_field(name='Monster Effect', value='When your opponent would Special Summon a monster(s) from the Extra Deck with 2600 or more ATK (Quick Effect): You can discard this card; return that monster(s) to the Deck, then, if all of the monsters that were used for the Summon of that monster are in the GYs, your opponent can Special Summon them in Defense Position. Until the end of this turn, neither player can Summon monsters from the Extra Deck.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c57(bot))