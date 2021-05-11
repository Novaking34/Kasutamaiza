import discord
from discord.ext import commands
from discord.utils import get

class c242(commands.Cog, name="c242"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Magia_Dance_Fortitudo', aliases=['c242', 'Magia_7'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Magia Dance Fortitudo',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359454.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Magia)', inline=True)
        embed.add_field(name='Type', value='Spell/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='If a "Magia" monster(s) is banished: You can target 1 card on the field; destroy it. If this card on the field is destroyed by a card or effect in your possession: You can add 1 "Magia Dance" card from your Deck to your hand. You can only use each effect of "Magia Dance Fortidudo" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c242(bot))