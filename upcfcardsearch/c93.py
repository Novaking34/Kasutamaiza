import discord
from discord.ext import commands
from discord.utils import get

class c93(commands.Cog, name="c93"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Dra-co_World_Ea-ter', aliases=['c93'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Dra-co World Ea-ter',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321537.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Counter', inline=False)
        embed.add_field(name='Card Effect', value='When a Field Spell Card or effect is activated: Pay 1000 LP; negate the activation, then, destroy that card. You can banish this card from your GY, except the turn it was sent to the GY; add 1 Field Spell from your Deck to your hand. You can only use this effect of "Dra-Co World Ea-ter" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c93(bot))