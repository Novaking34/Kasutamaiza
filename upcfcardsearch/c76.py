import discord
from discord.ext import commands
from discord.utils import get

class c76(commands.Cog, name="c76"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Enchanted_Forest_of_Springtime', aliases=['c76'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Enchanted Forest of Springtime',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321498.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='When this card is activated: You can take 1 Plant monster from your GY and either place it on top or bottom of your Deck. Once per turn: You can Tribute 1 Plant monster you control; Special Summon 1 Level 4 or lower Plant monster from your GY, but its effects are negated this turn, also banish it when it leaves the field. During your Standby Phase: Gain 200 LP for each Plant monster in your GY.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c76(bot))