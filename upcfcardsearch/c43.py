import discord
from discord.ext import commands
from discord.utils import get

class c43(commands.Cog, name="c43"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Power_Polymerization', aliases=['c43'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Power Polymerization',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321413.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Fusion Summon 1 Fusion Monster from your Extra Deck, using monsters from your hand or field as Fusion Material. If this card is used to Fusion Summon a Level 7 or lower Fusion Monster, until your opponent\'s End Phase, that monster gains 1000 ATK', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c43(bot))