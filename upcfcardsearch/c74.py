import discord
from discord.ext import commands
from discord.utils import get

class c74(commands.Cog, name="c74"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Catastrophic_Fusion', aliases=['c74'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Catastrophic Fusion',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321496.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='(This card is always treated as "Power Polymerization")\nFusion Summon 1 Fusion Monster from your Extra Deck, by sending Fusion Materials from your hand or field to the GY, and if you do, each player destroys 1 card they control, or, if "A True Catastrophe" was used as Fusion Material, you can send 1 card on the field to the GY instead.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c74(bot))