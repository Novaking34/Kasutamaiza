import discord
from discord.ext import commands
from discord.utils import get

class c45(commands.Cog, name="c45"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Toontastic_Kingdom', aliases=['c45'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Toontastic Kingdom',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321419.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Field', inline=False)
        embed.add_field(name='Card Effect', value='When this card is activated: All non-Toon Monsters you control are banished face-down, then if you control no monsters, take 2000 LP. This card\'s name becomes "That\'s All Folks" while in the Field Zone. Your opponent cannot target Toon Monsters you control with card effects. If a Toon Monster(s) you control would be destroyed by battle or card effect, you can banish 1 Toon Monster from your Deck instead.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c45(bot))