import discord
from discord.ext import commands
from discord.utils import get

class c174(commands.Cog, name="c174"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Procession_of_Phantaclysms', aliases=['c174', 'Phantaclysms_8'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Procession of Phantaclysms',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2344816.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Phantaclysms)', inline=True)
        embed.add_field(name='Type', value='Spell/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='You can target 1 other "Phantaclysm" card you control; destroy that target, and if you do, Special Summon 1 "Phantaclysmic" monster from your Deck. During the End Phase, if this card is in the GY and a "Phantaclysmic" card was destroyed and sent to the GY by an opponent\'s card or effect this turn: You can banish this card from your GY; return 1 "Phantaclysm" card from your GY to your hand. You can only activate each effect of "Procession of Phantaclysms" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c174(bot))