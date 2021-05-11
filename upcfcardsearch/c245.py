import discord
from discord.ext import commands
from discord.utils import get

class c245(commands.Cog, name="c245"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Magia_Dance_Simul', aliases=['c245', 'Magia_10'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Magia Dance Simul',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359465.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Magia)', inline=True)
        embed.add_field(name='Type', value='Spell/Field', inline=False)
        embed.add_field(name='Card Effect', value='During your Main Phase: You can destroy 1 other card you control or in your hand, then add 1 "Magia" card from your Deck to your hand. If this card is destroyed: You can add 1 "Magia" monster from your Deck to your hand. You can only use each effect of "Magia Dance Simul" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c245(bot))