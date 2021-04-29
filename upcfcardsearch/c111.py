import discord
from discord.ext import commands
from discord.utils import get

class c111(commands.Cog, name="c111"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='TerrorBear', aliases=['c111'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='TerrorBear',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321573.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Beast-Warrior/Toon/Fusion/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (2100/2400)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Toon Monster + 1 DARK monster\nWhile you control "That\'s All Folks" and your opponent controls no other Toon Monsters, this card can attack your opponent directly. You can only Special Summon 1 "TerrorBear" per turn. Once per turn: You can target 1 Toon Monster in your GY and 1 card on the field; banish the first target, then, return the second target to the Deck.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c111(bot))