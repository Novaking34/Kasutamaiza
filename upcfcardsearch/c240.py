import discord
from discord.ext import commands
from discord.utils import get

class c240(commands.Cog, name="c240"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Magia_Virga', aliases=['c240', 'Magia_5'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Magia Virga',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359264.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Magia)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Effect (WIND)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (1500/1500)', inline=False)
        embed.add_field(name='Monster Effect', value='If this card is Normal or Special Summoned: You can add 1 "Magia Dance" Spell/Trap from your Deck to your hand. If this card is destroyed by a card effect: You can add 1 "Magia" card from your GY to your hand. You can only use each effect of "Magia Virga" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c240(bot))