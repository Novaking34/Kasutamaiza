import discord
from discord.ext import commands
from discord.utils import get

class c272(commands.Cog, name="c272"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Convulsion_of_Nature', aliases=['c272'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Convulsion of Nature',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360708.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='(This card\'s name is always treated as "The Agusto Winds".)\nAs long as this card remains face-up on the field, both players must turn their respective Decks upside down and proceed with the current Duel. Once per turn, during your Standby Phase: Pay 300 LP, and if you cannot, destroy this card.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c272(bot))