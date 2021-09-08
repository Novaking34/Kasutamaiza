import discord
from discord.ext import commands
from discord.utils import get

class c44(commands.Cog, name="c44"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='That\'s_All_Folks', aliases=['c44'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='That\'s All Folks',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321417.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='You must pay 1000 LP to activate this card. When this card is activated: Add 1 Toon Monster from your Deck to your hand. During the 2nd Standby Phase after this card\'s activated, you can send it to the GY: Add 1 "Toontastic Kingdom" from your Deck to you hand, then, if you control no Field Spells, activate it. You can only activate 1 "That\'s All Folks" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c44(bot))