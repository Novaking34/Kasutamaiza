import discord
from discord.ext import commands
from discord.utils import get

class c79(commands.Cog, name="c79"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Light_Spire', aliases=['c79'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Light Spire',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321508.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Draw 1 card, then reveal it. Until the end of this turn, you cannot activate cards of the same name as the card you drew, also, you must keep that card revealed. You can banish this card from your GY, except the turn it was sent there; this turn, your opponent must reveal their hand. You can only activate 1 "Light Spire" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c79(bot))