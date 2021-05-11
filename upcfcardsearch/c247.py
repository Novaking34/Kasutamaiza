import discord
from discord.ext import commands
from discord.utils import get

class c247(commands.Cog, name="c247"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Maestitia_Aeternum', aliases=['c247', 'Magia_12'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Maestitia Aeternum',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359469.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Magia)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fiend/Spirit/Fusion/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='9 (2550/2350)', inline=False)
        embed.add_field(name='Monster Effect', value='1 "Magia Aevum" + 1 "Magia" monster\nMust be Special Summoned (from your Extra Deck) by banishing the above cards you control. (You do not use "Power Polymerization".) Cannot be destroyed by card effects. If this card is Special Summoned: You can banish 1 "Magia" card from your GY; send 1 Special Summoned monster your opponent controls to the GY. If this card battles a Special Summoned monster, this card gains 500 ATK/DEF during Damage Calculation only, also banish that monster at the end of the Damage Step. Once per turn, during the End Phase: Return this card to the Extra Deck, then Special Summon 1 of your banished "Magia" monsters. You can only Special Summon "Maestitia Aeternum(s)" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c247(bot))