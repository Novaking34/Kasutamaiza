import discord
from discord.ext import commands
from discord.utils import get

class c215(commands.Cog, name="c215"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Triple_Moon_Dragon', aliases=['c215'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Triple Moon Dragon',
                              color=0xcccccc)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2356380.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Dragon/Tuner/Synchro/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (300/300)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Tuner + 1 non-Tuner monster\nWhen this card is Synchro Summoned: You can Special Summon up to 3 Level 3 non-Tuner monsters from your hand in Defense Position, but their effects negated, also, for the rest of this turn, you cannot Special Summon monsters from the Extra Deck, except Xyz and Fusion Monsters. You can only Synchro Summon 1 "Triple Moon Dragon" per turn. If this card is destroyed by battle or card effect: You can target 1 "Numeric 4: Quantum Sun Dragon" in your GY; Special Summon it. You can only activate this effect of "Triple Moon Dragon" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c215(bot))