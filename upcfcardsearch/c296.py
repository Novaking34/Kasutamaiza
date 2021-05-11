import discord
from discord.ext import commands
from discord.utils import get

class c296(commands.Cog, name="c296"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Blazing_Azure', aliases=['c296'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Blazing Azure',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361142.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (2100/1900)', inline=False)
        embed.add_field(name='Monster Effect', value='When a monster on the field that was Special Summoned from the Extra Deck activates its effect (Quick Effect): You can Tribute this card from your hand or face-up field; negate the activation. You can only use this effect of "Blazing Azure" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c296(bot))