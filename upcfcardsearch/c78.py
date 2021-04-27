import discord
from discord.ext import commands
from discord.utils import get

class c78(commands.Cog, name="c78"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Grand_Fireplace', aliases=['c78'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Grand Fireplace',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321502.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Field', inline=False)
        embed.add_field(name='Card Effect', value='When this card is activated: Send 1 Pyro monster from your Deck to the GY. Once per turn: You can reveal 1 Pyro monster from your hand; shuffle that monster into your Deck, then Special Summon 1 Pyro monster with a different name from your GY, but its effects are negated this turn, also, for the rest of this turn, you cannot Special Summon monsters, except Pyro monsters. You can only activate 1 "Grand Fireplace" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c78(bot))