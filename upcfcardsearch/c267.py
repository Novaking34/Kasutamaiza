import discord
from discord.ext import commands
from discord.utils import get

class c267(commands.Cog, name="c267"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Choixier_Temptation', aliases=['c267', 'Choixier_5'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Choixier Temptation',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360662.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Choixier)', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Pay 1000 LP, then activate 1 of the following effects;\n● Send 1 card your opponent controls to the GY.\n● Draw 1 card during the End Phase.\nYou can only activate each effect of "Choixier Temptation" once per turn.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c267(bot))