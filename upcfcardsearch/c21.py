import discord
from discord.ext import commands
from discord.utils import get

class c21(commands.Cog, name="c21"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Temporal_Fusion', aliases=['c21','Temporal_12'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Temporal Fusion',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2320752.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Temporal)', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Fusion Summon 1 Fusion Monster by sending Aqua, Pyro and/or Rock monsters from your hand or field to the GY, or shuffling banished "Temporal" monsters into the Deck as Fusion Material. Once per turn, during either players Main Phase, except the turn this card was sent to the GY, you can banish this card from your GY; return 1 banished "Temporal" monster to the GY.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c21(bot))