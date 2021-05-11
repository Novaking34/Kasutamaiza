import discord
from discord.ext import commands
from discord.utils import get

class c268(commands.Cog, name="c268"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Sage_of_the_Choixier', aliases=['c268', 'Choixier_6'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Sage of the Choixier',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360666.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Choixier)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Tuner/Fusion/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (1500/1500)', inline=False)
        embed.add_field(name='Monster Effect', value='Must be Special Summoned by its own effect. You can Special Summon this card (from your Extra Deck) by Tributing 1 Normal Summoned monster and banishing 1 Spell from your hand. When you activate a "Choixier" card or effect that requires you to choose the activated effect while this card is face-up on the field: You can activate this effect; Apply this card\'s effect as 1 of the unchosen effects of that card. If this card leaves the field: You can return 1 banished Spell card to your hand.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c268(bot))