import discord
from discord.ext import commands
from discord.utils import get

class c58(commands.Cog, name="c58"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Kanma_the_Comedic_Reaper', aliases=['c58'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Kanma the Comedic Reaper',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321469.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Psychic/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (500/1400)', inline=False)
        embed.add_field(name='Monster Effect', value='If this card is Normal Summoned: Send 1 Level 3 or lower Psychic monster from your Deck to the GY. During the Main Phase, except the turn this card was Summoned: You can banish this card, then target 1 Level 3 or lower Psychic monster in your GY; Special Summon that target. During your Standby Phase, if you control only Level 3 or lower Psychic monsters (min. 1), and this card is banished: You can Special Summon it.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c58(bot))