import discord
from discord.ext import commands
from discord.utils import get

class c81(commands.Cog, name="c81"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Palace_of_the_Pale_Moonlight', aliases=['c81'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Palace of the Pale Moonlight',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321515.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Field', inline=False)
        embed.add_field(name='Card Effect', value='When this card is activated: Add 1 Level 3 or lower DARK Normal Monster from your Deck to your hand. DARK Normal Monsters gain 200 ATK/DEF. Once per turn: You can banish 1 DARK monster you control, face-down; add 1 Spell/Trap from your Deck that specifically lists "DARK Normal Monster" in its card text to your hand, but you cannot activate cards with that name for the rest of this turn. You can only activate 1 "Palace of the Pale Moonlight" effect per turn, and only once that turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c81(bot))