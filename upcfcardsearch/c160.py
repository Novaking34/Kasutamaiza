import discord
from discord.ext import commands
from discord.utils import get

class c160(commands.Cog, name="c160"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Rodor_the_Keeper_of_Time', aliases=['c160', 'of_Time_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Rodor the Keeper of Time',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336276.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (of Time)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Psychic/Normal (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (1300/1700)', inline=False)
        embed.add_field(name='Lore Text', value='During the creation of the new world, a race of Time Keepers were born, task to keep the history of all that was going on in the world. From countless battles to becoming a leader of the First Great War, to working with a unknown species of Gem-like creatures guarding great treasures, Rodor has keep its history bound and ready, just in case history repeats itself.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c160(bot))