import discord
from discord.ext import commands
from discord.utils import get

class c213(commands.Cog, name="c213"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Cardinal_Fusion', aliases=['c213'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Cardinal Fusion',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2356373.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Fusion Summon 1 Fusion Monster from your Extra Deck by shuffling monsters from your hand, field or GY into the Deck as Fusion Material, including at least 1 Xyz Monster.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c213(bot))