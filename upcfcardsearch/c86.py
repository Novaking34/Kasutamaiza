import discord
from discord.ext import commands
from discord.utils import get

class c86(commands.Cog, name="c86"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Springtime_the_Season_of_Absolute_Abundance', aliases=['c86'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Springtime the Season of Absolute Abundance',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321526.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Field', inline=False)
        embed.add_field(name='Card Effect', value='All Beast, Plant, and Insect monsters you control gain 300 ATK/DEF. Once per turn, if all monsters you control are Beast, Plant, and/or Insect monsters (min. 1): You can add 1 Spell/Trap that specifically list "Beast", "Plant", and/or "Insect" from your Deck to your hand. When this card is sent from the field to the GY: You can Special Summon 1 Level 3 or lower Beast, Plant or Insect monster from your GY. You can only activate each effect of "Springtime the Season of Absolute Abundance" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c86(bot))