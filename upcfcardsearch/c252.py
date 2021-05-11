import discord
from discord.ext import commands
from discord.utils import get

class c252(commands.Cog, name="c252"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Abyssal_Moluskraken', aliases=['c252', 'Abyssal_3'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Abyssal Moluskraken',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360286.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Abyssal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Aqua/Flip/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='9 (0/3000)', inline=False)
        embed.add_field(name='Monster Effect', value='FLIP: Look at up to 2 random cards in your opponent\'s hand, then shuffle 1 of them into the Deck. You can only use this effect of "Abyssal Moluskraken" once per turn.\nOnce per turn: You can change this card to face-down Defense Position.', inline=False)
        embed.set_footer(text='Set Code: ANCF')
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c252(bot))