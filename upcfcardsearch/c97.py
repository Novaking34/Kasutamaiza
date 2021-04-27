import discord
from discord.ext import commands
from discord.utils import get

class c97(commands.Cog, name="c97"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Outerworld_Fusion', aliases=['c97'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Outerworld Fusion',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321544.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Fusion Summon 1 Level 6 or lower Fusion monster, by banishing monsters from your hand, field or GY as material. Monsters Special Summoned by this effect cannot be destroyed by card effects. During the 3rd End Phase after this card was activated: Return that Fusion Summoned monster to the Extra Deck.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c97(bot))