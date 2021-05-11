import discord
from discord.ext import commands
from discord.utils import get

class c230(commands.Cog, name="c230"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Judgment_of_Zeus', aliases=['c230'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Judgment of Zeus',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359196.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Activate one of the following effects:\n● If your opponent controls 5 or more face-up monsters: Banish all face-up monsters your opponent controls.\n● If your opponent controls 5 or more Spells/Traps: Banish all Spells and Traps your opponent controls.\nYou can only activate 1 "Judgment of Zeus" per turn. If you controlled no other cards when you activated this card, its activation and effect cannot be negated.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c230(bot))