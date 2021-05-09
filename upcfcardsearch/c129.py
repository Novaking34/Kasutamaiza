import discord
from discord.ext import commands
from discord.utils import get

class c129(commands.Cog, name="c129"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Anu_the_Lord_of_Darkness', aliases=['c129'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Anu, the Lord of Darkness',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334887.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Normal (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (2200/1500)', inline=False)
        embed.add_field(name='Lore Text', value='Feared by all who gazes upon his power, Anu rules over the darkness with an iron fist. It is said that Anu has his potential bottled away, awaiting for someone to release his true power.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c129(bot))