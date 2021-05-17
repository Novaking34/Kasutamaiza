import discord
from discord.ext import commands
from discord.utils import get

class c314(commands.Cog, name="c314"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='The_Guardian_of_Knowledge', aliases=['c314'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='The Guardian of Knowledge')
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361302.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Xyz/Effect (DARK)', inline=False)
        embed.add_field(name='Rank (ATK/DEF)', value='9 (3200/3000)', inline=False)
        embed.add_field(name='Monster Effect', value='3 Level 9 Spellcaster monsters\nYou can also Xyz Summon this card by using 1 Rank 8 Spellcaster Xyz Monster you control as material. (Transfer its materials to this card.) If you control only Spellcaster monsters, your opponent cannot activate Spell Cards or effects. When you activate a Spell (Quick Effect): You can detach 1 material from this card; banish 1 card on the field. During your Main Phase: You can banish 3 Spells from your GY; Special Summon 1 Spellcaster monster from your GY, but it cannot activate its effects this turn. You can only use each effect of "The Guardian of Knowledge" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c314(bot))