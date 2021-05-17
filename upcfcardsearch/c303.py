import discord
from discord.ext import commands
from discord.utils import get

class c303(commands.Cog, name="c303"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='The_City_of_the_Unreturned', aliases=['c303'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='The City of the Unreturned',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361247.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='All monsters in the GYs become Rock monster. Once per turn, if a Rock monster(s) you control would be destroyed, you can banish an equal amount of Rock monsters from the GY(s) instead. If this card is sent to the GY: You can add 1 Rock monster from your Deck to your hand. You can only use this effect of "The City of the Unreturned" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c303(bot))