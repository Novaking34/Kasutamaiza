import discord
from discord.ext import commands
from discord.utils import get

class Embed(commands.Cog, name="c2"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Jaw_Blades', aliases=['c2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Jaw Blades',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2304599.jpg')

        embed.add_field(name='Status', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Equip', inline=False)
        embed.add_field(name='Card Effect', value='Equip only to a Beast, DInosaur, or Dragon monster. If equipped to "Flame-Claws Dragon", The equipped monster gains 1000 ATK, otherwise, the equipped monster gains 600 ATK/DEF. The equipped monster cannot attack an Attack Position monster whose ATK is less than or equal to half the equipped monster\'s ATK. If this card is destroyed by your own card effect: You can return it to the Deck.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Embed(bot))