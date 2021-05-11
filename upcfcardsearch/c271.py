import discord
from discord.ext import commands
from discord.utils import get

class c271(commands.Cog, name="c271"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Natura_Templi_Home_of_Distasta', aliases=['c271', 'Distasta_Master_3'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Natura Templi - Home of Distasta',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360706.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Distasta Master)', inline=True)
        embed.add_field(name='Type', value='Spell/Field', inline=False)
        embed.add_field(name='Card Effect', value='When this card is activated: Add 1 "Book of Natural Distasters" and 1 "Vir the True Elementalist" from your Deck to your hand. While you control this card, the first time a Continuous Spell you control would be destroyed by card effect, it is not destroyed. During the Main Phase: You can declare 1 card type (Monster, Spell, or Trap), then excavate the top card of your Deck; if the revealed card is the declared type, destroy 1 card on the field with that card type OR shuffle 1 card from your GY with the declared card type into your Deck, also, after that, place the excavated card on the bottom of your Deck. You can only activate each effect of "Nature Templi - Home of Distasta" once per turn.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c271(bot))