import discord
from discord.ext import commands
from discord.utils import get

class c200(commands.Cog, name="c200"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Insurgent_Resurgence', aliases=['c200', 'Scorn_Operative_6'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Insurgent Resurgence',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2348903.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Scorn Operative)', inline=True)
        embed.add_field(name='Type', value='Spell/Field', inline=False)
        embed.add_field(name='Card Effect', value='If this card is activated: You can reveal 3 "Manoeuvre -" cards with different names from your Deck, your opponent chooses 1 to shuffle into your Deck, then you choose 1 to add to your hand, and shuffle the rest into your Deck. You cannot Special Summon monsters from the Extra Deck the turn you activate this card, except "Scorn Operative" monsters.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c200(bot))