import discord
from discord.ext import commands
from discord.utils import get

class c173(commands.Cog, name="c173"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='House_of_Phantaclysms', aliases=['c173', 'Phantaclysms_6'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='House of Phantaclysms',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2344810.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Phantaclysms)', inline=True)
        embed.add_field(name='Type', value='Spell/Field', inline=False)
        embed.add_field(name='Card Effect', value='Any Battle Damage involving a "Phantaclysmic" monster and another monster is reduced to 0. You can reveal 1 card in your hand and send 1 "Phantaclysmic" card from your Deck to the GY; destroy the revealed card, and if you do, you can return 1 "Phantaclysm" card from your GY to your hand. You cannot Summon monsters, except "Phantaclysmic" monsters, the turn you activate this effect, You can only activate this effect of "House of Phantaclysms" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c173(bot))