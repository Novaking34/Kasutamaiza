import discord
from discord.ext import commands
from discord.utils import get

class c251(commands.Cog, name="c251"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Abyssal_Miggho', aliases=['c251', 'Abyssal_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Abyssal Miggho',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360282.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Abyssal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Reptile/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (0/0)', inline=False)
        embed.add_field(name='Monster Effect', value='If this card on the field is destroyed: Special Summon 1 "Abyssal" monster from your Deck in face-up Attack Position or face-down Defense Position. You can only use the effect of "Abyssal Miggho" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c251(bot))