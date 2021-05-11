import discord
from discord.ext import commands
from discord.utils import get

class c236(commands.Cog, name="c236"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Magia_Aevum', aliases=['c236', 'Magia_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Magia Aevum',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359250.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Magia)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='7 (2300/2100)', inline=False)
        embed.add_field(name='Monster Effect', value='If this card battles a Special Summoned monster, it gains 500 ATK/DEF during Damage Calculation only. You can only use each of the following effects of "Magia Aevum" once per turn. If 2 or more cards in your possession are destroyed at the same time by a card effect: You can shuffle 4 of your "Magia" cards that are banished and/or in your GY into the Deck; Special Summon this card from your hand. During your Main Phase: You can Set 1 "Magia Dance" Spell/Trap directly from your Deck, but banish it when it leaves the field.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c236(bot))