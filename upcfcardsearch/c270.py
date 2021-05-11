import discord
from discord.ext import commands
from discord.utils import get

class c270(commands.Cog, name="c270"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Book_of_Natural_Disasters', aliases=['c270', 'Distasta_Master_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Book of Natural Disasters',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360701.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Distasta Master)', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Fusion Summon 1 "Distasta Master" monster, by banishing monsters from your field and/or either player\'s GY as material. If you would banish a monster you control, you can also use 1 "Vir the True Elementalist" from your Deck as material. You can only use the following effects of "Book of Natural Disasters" once per turn.\n● You can banish this card from your GY and declare 1 card type (Monster, Spell, or Trap); excavate the top card of your Deck, and if it\'s the declared Type, you can either add that card to your hand OR place that card on the bottom of the Deck and Special Summon 1 "Vir True the Elementalist" that is banished or in your GY in Defense Position, otherwise place that card on the bottom of the Deck.\n● While this card is banished, except the turn it was banished: You can shuffle this card and 1 "Vir the True Elementalist" from your field or that is banished into your Deck, then draw 1 card.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c270(bot))