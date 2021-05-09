import discord
from discord.ext import commands
from discord.utils import get

class c121(commands.Cog, name="c121"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Little_Witch_Yui', aliases=['c121'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Little Witch Yui')
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334789.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Xyz/Effect (DARK)', inline=False)
        embed.add_field(name='Rank (ATK/DEF)', value='3 (1800/0)', inline=False)
        embed.add_field(name='Monster Effect', value='2 Level 3 monsters\nIf this card is Xyz Summoned: You can target 1 Normal Spell in your GY; attach that card to this card as material. You can only Xyz Summon 1 "Little Witch Yui" per turn. Once per turn: You can detach 1 material from this card, then apply the following effects, based on the number of material on this card, also, after that, if you detached a Normal Spell, this card cannot be destroyed by card effects until the start of your next Main Phase.\n● 2+: Target card\'s on the field, up to the number of material on this card; destroy them, then change this cards battle position.\n● 1: This card\'s ATK/DEF becomes 2500 until the End Phase.\n● 0: Add 1 Normal Spell from your GY to your hand.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c121(bot))