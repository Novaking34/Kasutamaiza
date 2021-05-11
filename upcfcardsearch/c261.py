import discord
from discord.ext import commands
from discord.utils import get

class c261(commands.Cog, name="c261"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Rise_of_the_Abyssals', aliases=['c261', 'Abyssal_12'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Rise of the Abyssals',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360625.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Abyssal)', inline=True)
        embed.add_field(name='Type', value='Trap/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='Once per turn: You can activate 1 of these effects.\n● Change 1 Set "Abyssal" monster on the field to face-up Attack or Defense Position.\n● Change 1 face-up "Abyssal" monster on the field to face-down Defense Position.\nYou can banish this card from your GY, then target 3 "Abyssal" monsters in your GY; shuffle them into the Deck, then draw 1 card.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c261(bot))