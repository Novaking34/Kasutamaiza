import discord
from discord.ext import commands
from discord.utils import get

class c195(commands.Cog, name="c195"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Scorn_Operative_Lunatic', aliases=['c195', 'Scorn_Operative_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Scorn Operative - Lunatic',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2348895.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Scorn Operative)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Gemini/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (1700/1200)', inline=False)
        embed.add_field(name='Monster Effect', value='This card is treated as a Normal Monster while face-up on the field or in the GY. While this card is a Normal Monster on the field, you can Normal Summon it to have it become an Effect Monster with this effect.\n● You can Tribute this card; Special Summon 2 "Scorn Operative" monsters with different names from your Deck, but their effects are negated.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c195(bot))