import discord
from discord.ext import commands
from discord.utils import get

class c82(commands.Cog, name="c82"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Path_of_Absolute_Darkness', aliases=['c82'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Path of Absolute Darkness',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321517.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Reveal 1 LIGHT Monster in your hand; add 1 DARK Monster with the same Level and Type as the revealed monster to your hand, then shuffle the revealed monster into your Deck. You can banish this card from your GY, except the turn it was sent to the GY; Special Summon 1 DARK Monster from your hand, but its effects are negated. You can only activate each effect of "Path of Absolute Darkness" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c82(bot))