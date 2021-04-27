import discord
from discord.ext import commands
from discord.utils import get

class c89(commands.Cog, name="c89"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='We_Bond_Together', aliases=['c89'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='We Bond Together',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321531.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Field', inline=False)
        embed.add_field(name='Card Effect', value='Discard 1 card; Fusion Summon 1 Fusion Monster from your Extra Deck, using monsters from your field and up to 1 monster your opponent controls as Fusion Material. You can only activate 1 "We Bond Together" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c89(bot))