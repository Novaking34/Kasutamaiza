import discord
from discord.ext import commands
from discord.utils import get

class c315(commands.Cog, name="c315"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='The_Keeper_of_Knowledge', aliases=['c315'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='The Keeper of Knowledge')
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361303.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Xyz/Effect (LIGHT)', inline=False)
        embed.add_field(name='Rank (ATK/DEF)', value='8 (2400/3200)', inline=False)
        embed.add_field(name='Monster Effect', value='2 Level 8 Spellcaster monsters\nSpellcaster monsters in your possession are unaffected by Spells. You can detach 1 material from this card; add 1 Spell from your GY to your hand, but you cannot activate cards or the effects of cards with the same name for the rest of this Phase. During your Main Phase: You can banish 2 Spells from your GY; destroy 1 card on the field. You can only use each effect of "The Keeper of Knowledge" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c315(bot))