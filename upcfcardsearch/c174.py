import discord
from discord.ext import commands
from discord.utils import get

class c174(commands.Cog, name="c174"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Phantom_Sightings', aliases=['c174', 'Phantaclysms_7'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Phantom Sightings',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2344812.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Phantaclysms)', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Add 1 "Phantaclysm" Spell/Trap from your Deck to your hand. You can only activate 1 "Phantom Sightings" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c174(bot))