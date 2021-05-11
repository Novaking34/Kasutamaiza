import discord
from discord.ext import commands
from discord.utils import get

class c241(commands.Cog, name="c241"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Magia_Dance_Armis', aliases=['c241', 'Magia_6'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Magia Dance Armis',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359451.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Magia)', inline=True)
        embed.add_field(name='Type', value='Spell/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='During your Main Phase, if you control another "Magia" card: You can destroy 1 other card you control or in your hand, and if you do, you can shuffle 1 banished card into the Deck. If this card on the field is destroyed by a card or effect in your possession: You can add 1 "Magia Dance" card from your Deck to your hand. You can only use each effect of "Magia Dance Armis" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c241(bot))