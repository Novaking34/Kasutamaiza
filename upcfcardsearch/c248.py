import discord
from discord.ext import commands
from discord.utils import get

class c248(commands.Cog, name="c248"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Maestitia_Gloria', aliases=['c248', 'Magia_13'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Maestitia Gloria',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359474.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Magia)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fiend/Spirit/Fusion/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='8 (2350/2150)', inline=False)
        embed.add_field(name='Monster Effect', value='1 "Magia Gladio" + 1 "Magia" monster\nMust be Special Summoned (from your Extra Deck) by banishing the above cards you control. (You do not use "Power Polymerization".) Cannot be destroyed by card effects. If this card is Special Summoned: You can banish 1 "Magia" card from your GY; change up to 2 face-up monsters on the field to face-down Defense Position. If this card battles a Defense Position monster, this card gains 500 ATK/DEF during Damage Calculation only, also, inflict double piercing Battles Damage to your opponent. Once per turn, during the End Phase: Return this card to the Extra Deck, then Special Summon 1 of your banished "Magia" monsters. You can only Special Summon "Maestitia Gloria(s)" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c248(bot))