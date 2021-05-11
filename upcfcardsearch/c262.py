import discord
from discord.ext import commands
from discord.utils import get

class c262(commands.Cog, name="c262"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Chthulu_the_First_Abyssal', aliases=['c262', 'Abyssal_13'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Chthulu, the First Abyssal',
                              color=0x00008B)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360628.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Abyssal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fiend/Link/Effect (WATER)', inline=False)
        embed.add_field(name='Link Rating (ATK/Link Arrows)', value='3 (3000/↙️⬇️↘️)', inline=False)
        embed.add_field(name='Monster Effect', value='3 "Abyssal" monsters\nUnaffected by your opponent\'s card effects. Once per turn: You can activate 1 of these effects.\n● Banish monsters your opponent controls, up to the number of "Abyssal" monsters you control.\n● Banish Spells/Traps your opponent controls, up to the number of face-down monsters you control.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c262(bot))