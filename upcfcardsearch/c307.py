import discord
from discord.ext import commands
from discord.utils import get

class c307(commands.Cog, name="c307"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Netherworld\'s_Gaze', aliases=['c307'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Netherworld\'s_Gaze',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361266.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Continous', inline=False)
        embed.add_field(name='Card Effect', value='Each face-up monster on the field loses ATK equal to its original ATK. Once during your Standby Phase, banish 1 Spell/Trap from your hand or GY or destroy this card.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c307(bot))