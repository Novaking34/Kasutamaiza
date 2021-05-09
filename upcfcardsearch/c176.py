import discord
from discord.ext import commands
from discord.utils import get

class c176(commands.Cog, name="c176"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Phantaclysmic_Commandments', aliases=['c176', 'Phantaclysms_9'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Phantaclysmic Commandments',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2344820.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Phantaclysms)', inline=True)
        embed.add_field(name='Type', value='Trap/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='Once per turn: You can target 1 card on the field, or in either player\'s GY; destroy 1 "Phantaclysm" card in your hand or field, except "Phantaclysmic Commandments", and if you do, return the targeted card to its owners hand and all activated card effects with the same name as the targeted card are negated until the end of the turn. If you activate another "Phantaclysmic Commandments": Send this card to the GY.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c176(bot))