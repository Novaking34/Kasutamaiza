import discord
from discord.ext import commands
from discord.utils import get

class c259(commands.Cog, name="c259"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Abyssal_Awakening', aliases=['c259', 'Abyssal_10'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Abyssal Awakening',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360321.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Abyssal)', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Send 1 "Abyssal" card from your hand or field to the GY, and if you do, Set 1 "Abyssal" card with a different type (Monster, Spell or Trap) from your Deck to your field, and if it was a Spell/Trap Card, you can activate it this turn. You can only activate 1 "Abyssal Awakening" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c259(bot))