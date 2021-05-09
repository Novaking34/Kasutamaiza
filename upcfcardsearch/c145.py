import discord
from discord.ext import commands
from discord.utils import get

class c145(commands.Cog, name="c145"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Gozen_the_Dragon_Guard_of_Spellspire', aliases=['c145', 'Spellspire_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Gozen the Dragon Guard of Spellspire',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336211.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Spellspire)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Dragon/Normal (WIND)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='7 (400/2800)', inline=False)
        embed.add_field(name='Lore Text', value='Even though Gozen isn\'t the strongest fighter, the mages that guard the Spellspire entrust him to guard the ground floor. His defensive maneuvers are unmatched but his offensive needs work.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c145(bot))